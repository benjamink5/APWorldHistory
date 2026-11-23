#!/usr/bin/env python3
"""Consistency checks for the AP World History study materials.

usage (from the repo root):
  python3 -I .claude/skills/check-materials/scripts/check.py              # every unit + Course/
  python3 -I .claude/skills/check-materials/scripts/check.py --unit 1 2   # some units
  python3 -I .claude/skills/check-materials/scripts/check.py Unit1/Notes/AP_WH_1.2_Notes_EN.md
  ... --render     # also draw every Mermaid diagram with the md-to-pdf skill (slow: ~1 s/file)
  ... --quiet      # print problems only

Checks:
  pairs      EN/KR twins: same counts of headings, table rows, Mermaid blocks, ⚠️
  chars      no U+FFFD replacement characters (broken Korean writes)
  cards      flashcards: per-section card counts == pie slices == "(N cards)" title,
             EN == KR, every <details> closed
  opml       well-formed XML, OPML 2.0, EN/KR outline counts equal, leaves end in a [x.y] tag
  mermaid    static rules from CLAUDE.md (quoted labels, gantt years, mindmap brackets, pie showData)
  ced        notes LO letters and HD-table KC codes match Unit<N>/Notes/AP_WH_Unit<N>_CED_EN.md
  render     (--render) every Mermaid block parses and draws

Units 3–5 were imported in a different format (CLAUDE.md). Format-convention problems in those
units (cards, OPML tags, CED tables, twins, pairs) are counted and summarized in one line instead
of listed; add --strict to list them. Exit code 1 if any error.
"""
import argparse, glob, os, re, subprocess, sys, tempfile
import xml.etree.ElementTree as ET

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
LEGACY_UNITS = {3, 4, 5}
MERMAID = re.compile(r"^```mermaid\n(.*?)^```", re.S | re.M)

errors, warnings, notes = [], [], []
legacy = []  # (check, path, msg) for Units 3–5 convention problems
STRICT = False


def rel(p):
    return os.path.relpath(p, REPO)


def unit_of(p):
    m = re.search(r"(?:^|/)Unit(\d+)/", rel(p))
    return int(m.group(1)) if m else None


def report(level, check, path, msg):
    if level == "L":
        if STRICT:
            warnings.append((check, rel(path), msg))
        else:
            legacy.append((check, rel(path), msg))
        return
    (errors if level == "E" else warnings).append((check, rel(path) if path else "", msg))


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def legacy_level(p):
    return "L" if unit_of(p) in LEGACY_UNITS else "E"


# ---------------------------------------------------------------- pairs / chars
def counts(s):
    return {
        "headings": len(re.findall(r"^#+ ", s, re.M)),
        "table rows": len(re.findall(r"^\|", s, re.M)),
        "mermaid": len(MERMAID.findall(s)),
        "⚠️": s.count("⚠️"),
    }


def check_pairs(files):
    seen = set()
    for f in files:
        if not f.endswith("_EN.md"):
            continue
        k = f[:-6] + "_KR.md"
        seen.add(f)
        if not os.path.exists(k):
            report(legacy_level(f), "pairs", f, "no KR twin")
            continue
        a, b = counts(read(f)), counts(read(k))
        diff = [f"{key} EN {a[key]} / KR {b[key]}" for key in a if a[key] != b[key]]
        if diff:
            report(legacy_level(f), "pairs", f, "; ".join(diff))
    for f in files:
        if f.endswith("_KR.md") and not os.path.exists(f[:-6] + "_EN.md"):
            report(legacy_level(f), "pairs", f, "no EN twin")


def check_chars(files):
    for f in files:
        s = read(f)
        if "�" in s:
            lines = [str(i + 1) for i, l in enumerate(s.splitlines()) if "�" in l]
            report("E", "chars", f, "U+FFFD on line(s) " + ", ".join(lines[:10]))


# ---------------------------------------------------------------- flashcards
def check_cards(files):
    totals = {}
    for f in files:
        if "_Flashcards_" not in f:
            continue
        s, lvl = read(f), legacy_level(f)
        secs = re.split(r"^## \d\.", s, flags=re.M)[1:]
        cards = [len(re.findall(r"^- \[ \] \*\*", x, re.M)) for x in secs]
        pie = re.search(r"pie showData(.*?)```", s, re.S)
        if not pie:
            report(lvl, "cards", f, "no `pie showData` chart")
            continue
        slices = [int(v) for v in re.findall(r":\s*(\d+)", pie.group(1))]
        if cards != slices:
            report(lvl, "cards", f, f"section card counts {cards} != pie {slices}")
        title = re.search(r"\((\d+) (?:cards|장)\)", pie.group(1))
        if title and int(title.group(1)) != sum(cards):
            report(lvl, "cards", f, f"pie title says {title.group(1)} cards, real total {sum(cards)}")
        o, c = s.count("<details>"), s.count("</details>")
        if not (o == c == sum(cards)):
            report(lvl, "cards", f, f"<details> {o} / </details> {c} / cards {sum(cards)}")
        totals[f] = cards
    for f, cards in totals.items():
        if f.endswith("_EN.md"):
            k = f[:-6] + "_KR.md"
            if k in totals and totals[k] != cards:
                report(legacy_level(f), "cards", f, f"EN {cards} != KR {totals[k]}")


