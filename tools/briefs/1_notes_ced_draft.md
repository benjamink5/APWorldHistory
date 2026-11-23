# Brief template: CED-based notes + flashcards for one topic (stage 1, before the textbook)

Used for Unit 1 (one agent per topic, all topics run in parallel). Fill every `<…>` and paste the
whole brief into the agent prompt. Before sending, write the topic's CED Learning Objectives and
Historical Developments into the last section yourself: the agent must not invent CED wording.

---

You are writing AP World History: Modern study materials for **Topic <X.Y>** in the repo `<REPO_ROOT>`. Create exactly 4 files (create the folders if missing):
- `Unit<N>/Notes/AP_WH_<X.Y>_Notes_EN.md`, `Unit<N>/Notes/AP_WH_<X.Y>_Notes_KR.md`
- `Unit<N>/Flashcards/AP_WH_<X.Y>_Flashcards_EN.md`, `Unit<N>/Flashcards/AP_WH_<X.Y>_Flashcards_KR.md`

Do not modify or delete any other file. Do not git commit.

## Format templates — read these first
Read `Unit2/Notes/AP_WH_2.1_Notes_EN.md`, `Unit2/Notes/AP_WH_2.1_Notes_KR.md`, `Unit2/Flashcards/AP_WH_2.1_Flashcards_EN.md`, `Unit2/Flashcards/AP_WH_2.1_Flashcards_KR.md` (or any finished topic). Match their structure, heading style, table style, Korean writing style (plain declarative "~했다/~이다", short clear sentences), Mermaid usage, and flashcard markup exactly. Differences from the template:
1. Source line exactly: EN `> Source: Based on the College Board CED · Textbook not yet incorporated` / KR `> 출처: CED 기준 · 교재 반영 전`. Never write "the textbook says". Use `> ⚠️ Needs verification: ...` / `> ⚠️ 확인 필요: ...` only for facts or dates that are genuinely disputed or uncertain.
2. Unit line: EN `**<Unit line EN>**` / KR `**<Unit line KR>**`.
3. An opening quote in the Big Picture is optional. Include one only if it is a well-known, accurately attributed primary source.

## Notes structure (both languages: identical sections, rows, and diagrams)
Title (`# AP World History: Modern — Topic <X.Y> <title>` / `# AP 세계사: 모던 — 토픽 <X.Y> <Korean title> (<English title>)`) → Focus Question → source line → Unit line → `---` → Learning Objective table → Historical Developments (CED) table with a "Covered in / 다루는 곳" § column → `---` → Big Picture summary (paragraph + Mermaid flowchart) → §1…§n sections → Timeline section (Mermaid `timeline` for events AND `gantt` for periods/dynasties) → at least one map-style Mermaid `flowchart` for geography or movement → comparison table(s) (optionally a Mermaid `mindmap`) → Key Terms table (Theme | Term | Definition).
Every LO, every HD, and every illustrative example must be covered somewhere and mapped in the HD table.
KR: key terms show the English in parentheses, e.g. 징세 청부 (Tax farming), on first mention and in all tables.

Mermaid safety rules: put node labels in double quotes and use `<br/>` for line breaks. In `timeline`, no colons inside event text. In `gantt`, use `dateFormat YYYY` with 4-digit years ≥1000 only; for earlier starts, begin the bar at the earliest allowed year and put the real start year in the label. In `mindmap`, no parentheses or brackets in node text except the root `((...))`. For pie charts use `pie showData`.

## Flashcard structure (both languages identical: same cards, same order)
Title `... · Flashcards` / `... · 플래시카드`, then the source line, then a Mermaid `pie showData` titled `Card Breakdown (N cards)` / `카드 구성 (N장)` with 5 slices: EN `Key Terms`, `People`, `Dates & Events`, `Cause & Effect`, `Comparison & AP Writing`; KR `핵심 용어`, `인물`, `연도·사건`, `원인·결과`, `비교·AP 서술형`. Then sections `## 1.` … `## 5.` in that order. Total 20–40 cards (aim for about 30–36). Each card exactly:
```
- [ ] **Question**
<details><summary>▶ Answer</summary>...</details>
```
(KR uses `▶ 정답`.) The Comparison & AP Writing section has comparison cards, at least two SAQ-style cards, and one LEQ-thesis card, written Claim → Evidence → Reasoning (KR 주장 → 근거 → 설명) on separate lines ending in `<br/>`. The pie counts must equal the real number of cards in each section.

## Topic <X.Y> content (College Board CED)
<Paste the output of `python3 -I .claude/skills/unit-builder/scripts/ced_topic.py <X.Y>` here. It has this shape:>
Title: **<X.Y> <CED title>** (KR: <Korean title>)
Suggested skill: <code> <skill> — <description>
Learning Objectives and Historical Developments (use this wording):
- **LO A (<theme>):** <...>
  - <KC code>: <HD text>
  - Illustrative examples — *<Category>:* <item>; <item>   (or "none in the CED for this LO")
KR wording: for the KR LO and HD tables, copy the Korean translations from `Unit<N>/Notes/AP_WH_Unit<N>_CED_KR.md` (Topic <X.Y>) instead of translating again, and reuse its Korean terms.
<Content to cover: key states, people, dates, comparisons, map ideas. Keep it to standard AP-level scholarship.>

## Final check (before reporting)
Count the cards in each section of both flashcard files and confirm the counts match the pie and each other. Confirm the EN and KR notes have the same headings and the same table row counts, and that every HD is mapped. Report the 4 file paths, the card total with per-category counts, and a short list of anything that needs verification.
