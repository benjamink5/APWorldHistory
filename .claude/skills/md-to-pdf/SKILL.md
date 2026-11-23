---
name: md-to-pdf
description: Convert this repo's Markdown study files (notes, flashcards, MCQ tests, DBQs) to print-ready PDFs with Mermaid diagrams drawn, flashcard answers expanded, and questions kept on one page. Use whenever the user asks to make, print, export, or render a PDF of any .md file here — e.g. "1.2 노트 PDF로 만들어줘", "Unit 3 플래시카드 출력", "시험지 인쇄용으로", "pdf로 뽑아줘", "정답 없이 문제만 PDF로".
---

# Markdown → PDF

One script does everything: `scripts/md2pdf.py`. It runs pandoc (Markdown → HTML), draws the Mermaid diagrams with a local `mermaid.min.js`, and prints the page through macOS WebKit (`scripts/html2pdf.swift`, compiled once into `~/Library/Caches/md-to-pdf/`).

## Where output goes

Every generated file goes in `Output/` at the repo root, which is gitignored. The PDF path mirrors the source path: `Unit1/Notes/AP_WH_1.2_Notes_KR.md` → `Output/Unit1/Notes/AP_WH_1.2_Notes_KR.pdf`. Don't write PDFs next to the Markdown. Use `-o` only when the user names a different place.

## Run

From the repo root:

```bash
python3 -I .claude/skills/md-to-pdf/scripts/md2pdf.py Unit1/Notes/AP_WH_1.2_Notes_KR.md
python3 -I .claude/skills/md-to-pdf/scripts/md2pdf.py Unit3/Flashcards/*.md        # many files
python3 -I .claude/skills/md-to-pdf/scripts/md2pdf.py --no-answers Unit1/Flashcards/AP_WH_1.2_Flashcards_KR.md
```

| Option | Use when |
|---|---|
| `--no-answers` | The user wants questions only. Flashcard `<details>` answers stay closed and do not print. (Answers are shown by default.) |
| `--a4` | The user asks for A4. The default is US Letter. |
| `--keep-h3` / `--no-keep-h3` | Override whether each `### …` block is kept on one page. This is on automatically for test files (names containing MCQ, Test, DBQ, Practice, Questions, AnswerKey, Explanations). |
| `-o PATH` | A `.pdf` path for one input, or a folder for several. |
| `--html` | Also save the intermediate HTML next to the PDF, for debugging the layout. |

Each file takes a few seconds. For a whole unit, pass all the files in one call.

## Read the report

The script prints one line per file: `✓ <pdf> (N pages)`. If a Mermaid block does not parse, it adds `mermaid #k [first line]: error`. That diagram is printed as red-bordered source text so the PDF is still usable. These are real syntax errors in the Markdown. They were never visible before because the files had not been rendered. Tell the user which file and diagram failed. Fix the source only if they ask, and keep the EN/KR twins in sync.

Check the result by looking at it, not only by trusting the page count. Render a few pages to PNG (for example, with a throwaway Swift script using `PDFPage.thumbnail`) and view them, especially pages with diagrams or wide tables.

## Rendering choices (so you don't "fix" them)

- **Mermaid `timeline` prints as a table** (Year | Events). With 20+ events, a timeline drawing scaled to the page width becomes unreadable. Other diagram types (flowchart, gantt, pie, mindmap) are drawn.
- `(A)`-style answer options stay literal. The pandoc `fancy_lists` extension is turned off.
- The `neutral` Mermaid theme is grayscale on purpose, so pages print well on a black-and-white printer.
- A question paragraph (`**12.** …`) and the option list that follows it are never split across pages.

## If something is missing

- **pandoc** not found: `brew install pandoc`.
- **swiftc** not found: `xcode-select --install`.
- **mermaid.min.js**: the network is blocked, so it is never downloaded. The script looks in `scripts/vendor/`, `$MERMAID_JS`, the keynote-mermaid plugin, the npx cache, and some installed apps. If it finds none, diagrams are printed as text and the script says so.
