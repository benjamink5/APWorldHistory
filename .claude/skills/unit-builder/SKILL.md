---
name: unit-builder
description: Build a new AP World History unit's study materials end to end, following this repo's five-stage pipeline (CED-based notes and flashcards → textbook integration → mind map → MCQ set → final checks) with the saved agent briefs in tools/briefs/. Also resumes a unit that is partway done and tells you which stage comes next. Use whenever the user wants materials for a unit that doesn't have them yet (Units 6–9 have only CED reference files), wants to continue or redo a stage, or asks "Unit 6 자료 만들어줘", "다음 단원 시작하자", "Unit 7 노트랑 플래시카드", "교재 반영해줘", "마인드맵 만들어줘", "MCQ 만들어줘", "Unit 6 어디까지 했어?". Use it for a single stage too, such as only the mind map or only the MCQ for a unit.
---

# Build a unit

This repo builds each unit through the same pipeline. The details of each stage live in the briefs in `tools/briefs/`, and the conventions live in `CLAUDE.md`. Read both before you start, because this skill only sequences them. It is a long job: one agent per topic for two stages, about four agents for the mind map, and one reviewer. Before each stage, tell the user what it will cost (the number of agents and the number of files they will write). Stop for their review between stages.

## 0. Where is the unit?

```bash
python3 -I .claude/skills/unit-builder/scripts/status.py <N>
```

For each topic, this shows whether the notes and flashcards exist and which source-line stage they are in (CED draft / textbook / other format), plus whether the textbook OCR text (`<topic>.txt`) exists in the shared iCloud folder. It also reports the mind map and MCQ state and names the next stage. Start from that stage. Don't redo finished stages unless the user asks.

Before any writing:
- **Branch.** First run `git status --short`. If there is uncommitted work, ask the user whether to commit it on its current branch before switching. Then follow the CLAUDE.md Git rule: `git switch main && git pull`, then `git switch -c unit<N>-<stage>` (or one `unit<N>-materials` branch if the user prefers). Commit and push after each stage when the user asks.
- **CED reference.** `Unit<N>/Notes/AP_WH_Unit<N>_CED_EN.md` must exist; it is the source of all LO/HD wording. If it is missing, transcribe it first with brief 5A.
- **"Other format" notes** (Units 3–5 were imported): don't overwrite them. Ask the user whether to rebuild the unit in the standard format or leave it.

## Stage 1: CED draft (notes + flashcards, one agent per topic)

