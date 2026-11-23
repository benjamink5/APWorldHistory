"""Build AP_WH_Unit<N>_MindMap_{EN,KR}.opml from paired EN/KR region data.

Usage (from the repo root):
    python3 -I tools/mindmap/build_opml.py tools/mindmap/unit1 Unit1/Mindmaps

<unit_dir> holds meta.json (unit number, titles) plus one or more region files (*.json).
Each region file is a JSON array of:
    {"order": 1, "name_en": "...", "name_kr": "...",
     "people": [{"sort": 1206, "en": "...", "kr": "..."}],
     "events": [{"sort": 1206, "en": "...", "kr": "..."}],
     "institutions": [{"en": "...", "kr": "..."}]}
Text is plain (no Markdown, not XML-escaped); every item ends with a topic tag such as [1.3]
or [1.2, 1.7]. People and events are sorted by "sort"; ElementTree does the escaping.
"""
import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from email.utils import formatdate

unit_dir, out_dir = sys.argv[1], sys.argv[2]
with open(os.path.join(unit_dir, "meta.json"), encoding="utf-8") as f:
    meta = json.load(f)
N = meta["unit"]

regions = []
for path in sorted(glob.glob(os.path.join(unit_dir, "*.json"))):
    if os.path.basename(path) == "meta.json":
        continue
    with open(path, encoding="utf-8") as f:
        regions.extend(json.load(f))
regions.sort(key=lambda r: r["order"])

orders = [r["order"] for r in regions]
assert len(orders) == len(set(orders)), f"duplicate order values: {orders}"

TAG = re.compile(rf"\[{N}\.\d(?:, ?{N}\.\d)*\]$")
problems = []
for r in regions:
    for kind in ("people", "events", "institutions"):
        items = r.get(kind, [])
        if kind != "institutions":
            items.sort(key=lambda it: it["sort"])  # stable: keeps data order on ties
        for it in items:
            for lang in ("en", "kr"):
                t = it.get(lang, "").strip()
                if not t:
                    problems.append((r["name_en"], kind, "empty", lang))
                elif not TAG.search(t):
                    problems.append((r["name_en"], kind, "no tag", t))
                elif "\n" in t or "**" in t:
                    problems.append((r["name_en"], kind, "markup", t))
            te, tk = TAG.search(it.get("en", "").strip()), TAG.search(it.get("kr", "").strip())
            if te and tk and te.group().replace(" ", "") != tk.group().replace(" ", ""):
                problems.append((r["name_en"], kind, "tag mismatch", it["en"], it["kr"]))
if problems:
    for p in problems:
        print("PROBLEM:", p)
    sys.exit(1)

LABELS = {
    "en": {"legend": f"Legend: [{N}.x] = source topic · ⚠️ = textbook differs from most sources · Events in chronological order",
           "people": "People", "events": "Events", "institutions": "Institutions", "name": "name_en"},
    "kr": {"legend": f"범례: [{N}.x] = 출처 토픽 · ⚠️ = 교재와 일반적인 설명이 다름 · 사건은 연도순",
           "people": "인물", "events": "사건", "institutions": "제도", "name": "name_kr"},
}

date = formatdate(localtime=True)
for lang, L in LABELS.items():
    opml = ET.Element("opml", version="2.0")
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = meta[lang]["title"]
    ET.SubElement(head, "dateCreated").text = date
    body = ET.SubElement(opml, "body")
    unit = ET.SubElement(body, "outline", text=meta[lang]["unit"])
    ET.SubElement(unit, "outline", text=L["legend"])
    for r in regions:
        node = ET.SubElement(unit, "outline", text=r[L["name"]])
        for kind in ("people", "events", "institutions"):
            items = r.get(kind, [])
            if not items:
                continue
            k = ET.SubElement(node, "outline", text=L[kind])
            for it in items:
                ET.SubElement(k, "outline", text=it[lang].strip())
    ET.indent(opml, space="  ")
    out = os.path.join(out_dir, f"AP_WH_Unit{N}_MindMap_{lang.upper()}.opml")
    ET.ElementTree(opml).write(out, encoding="UTF-8", xml_declaration=True)
    with open(out, "a", encoding="utf-8") as f:
        f.write("\n")
    print("wrote", out)

for r in regions:
    print(r["order"], r["name_en"], {k: len(r.get(k, [])) for k in ("people", "events", "institutions")})