# ---------------------------------------------------------------- OPML
def check_opml(files):
    info = {}
    for f in files:
        if not f.endswith(".opml"):
            continue
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError as e:
            report("E", "opml", f, f"not well-formed XML: {e}")
            continue
        if root.tag != "opml" or root.get("version") != "2.0":
            report("E", "opml", f, f"root is <{root.tag} version={root.get('version')}>, expected OPML 2.0")
        outlines = root.iter("outline")
        n, untagged = 0, []
        for o in outlines:
            n += 1
            text = o.get("text", "")
            if len(o) == 0 and not re.match(r"(Legend|범례)\s*:", text) and not re.search(r"\[\d+\.\d+[^\]]*\]\s*$", text):
                untagged.append(o.get("text", "")[:60])
        if untagged:
            report(legacy_level(f), "opml", f, f"{len(untagged)} leaf node(s) without a [x.y] topic tag, e.g. {untagged[0]!r}")
        info[f] = n
    for f, n in info.items():
        if "_EN" in f:
            k = f.replace("_EN", "_KR")
            if k in info and info[k] != n:
                report(legacy_level(f), "opml", f, f"outline count EN {n} != KR {info[k]}")


# ---------------------------------------------------------------- Mermaid static rules
NODE_UNQUOTED = re.compile(r"\b\w+\s*(\[|\(\(|\(|\{)(?!\")([^\]\)\}\"]*?)(\]|\)\)|\)|\})")
EDGE_UNQUOTED = re.compile(r"--+>?\|(?!\")([^|]*)\|")


def check_mermaid(files):
    for f in files:
        if not f.endswith(".md"):
            continue
        s = read(f)
        for m in MERMAID.finditer(s):
            block, line0 = m.group(1), s[: m.start()].count("\n") + 2
            lines = block.splitlines()
            kind = (lines[0].split() or [""])[0] if lines else ""
            where = lambda i: f"line {line0 + i}"
            if kind in ("flowchart", "graph"):
                for i, l in enumerate(lines[1:], 1):
                    code = l.split("%%")[0]
                    for e in EDGE_UNQUOTED.finditer(code):
                        if re.search(r"[()]", e.group(1)):
                            report("E", "mermaid", f, f"{where(i)}: unquoted edge label with parentheses: |{e.group(1)}|")
                    if re.match(r"\s*(subgraph|classDef|class|style|linkStyle|click)\b", code):
                        continue
                    for n in NODE_UNQUOTED.finditer(code):
                        if re.search(r"[()\[\]]", n.group(2)):
                            report("E", "mermaid", f, f"{where(i)}: unquoted node label with brackets: {code.strip()[:70]}")
                            break
            elif kind == "gantt":
                if not re.search(r"^\s*dateFormat\s+YYYY\s*$", block, re.M):
                    report("E", "mermaid", f, f"line {line0}: gantt without `dateFormat YYYY`")
                for i, l in enumerate(lines[1:], 1):
                    if ":" in l and not re.match(r"\s*(title|dateFormat|axisFormat|section|todayMarker|tickInterval)\b", l):
                        for y in re.findall(r"(?<![\w.])(\d{1,4})(?![\w.])", l.split(":", 1)[1]):
                            if len(y) != 4 or int(y) < 1000:
                                report("E", "mermaid", f, f"{where(i)}: gantt year {y} is not a 4-digit year >= 1000")
            elif kind == "mindmap":
                for i, l in enumerate(lines[1:], 1):
                    t = l.strip()
                    if not t or t.startswith("root((") or re.match(r"^\w*\(\(.*\)\)$", t) and i == 1:
                        continue
                    if re.search(r"[()\[\]{}]", t):
                        report("E", "mermaid", f, f"{where(i)}: mindmap node with brackets: {t[:60]}")
            elif kind == "pie" and "_Flashcards_" in f and not lines[0].strip().startswith("pie showData"):
                report(legacy_level(f), "mermaid", f, f"line {line0}: flashcard pie should be `pie showData`")


# ---------------------------------------------------------------- CED KC codes
def ced_topics(unit):
    p = os.path.join(REPO, f"Unit{unit}/Notes/AP_WH_Unit{unit}_CED_EN.md")
    if not os.path.exists(p):
        return None
    out = {}
    for t in re.split(r"^## Topic ", read(p), flags=re.M)[1:]:
        tid = t.split()[0]
        out[tid] = (
            re.findall(r"^\| (KC-[0-9A-Za-z.]+|—) \|", t, re.M),
            sorted(set(re.findall(r"^### Learning Objective ([A-Z])", t, re.M))),
        )
    return out


