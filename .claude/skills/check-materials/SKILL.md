---
name: check-materials
description: Run every consistency check on the AP World History study materials in one go. The checks are EN/KR twin parity (headings, table rows, Mermaid blocks, ⚠️), broken Korean characters, flashcard counts against the pie chart, OPML well-formedness and topic tags, the CLAUDE.md Mermaid safety rules, LO letters and KC codes against the unit's CED file, and optionally drawing every diagram. Use after editing or generating any notes, flashcards, mind maps, or tests in this repo, before committing, and whenever the user asks to check, verify, validate, or "검사/점검/확인" the materials, e.g. "Unit 2 검사해줘", "커밋 전에 확인해줘", "EN/KR 짝 맞는지 봐줘", "플래시카드 숫자 맞아?". Prefer this over writing a one-off parity or count script.
---

# Check the study materials

One script runs every check listed under "Checks to run after editing" in `CLAUDE.md`, plus a CED cross-check. Use it instead of writing throwaway counting scripts.

```bash
python3 -I .claude/skills/check-materials/scripts/check.py                  # all units + Course/
python3 -I .claude/skills/check-materials/scripts/check.py --unit 2         # one or more units
python3 -I .claude/skills/check-materials/scripts/check.py Unit1/Notes/AP_WH_1.3_Notes_EN.md   # files or folders (twins are added automatically)
python3 -I .claude/skills/check-materials/scripts/check.py --unit 1 --render   # also draw every Mermaid diagram
```

Add `--quiet` to print only the checks that found something, and `--strict` to list the Units 3–5 differences too (see below). The script exits with 1 if there is any error, so you can chain it before a commit.

## What it checks

| Check | Error when |
|---|---|
| `pairs` | an `_EN.md` and its `_KR.md` twin differ in headings, table rows, Mermaid blocks, or ⚠️ count, or a twin is missing |
| `chars` | a file contains `�` (U+FFFD). Korean writes have produced these before |
| `cards` | a flashcard section's card count differs from its pie slice, the "(N cards)" title differs from the total, `<details>` tags are unbalanced, or EN and KR card counts differ |
| `opml` | the XML is not well-formed, the file is not OPML 2.0, EN and KR outline counts differ, or a leaf lacks a `[x.y]` tag (the "Legend:/범례:" node is exempt) |
| `mermaid` | a CLAUDE.md safety rule is broken: an unquoted node or edge label contains brackets, a gantt has no `dateFormat YYYY` or uses a year below 1000, a mindmap node has brackets, or a flashcard pie is not `pie showData` |
| `ced` | a topic note's LO letters or its HD-table KC codes (codes and order) differ from `Unit<N>/Notes/AP_WH_Unit<N>_CED_EN.md` |
| `render` (`--render`) | a Mermaid block fails to parse when drawn with the `md-to-pdf` skill. Drawing takes about 1 s per file, so use it on the files you touched or before a commit, not on every small edit |

The static `mermaid` check is stricter than the renderer on purpose. Mermaid sometimes draws a gantt with a 3-digit year or a mindmap node with parentheses, but these break in other renderers, so CLAUDE.md forbids them anyway. An unquoted label with parentheses breaks in Mermaid itself; the static check and `--render` both catch it.

## Units 3–5

These units were imported from elsewhere in a different format: no LO/HD tables, other flashcard and mind-map layouts, and one KR test file without the `_KR` suffix. CLAUDE.md says not to treat them as templates. The script therefore does not list their format-convention differences. It prints one summary line instead, such as "121 convention difference(s) not listed (cards 76, ced 22, …)". Real damage is still reported as an error in every unit: broken characters, malformed XML, and diagrams that fail to render. Use `--strict` when someone is converting a Units 3–5 file to the standard format and wants to see what is left.

## Reading the result and fixing

- Report the summary line and every error to the user. For each error, give the file and the line, and say what would fix it. Fix the error only if the user asked for fixes or the error came from your own edit in this session.
- **pairs:** open both twins and find the extra or missing heading, row, or block. Usually one language got an edit the other didn't. Fix the twin rather than deleting content.
- **cards:** recount after editing. The pie slices and the "(N cards)" title must follow the real card count, not the other way round.
- **ced:** the CED file is the authority (CLAUDE.md, "Sources"). Fix the notes table unless the CED file itself is wrong, in which case check the PDF page image before changing either.
- **Generated files** (the Unit 1 mind map and MCQ files): fix the data in `tools/mindmap/` or `tools/mcq/` and regenerate; don't hand-edit the output (CLAUDE.md).
- Run the checker again after fixing, and include the clean summary line in your report.

## Extending

When a new rule enters CLAUDE.md, add a check function to `scripts/check.py`, register it in `main()`, and add a row to the table above. The script was verified by copying Unit 1 files into a scratch folder under `Output/`, injecting one error of each kind (a dropped KR table row, a `�`, an off-by-one pie slice, a broken OPML tag, unquoted Mermaid labels, a 3-digit gantt year, a mindmap bracket, and a wrong KC code), and confirming that each one was reported. Repeat that test after changing a check.
