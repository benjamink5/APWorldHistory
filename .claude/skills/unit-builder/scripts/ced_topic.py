#!/usr/bin/env python3
"""Print a topic's CED block, ready to paste into the "Topic <X.Y> content" section of
tools/briefs/1_notes_ced_draft.md. The wording is copied verbatim from
Unit<N>/Notes/AP_WH_Unit<N>_CED_EN.md (titles in Korean come from the _KR file).

usage: python3 -I .claude/skills/unit-builder/scripts/ced_topic.py 6.1 [6.2 ...]
       python3 -I .claude/skills/unit-builder/scripts/ced_topic.py --unit-line 6
       python3 -I .claude/skills/unit-builder/scripts/ced_topic.py --list 6      # topic table for the user
"""
import os, re, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def ced_files(unit):
    base = os.path.join(REPO, f"Unit{unit}/Notes/AP_WH_Unit{unit}_CED")
    en, kr = base + "_EN.md", base + "_KR.md"
    if not os.path.exists(en):
        sys.exit(f"missing {os.path.relpath(en, REPO)}: transcribe the CED first (tools/briefs/5_ced_reference_and_audit.md, 5A)")
    return read(en), read(kr) if os.path.exists(kr) else ""


def unit_line(unit):
    en, kr = ced_files(unit)
    title_en = re.search(r"^# .*CED Reference: (.+)$", en, re.M).group(1).strip()
    m = re.search(r"\*\*Period:\*\* c\. (\d{4}) to (c\. (\d{4})|the present)", en)
    period = f"c. {m.group(1)}–{m.group(3) or 'present'}" if m else ""
    mk = re.search(r"^# .*CED 정리: (.+?) \((.+)\)$", kr, re.M)
    title_kr = mk.group(1).strip() if mk else title_en
    return f"**Unit {unit}: {title_en} ({period})**", f"**Unit {unit}: {title_kr} ({title_en}, {period})**"


def topic(tid):
    unit = int(tid.split(".")[0])
    en, kr = ced_files(unit)
    blocks = {b.split()[0]: b for b in re.split(r"^## Topic ", en, flags=re.M)[1:]}
    if tid not in blocks:
        sys.exit(f"topic {tid} not found; topics in Unit {unit}: {', '.join(blocks)}")
    b = blocks[tid]
    title = b.splitlines()[0][len(tid):].strip()
    mk = re.search(rf"^## 토픽 {re.escape(tid)} (.+?) \({re.escape(title)}\)$", kr, re.M)
    out = [f"Title: **{tid} {title}** (KR: {mk.group(1) if mk else '—'})"]
    skill = re.search(r"^\*\*Suggested skill:\*\* (.+)$", b, re.M)
    if skill:
        out.append(f"Suggested skill: {skill.group(1)}")
        after = b[skill.end():].split("### Learning Objective")[0]
        for l in after.splitlines():
            if l.startswith("- "):
                out.append(f"  {l.strip()}")
    out.append("Learning Objectives and Historical Developments (use this wording):")
    for lo in re.split(r"^### Learning Objective ", b, flags=re.M)[1:]:
        lines = lo.splitlines()
        head = lines[0].strip()  # "A (CDI)"
        letter, theme = head.split(" ", 1) if " " in head else (head, "")
        text = next((l.strip() for l in lines[1:] if l.strip() and not l.startswith(("|", "*", "-", ">"))), "")
        out.append(f"- **LO {letter} {theme}:** {text}")
        for row in re.findall(r"^\| (KC-[^|]+|—) \| (.+?) \|$", lo, re.M):
            out.append(f"  - {row[0].strip()}: {row[1].strip()}")
        ex = re.search(r"^\*\*Illustrative examples\*\*\n((?:- .*\n?)+)", lo, re.M)
        if ex:
            for item in ex.group(1).strip().splitlines():
                out.append(f"  - Illustrative examples — {item[2:].strip()}")
        else:
            out.append("  - Illustrative examples: none in the CED for this LO. Do not present anything as a CED example.")
        notes = [l.strip() for l in lines if l.strip().startswith("*") and not l.startswith("**")]
        for n in notes:
            out.append(f"  - Note: {n.strip('*').strip()}")
    return "\n".join(out)


def topic_list(unit):
    en, kr = ced_files(unit)
    rows = ["| Topic | Title | Korean title | LOs | HDs | Example groups |", "|---|---|---|---|---|---|"]
    for b in re.split(r"^## Topic ", en, flags=re.M)[1:]:
        tid = b.split()[0]
        title = b.splitlines()[0][len(tid):].strip()
        mk = re.search(rf"^## 토픽 {re.escape(tid)} (.+?) \({re.escape(title)}\)$", kr, re.M)
        los = ", ".join(h.strip() for h in re.findall(r"^### Learning Objective (.+)$", b, re.M))
        review = "Review:" in b
        hds = len(re.findall(r"^\| (KC-[^|]+|—) \|", b, re.M))
        exs = len(re.findall(r"^- \*[^*]+:\*", b, re.M))
        rows.append(f"| {tid} | {title} | {mk.group(1) if mk else '—'} | {los} | {str(hds) + ' review KCs' if review else hds} | {exs} |")
    return "\n".join(rows)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    if args[0] == "--list":
        for u in args[1:]:
            print(topic_list(int(u)))
        return
    if args[0] == "--unit-line":
        for u in args[1:]:
            e, k = unit_line(int(u))
            print(f"EN: {e}\nKR: {k}")
        return
    print("\n\n".join(topic(t) for t in args))


if __name__ == "__main__":
    main()