def check_ced(files):
    cache = {}
    for f in files:
        m = re.search(r"AP_WH_(\d+)\.(\d+)_Notes_EN\.md$", f)
        if not m:
            continue
        unit, tid = int(m.group(1)), f"{m.group(1)}.{m.group(2)}"
        if unit not in cache:
            cache[unit] = ced_topics(unit)
        ced = cache[unit]
        if ced is None:
            report("W", "ced", f, f"no CED reference file for Unit {unit}")
            continue
        if tid not in ced:
            report("E", "ced", f, f"topic {tid} not in the CED file")
            continue
        s = read(f)
        head = s.split("## Big Picture")[0]
        if "Historical Development" not in head:
            report(legacy_level(f), "ced", f, "no LO/HD tables before the Big Picture")
            continue
        kc = []
        for row in re.findall(r"^\|.*$", head, re.M):
            for k in re.findall(r"KC-[0-9IVX]+(?:\.[0-9A-Za-z]+)*", row):
                k = k.rstrip(".")
                if k not in kc:
                    kc.append(k)
        lo = sorted(set(re.findall(rf"{re.escape(tid)} LO-([A-Z])", s)))
        ckc, clo = ced[tid]
        ckc = [k for k in ckc if k != "—"]
        if kc != ckc:
            missing = [k for k in ckc if k not in kc]
            extra = [k for k in kc if k not in ckc]
            msg = f"HD-table KC codes differ from the CED: missing {missing}, extra {extra}" if (missing or extra) else f"KC order differs from the CED: {kc} vs {ckc}"
            report(legacy_level(f), "ced", f, msg)
        if lo != clo:
            report(legacy_level(f), "ced", f, f"LO letters {lo} != CED {clo}")


# ---------------------------------------------------------------- render
def check_render(files):
    md = [f for f in files if f.endswith(".md") and MERMAID.search(read(f))]
    if not md:
        return
    script = os.path.join(REPO, ".claude/skills/md-to-pdf/scripts/md2pdf.py")
    with tempfile.TemporaryDirectory() as tmp:
        r = subprocess.run([sys.executable, "-I", script, "-o", tmp, *md], capture_output=True, text=True, cwd=REPO)
    cur = None
    for line in r.stdout.splitlines():
        if line.startswith("✓") or line.startswith("✗"):
            cur = os.path.basename(line.split()[1]).replace(".pdf", ".md")
            if line.startswith("✗"):
                report("E", "render", None, line[2:])
        elif line.strip().startswith("mermaid #"):
            src = next((f for f in md if os.path.basename(f) == cur), cur)
            report("E", "render", src, line.strip())
    notes.append(f"render: drew diagrams in {len(md)} file(s)")


# ---------------------------------------------------------------- main
def collect(args):
    if args.paths:
        out = []
        for p in args.paths:
            p = os.path.abspath(p)
            if os.path.isdir(p):
                out += glob.glob(os.path.join(p, "**", "*.md"), recursive=True) + glob.glob(os.path.join(p, "**", "*.opml"), recursive=True)
            else:
                out.append(p)
                twin = p.replace("_EN.", "_KR.") if "_EN." in p else p.replace("_KR.", "_EN.")
                if twin != p and os.path.exists(twin):
                    out.append(twin)
        return sorted(set(out))
    dirs = [f"Unit{u}" for u in args.unit] if args.unit else sorted(d for d in os.listdir(REPO) if re.fullmatch(r"Unit\d+", d)) + ["Course"]
    out = []
    for d in dirs:
        out += glob.glob(os.path.join(REPO, d, "**", "*.md"), recursive=True)
        out += glob.glob(os.path.join(REPO, d, "**", "*.opml"), recursive=True)
    return sorted(out)


def main():
    ap = argparse.ArgumentParser(description="Check the study materials.")
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--unit", type=int, nargs="+")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--strict", action="store_true", help="list Units 3-5 format problems too")
    a = ap.parse_args()
    global STRICT
    STRICT = a.strict
    files = collect(a)
    checks = [("pairs", check_pairs), ("chars", check_chars), ("cards", check_cards), ("opml", check_opml),
              ("mermaid", check_mermaid), ("ced", check_ced)] + ([("render", check_render)] if a.render else [])
    for _, fn in checks:
        fn(files)
    print(f"Checked {len(files)} file(s): {len(errors)} error(s), {len(warnings)} warning(s)\n")
    for name, _ in checks:
        e = [x for x in errors if x[0] == name]
        w = [x for x in warnings if x[0] == name]
        if not e and not w:
            if not a.quiet:
                print(f"✓ {name}")
            continue
        print(f"{'✗' if e else '⚠'} {name}: {len(e)} error(s), {len(w)} warning(s)")
        for lvl, items in (("ERROR", e), ("warn ", w)):
            for _, path, msg in items:
                print(f"    {lvl} {path}: {msg}" if path else f"    {lvl} {msg}")
    if legacy:
        by = {}
        for c, _, _ in legacy:
            by[c] = by.get(c, 0) + 1
        print(f"\n· Units 3–5 (imported, different format): {len(legacy)} convention difference(s) not listed ("
              + ", ".join(f"{k} {v}" for k, v in by.items()) + "). Use --strict to list them.")
    for n in notes:
        if not a.quiet:
            print("  " + n)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