1. Show the user the topic list and get confirmation. CLAUDE.md requires this. `python3 -I .claude/skills/unit-builder/scripts/ced_topic.py --list <N>` prints it as a table: topic, title, Korean title, LOs with themes, HD count, and example groups.
2. For each topic, fill `tools/briefs/1_notes_ced_draft.md`:
   - `<X.Y>`, `<N>`, `<REPO_ROOT>`.
   - **Unit lines:** `python3 -I .claude/skills/unit-builder/scripts/ced_topic.py --unit-line <N>` prints the EN and KR lines.
   - **Topic content:** paste the output of `python3 -I .claude/skills/unit-builder/scripts/ced_topic.py <X.Y>`. It is copied verbatim from the CED file. Agents must not invent or paraphrase CED wording, so don't retype it. Keep the template's "KR wording" line, so the KR tables reuse the CED KR translation. Then add a short "Content to cover" list: the key states, people, dates, and comparisons an AP teacher would expect, and every illustrative example. Where the CED lists no examples, the script says so; keep that line so the agent doesn't present its own choices as CED examples.
   - Review topics (the unit's last topic, with no HDs but "Review: Unit N Key Concepts") still get notes, built around comparing or connecting the unit's other topics.
3. Spawn all topic agents in one message, so they run in parallel.
4. When they finish, run `check-materials` (`python3 -I .claude/skills/check-materials/scripts/check.py --unit <N> --render`) and fix what it reports. Then show the user the topic list with card counts and anything flagged "⚠️ Needs verification".

## Stage 2: textbook integration (one agent per topic)

1. **Textbook text.** It lives in `~/Library/Mobile Documents/com~apple~CloudDocs/Family Shared/AP-WorldHistory/Unit<a>-<b>/Textbook/<X.Y>.txt`; two units share each folder (`Unit05-06`). The status script shows which topics have the text and which PDFs belong to the unit. If the text is missing:
   - Ask the user for it. They may only have the scanned PDF.
   - Don't fabricate textbook content, and don't run stage 2 for that topic without the text. The user may choose to skip stage 2 and keep the CED-draft notes; the source line then stays "Textbook not yet incorporated".
2. Fill `tools/briefs/2_notes_textbook_integration.md` for each topic. Add a "Special item" for every ⚠️ left by stage 1 that the textbook might settle, and for any known conflict listed in CLAUDE.md "Known open issues".
3. When an agent finishes, send it the flashcard follow-up message from the same brief through SendMessage. That agent has already read the textbook.
4. **Blocked writes:** if an agent's write is blocked by permissions, don't work around it. Ask the user to approve, then make the edit in the main session (CLAUDE.md).
5. Run `check-materials` again, and update CLAUDE.md "Known open issues" if the textbook contradicts itself or scholarship in a way the next units will meet again.

## Stage 3: mind map (about 4 agents, by region)

1. Decide the regions from the notes, about 12–16 for a unit, then split them among about 4 agents so that every person and event has exactly one owner. Name the boundary cases in each brief.
2. Create `tools/mindmap/unit<N>/meta.json` modeled on `tools/mindmap/unit1/meta.json` (the unit number, EN/KR titles, and the Unit lines).
3. Fill `tools/briefs/3_mindmap_data.md` for each agent, using its own region list and output file `tools/mindmap/unit<N>/<letter>_<regions>.json`.
4. Build:
   ```bash
   python3 -I tools/mindmap/build_opml.py tools/mindmap/unit<N> Unit<N>/Mindmaps
   ```
5. The agents mark people as `(dates unknown)` when the notes give no dates. Fill those from standard references in the main session, and record which ones you filled in `tools/mindmap/unit<N>/applied_fix_dates.py`, like Unit 1. CLAUDE.md lists this under known issues. Then regenerate, and run `check-materials` (OPML well-formedness, EN/KR counts, topic tags).

## Stage 4: MCQ set (main session writes it; one blind reviewer)

Follow `tools/briefs/4_mcq_design_and_review.md` step by step. The main session does this stage itself, because the grid and the answer balance need one mind.

1. **Grid:** topic → stimulus set → question number → type → difficulty, about 30 questions in sets of 2–4. Show it to the user before writing.
2. **Data:** write `tools/mcq/unit<N>/data_*.py` in the schema of `tools/mcq/unit1/data_a.py`. Every text is an (EN, KR) pair, and no explanation refers to an option letter. Check every fact the answer depends on against the notes (`grep`), and mark explanations that go beyond the notes with 📌.
3. **meta.py:** copy `tools/mcq/unit1/meta.py`. Fill `TOPICS` from the CED titles (KR from the CED KR file), and set `TARGET` with:
   ```bash
   python3 -I .claude/skills/unit-builder/scripts/mcq_target.py --sets 3,2,2,3,... --seed 1
   ```
   This applies the brief's rules: balanced letters, no run over 2, no repeated 4-letter window, no ABAB, no repeat within a set. `--check <TARGET>` verifies an existing sequence.
4. Generate with `python3 -I tools/mcq/gen.py tools/mcq/unit<N> Unit<N>/Tests` and read its report. Keep "correct option is the longest" near a quarter of the questions.
5. **Blind review:** send the brief's reviewer prompt to a fresh agent that never sees the key. Any disagreement, or any "two answers are defensible" flag, means that question gets rewritten. Then do the brief's final cross-check of the generated files.

## Stage 5: finish

1. `python3 -I .claude/skills/check-materials/scripts/check.py --unit <N> --render` must report 0 errors.
2. Update `CLAUDE.md` ("Units 1 and 2 are complete", the Units 6–9 line, known open issues, and Korean spelling variants you settled) and the README contents table.
3. Commit and push on the feature branch when the user asks. If they want a PR description, write it to `Output/PR_<branch>.md`.

## Keeping it consistent

- **Korean terms:** reuse the spellings already used in earlier units' KR notes and in the unit's CED KR file. Where those differ, follow CLAUDE.md "Known open issues".
- **Use the same brief text every time.** If a brief has a gap, fix the template in `tools/briefs/` and tell the user, rather than improvising instructions in one agent prompt. The next unit then benefits too.
- **Report progress per stage:** what was produced (files, card counts, question count), what check-materials said, and what needs the user's decision.
