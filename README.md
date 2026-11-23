# AP World History: Modern — Study Materials

Bilingual (English / Korean) study materials for **AP World History: Modern**, written to the College Board Course and Exam Description (CED) and revised against the class textbook. Every English file has a Korean twin (`_EN` / `_KR`).

## Contents

| Unit | Period | Topics | Status |
|---|---|---|---|
| [Unit 1](Unit1/) | The Global Tapestry, c. 1200–1450 | 1.1–1.7 | Complete, textbook incorporated |
| [Unit 2](Unit2/) | Networks of Exchange, c. 1200–1450 | 2.1–2.7 | Complete, textbook incorporated |
| [Unit 3](Unit3/) | Land-Based Empires, c. 1450–1750 | 3.1–3.4 | Imported; different format |
| [Unit 4](Unit4/) | Transoceanic Interconnections, c. 1450–1750 | 4.1–4.8 | Imported; different format, no 4.1 EN notes |
| [Unit 5](Unit5/) | Revolutions, c. 1750–1900 | 5.1–5.10 | Imported; different format |

Units 3–5 were made separately and copied in, so their layout and test formats differ from Units 1–2.

## Layout

```
Unit<N>/
├── Notes/        AP_WH_<topic>_Notes_{EN,KR}.md         topic notes with tables and Mermaid diagrams
├── Flashcards/   AP_WH_<topic>_Flashcards_{EN,KR}.md    20–40 cards per topic, answers in <details>
├── Mindmaps/     AP_WH_Unit<N>_MindMap_{EN,KR}.opml     region → people / events / institutions
└── Tests/        AP_WH_Unit<N>_MCQ_…                    stimulus-based MCQs and answer keys (Unit 3 also has DBQs)
tools/            generators and agent briefs used to build the materials
Output/           generated PDFs and other exports (gitignored)
```

## Using the files

- **Notes, flashcards, and tests** are Markdown. GitHub draws the Mermaid diagrams. Flashcard answers are folded under `▶ Answer` / `▶ 정답`; click to reveal them.
- **Mind maps** are OPML 2.0 and open in MindNode, XMind, OmniOutliner, and most outliners.
- **PDFs**: run `python3 -I .claude/skills/md-to-pdf/scripts/md2pdf.py <file.md> …`. The PDF goes to `Output/`, at the same path as the source file. Add `--no-answers` to print flashcards as questions only, or `--a4` for A4 paper. This needs macOS, `pandoc`, and the Xcode command-line tools. The script lists its other requirements and options.

## Regenerating

The Unit 1 mind map and MCQ set are generated from data in `tools/`:

```bash
python3 -I tools/mindmap/build_opml.py tools/mindmap/unit1 Unit1/Mindmaps
python3 -I tools/mcq/gen.py tools/mcq/unit1 Unit1/Tests
```

To change those files, edit the data and regenerate. Everything else is edited directly. `CLAUDE.md` describes the conventions, sources, and the build pipeline in detail.

## Sources and caveats

- CED wording was written from memory, because the CED PDF could not be downloaded. Check it against the official CED where exact wording matters.
- Textbook content comes from OCR'd text, so a few facts are marked "check against the printed textbook".
- Where the textbook disagrees with standard scholarship, the files give the textbook version first and flag the other view with ⚠️.
