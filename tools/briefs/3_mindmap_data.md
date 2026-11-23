# Brief template: mind map data (one agent per group of regions)

Used for the Unit 1 mind map: four agents, each owning a fixed set of regions, so that every person
and event has exactly one owner. The agents write JSON only. The main session then runs
`tools/mindmap/build_opml.py`. Fill every `<…>`; give each agent its own region list and output
file name.

---

Goal: produce structured data that the main session will turn into an OPML mind map (`Unit<N>/Mindmaps/AP_WH_Unit<N>_MindMap_EN.opml` / `_KR.opml`). The user asked for a Unit <N> mind map organized by state → people / events / institutions, in EN and KR, with source-topic tags. You do NOT write OPML. You write ONE JSON file: `<OUT_JSON>`.

## Sources (read-only)
- **Notes:** `AP_WH_<N>.1_Notes_EN.md` … `AP_WH_<N>.<last>_Notes_EN.md` and their `_KR.md` twins in `<REPO_ROOT>/Unit<N>/Notes/`. Use ONLY facts in these notes, and use the KR notes' Korean terms and name spellings.
- **Cross-topic coverage:** your regions may appear in several topics (the comparison topic covers everything), so grep all of them.
- **Style reference:** the first ~60 lines of `Unit2/Mindmaps/AP_WH_Unit2_MindMap_EN.opml` / `_KR.opml`.

Do not modify any file in the repo.

## JSON format
A JSON array of region objects, matching the schema in the docstring of `tools/mindmap/build_opml.py`:
`order`, `name_en`, `name_kr`, `people[]`, `events[]`, `institutions[]`. People and events also need a numeric `sort`: birth year or reign start for people, start year for events. Use negative numbers for B.C.E., 1235 for "c. 1235", and 1200 for "13th century". Every item has both `en` and `kr`, saying the same thing with the same years and the same topic tags. Text is plain: no newlines, no Markdown, and no XML escaping.

## Item formats
- **People:**
  - EN `Name (r. 1312–1337) — one-line key achievement [<N>.5]`. Lifespans are `(1225–1274)`; when both apply, write `(b. 1162; r. 1206–1227)`.
  - KR `한국어 이름 (English Name) (재위 1312–1337) — 핵심 업적 한 줄 [<N>.5]`. When both apply, write `(1162년 출생, 재위 1206–1227)`.
  - Only real individuals go under People, not dynasties or groups.
- **Events:** `1235 — Event [<N>.5]` / `1235 — 사건 [<N>.5]`. Ranges `1337–1453 — …`. Centuries `13th century — …` / `13세기 — …`.
- **Institutions:** EN `Term — one-line description` / KR `한국어 용어 (English term) — 한 줄 설명`, each ending in its topic tag.
- **Topic tags:** every item ends with its tag, e.g. `[<N>.3]`, or `[<N>.2, <N>.7]` when several topics cover it.
- **Textbook vs. most sources:** where the notes have a ⚠️ conflict, give the textbook version and add before the tag `(⚠️ textbook; most sources say …)` / `(⚠️ 교재 기준, 많은 자료는 …)`.
- **Missing dates:** if the notes give no dates for a person, write `(dates unknown)` / `(생몰 미상)`. The main session fills these from standard references and records them; Unit 1 needed about 60.
- **Size:** about 2–8 people, 4–12 events, and 3–8 institutions per region. Never pad with facts from outside the notes.

## Your regions
<order>. `<name_en>` / `<name_kr>` — <topics where it appears; notes on boundaries with other agents' regions>

## Before reporting
Run a `python3 -I` check:
- the file loads with `json.load`
- every item has a non-empty `en` and `kr`
- every item ends with a tag, and the EN and KR tags match
- every KR person entry has the English name in parentheses
- people and events are sorted by `sort`

Report the JSON path, the item counts per region, the ⚠️ conflicts you marked, and any items that may overlap another region.
