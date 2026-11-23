#!/usr/bin/env python3
"""Show how far a unit has gone through the build pipeline, and what to do next.

usage: python3 -I .claude/skills/unit-builder/scripts/status.py 6 [7 ...]

Reads only. Reports, per topic: notes and flashcards (EN/KR) and which source-line stage they
are in, whether the textbook OCR text exists, then the mind map and MCQ state.
"""
import glob, os, re, sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TEXTBOOK_ROOT = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Family Shared/AP-WorldHistory")
SRC_CED = "Textbook not yet incorporated"
SRC_TB = "Textbook incorporated"


def textbook_dir(unit):
    for d in sorted(glob.glob(os.path.join(TEXTBOOK_ROOT, "Unit*-*"))):
        m = re.search(r"Unit(\d+)-(\d+)$", d)
        if m and int(m.group(1)) <= unit <= int(m.group(2)):
            return os.path.join(d, "Textbook")
    return None


def stage(path):
    if not os.path.exists(path):
        return "—"
    head = open(path, encoding="utf-8").read(1500)
    if SRC_TB in head or "교재 반영 (교재" in head:
        return "textbook"
    if SRC_CED in head or "교재 반영 전" in head:
        return "CED draft"
    return "other format"


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for u in map(int, sys.argv[1:]):
        print(f"== Unit {u}")
        ced = os.path.join(REPO, f"Unit{u}/Notes/AP_WH_Unit{u}_CED_EN.md")
        if not os.path.exists(ced):
            print("  CED reference: missing (do this first: tools/briefs/5_ced_reference_and_audit.md, 5A)")
            continue
        topics = re.findall(r"^## Topic (\d+\.\d+) (.+)$", open(ced, encoding="utf-8").read(), re.M)
        tb = textbook_dir(u)
        tb_note = tb if tb and os.path.isdir(tb) else "no textbook folder found"
        print(f"  CED reference: ok ({len(topics)} topics)   textbook: {tb_note}")
        if tb and os.path.isdir(tb):
            # the folder is shared by two units; keep only this unit's PDFs ("Unit5", "Unit05", "Unit4-T1", ...)
            pdfs = [os.path.basename(p) for p in glob.glob(os.path.join(tb, "*.pdf"))
                    if re.search(rf"Unit0?{u}(?!\d)", os.path.basename(p))]
            print(f"  textbook PDFs for Unit {u}: {', '.join(sorted(pdfs)) if pdfs else 'none yet'}")
        print(f"  {'topic':<6} {'notes EN/KR':<30} {'flashcards EN/KR':<30} textbook .txt")
        counts = {"—": 0, "CED draft": 0, "textbook": 0, "other format": 0}
        for tid, title in topics:
            n = [stage(os.path.join(REPO, f"Unit{u}/Notes/AP_WH_{tid}_Notes_{l}.md")) for l in ("EN", "KR")]
            c = [stage(os.path.join(REPO, f"Unit{u}/Flashcards/AP_WH_{tid}_Flashcards_{l}.md")) for l in ("EN", "KR")]
            txt = "yes" if tb and os.path.exists(os.path.join(tb, f"{tid}.txt")) else "no"
            counts[n[0]] += 1
            print(f"  {tid:<6} {n[0] + ' / ' + n[1]:<30} {c[0] + ' / ' + c[1]:<30} {txt}")
        mm = [os.path.exists(os.path.join(REPO, f"Unit{u}/Mindmaps/AP_WH_Unit{u}_MindMap_{l}.opml")) for l in ("EN", "KR")]
        mmdata = [p for p in glob.glob(os.path.join(REPO, f"tools/mindmap/unit{u}/*.json")) if not p.endswith("meta.json")]
        mcq = [os.path.exists(os.path.join(REPO, f"Unit{u}/Tests/AP_WH_Unit{u}_MCQ_{l}.md")) for l in ("EN", "KR")]
        mcqdata = glob.glob(os.path.join(REPO, f"tools/mcq/unit{u}/data_*.py"))
        print(f"  mind map: OPML {'EN+KR' if all(mm) else 'missing'}; data {len(mmdata)} file(s) in tools/mindmap/unit{u}/")
        print(f"  MCQ: sheets {'EN+KR' if all(mcq) else 'missing'}; data {len(mcqdata)} file(s) in tools/mcq/unit{u}/")
        if counts["—"]:
            nxt = f"stage 1 (CED draft) for {counts['—']} topic(s)"
        elif counts["CED draft"]:
            nxt = f"stage 2 (textbook integration) for {counts['CED draft']} topic(s)"
        elif counts["other format"]:
            nxt = "notes are in another format (imported); ask the user before rebuilding them"
        elif not all(mm):
            nxt = "stage 3 (mind map)"
        elif not all(mcq):
            nxt = "stage 4 (MCQ)"
        else:
            nxt = "stage 5 (final checks), or done"
        print(f"  next: {nxt}\n")


if __name__ == "__main__":
    main()
