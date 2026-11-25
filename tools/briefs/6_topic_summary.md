# Brief 6 — Topic summary notes (EN + KR)

A short, plain-language study summary of one topic, written from that topic's finished notes. It is for a student who finds the full notes hard to follow. Run one agent per topic in parallel. Fill in `<N>` (unit) and `<X.Y>` (topic) below.

---

You are writing a plain-language summary of AP World History: Modern **Topic <X.Y>** for a high-school student who finds the full notes hard to follow. Work in `/Users/okjoonkim/JKProjects/APWorldHistory`. Read `CLAUDE.md` first; its conventions (EN/KR parity, Korean term style, ⚠️ wording, Mermaid safety rules) apply.

**Read:** `Unit<N>/Notes/AP_WH_<X.Y>_Notes_EN.md` and `Unit<N>/Notes/AP_WH_<X.Y>_Notes_KR.md` in full. Use the KR notes for Korean terms and spellings so the summary matches them.

**Write exactly two files:**
- `Unit<N>/Summaries/AP_WH_<X.Y>_Summary_EN.md`
- `Unit<N>/Summaries/AP_WH_<X.Y>_Summary_KR.md`

Do not edit any other file.

## Content rules

- **Only facts that are in the topic's notes.** No new facts, dates, or numbers from memory. If you simplify, keep it true. Where the notes say "check against the printed textbook", keep that caveat or leave the fact out.
- **Pick what matters for the exam:** the Learning Objectives and Historical Developments in the notes' LO/HD tables come first. Every LO must be reflected somewhere in the summary. Leave out side details.
- **Plain language.** Short sentences, everyday words, one idea per bullet. Explain any AP term the first time it appears. The EN file should be readable by an English learner.
- **⚠️ notes:** if the summary uses a fact that carries a ⚠️ textbook-vs-scholarship note in the notes, carry the note over in the Notes wording (`> ⚠️ The textbook … Many accounts say … Check how your teacher presents this.` / `> ⚠️ 교재는 … 많은 설명에서는 … 선생님이 어떻게 가르치는지 확인이 필요하다.`). Don't add ⚠️ notes that aren't in the notes.
- **Length:** about 80–130 lines per file.

## Layout (both files, same order; EN heading / KR heading)

```
# AP World History: Modern — Topic <X.Y> Summary: <short title> (c. YYYY–YYYY)
# AP 세계사: 모던 — 토픽 <X.Y> 요약: <짧은 제목> (<English title>)

> Source: Summary of AP_WH_<X.Y>_Notes_EN.md (College Board CED · textbook incorporated, Topic <X.Y> reading)
> 출처: AP_WH_<X.Y>_Notes_KR.md 요약 (College Board CED 기준 · 교재 반영, 교재 Topic <X.Y>)

**Unit <N>: <unit title>**   (copy the Unit line from the notes)

---

## In One Sentence / ## 한 문장 요약
One sentence that answers the notes' Focus Question.

## The Big Picture / ## 큰 그림
One paragraph of 3–5 sentences, then one Mermaid `flowchart LR` of 4–7 nodes showing the main cause → result chain.

## Key Points / ## 핵심 정리
4–6 numbered `### 1. …` subsections (one per main idea, usually one per region, state, or LO). Each has 3–5 bullets. Bold the one or two words per bullet that the student must remember.

## Must-Know Terms & People / ## 꼭 알아야 할 용어·인물
Table `| Term | What it is | Why it matters |` / `| 용어 | 무엇인가 | 왜 중요한가 |`, 8–12 rows.

## Key Dates / ## 주요 연도
Table `| Year | Event |` / `| 연도 | 사건 |`, 5–8 rows, in chronological order.

## How the Exam Asks About It / ## 시험에서는 이렇게 묻는다
Exactly four bullets, with these bold labels:
- **Legitimacy & consolidation / 정당화와 공고화:** how rulers in this topic justified and kept power (skip to the closest theme if the topic has no states).
- **Continuity, innovation, diversity / 연속성·혁신·다양성:** one example of each.
- **Likely comparison / 자주 나오는 비교:** one pairing and the key similarity and difference.
- **Common trap / 자주 하는 실수:** one confusion students often make, and the fix.

## Check Yourself / ## 스스로 확인하기
Exactly 3 short-answer questions, numbered, each followed by
`<details><summary>▶ Answer</summary>…</details>` (KR: `▶ 정답`). Answers are 1–3 sentences.
```

## Format rules

- **EN/KR parity is a hard rule:** same headings in the same order, same table row counts, same single Mermaid block with the same nodes and edges, same ⚠️ notes, same questions in the same order. Write the EN file first, then translate it to KR.
- **Korean:** plain declarative style (`~했다/~이다`). Key terms and people carry the English in parentheses on first use and in every table row: `과거제 (Civil service examinations)`, `만사 무사 (Mansa Musa)`. Use the spellings in the KR notes.
- **Mermaid:** every node label in double quotes, `<br/>` for line breaks, no unquoted parentheses.
- After writing, grep the KR file for `�`, then run
  `python3 -I .claude/skills/check-materials/scripts/check.py Unit<N>/Summaries/AP_WH_<X.Y>_Summary_EN.md Unit<N>/Summaries/AP_WH_<X.Y>_Summary_KR.md`
  and fix anything it reports.

**Report back:** the two file paths, their line counts, the check result, which ⚠️ notes you carried over, and any fact you left out because the notes flagged it as uncertain.
