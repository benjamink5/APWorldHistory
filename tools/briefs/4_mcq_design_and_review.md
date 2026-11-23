# MCQ set: design checklist and blind-review brief

The Unit 1 set was written by the main session directly as paired EN/KR data
(`tools/mcq/unit1/data_*.py`) and generated with `tools/mcq/gen.py`. These are the steps that
made it reliable. Repeat them for a new unit.

## 1. Design before writing
- **Plan a grid first:** topic → stimulus set → question number → type → difficulty. Spread questions evenly across topics. Use sets of 2–4 questions on one stimulus.
- **Mix of question types:** source analysis, causation, comparison, continuity & change, contextualization.
- **Difficulty:** easy : medium : hard = 3 : 5 : 2.
- **Mix of stimulus types:**
  - Primary sources: short public-domain excerpts only, with author, date, work, translator, and translation year. Use only texts you can quote reliably. For medieval texts, an "English translation adapted for this practice set from the original" is acceptable.
  - Secondary passages, maps, charts, and images: when written for the set, label them `Practice passage written for this set (not a quotation from a published historian)` or `Map/Image description written for this practice set`.
  - Charts built from estimates: say so and round the numbers.
- **Facts:** check every fact the answer depends on against the notes (`grep`). Mark explanations that use content not in the notes with 📌.

## 2. Write the data
Use the schema in `tools/mcq/unit1/data_a.py`. Every question has:
- stem, 4 options, answer letter
- why it is correct
- a one-line reason for each wrong option
- skill, type, difficulty, review section, and an optional 📌 note

Every text field is an (EN, KR) pair. Explanations must never mention option letters, because `gen.py` reorders options to the answer sequence in `meta.py`.

Good distractors are plausible and wrong for a historical reason:
- the same era in another region
- the wrong period (for example, the Pax Mongolica for an earlier transfer)
- cause and effect reversed
- true but not what the stem asks (for example, a similarity when the stem asks for a difference)

Avoid distractors that fail on absurdity alone. Never use "all/none of the above".

## 3. Generate and inspect the patterns
Run `python3 -I tools/mcq/gen.py tools/mcq/unit<N> .` and read its printed report:
- answer distribution, longest same-letter run
- difficulty, type, topic, and stimulus counts
- the number of questions where the correct option is the longest

Keep the last number near a quarter. Unit 1 went from 27/30 to 10/30 by shortening correct options and adding specific detail to distractors.

Choose `TARGET` in `meta.py` with a seeded random search under these rules:
- balanced counts
- no run longer than 2
- no repeated 4-letter window
- no xyxy alternation
- no repeated letter within one stimulus set

## 4. Blind review (independent agent, no answer key)
Send this to a fresh general-purpose agent:

> You are an independent reviewer for an AP World History: Modern practice test (Unit <N>). I want an unanchored check, so I am NOT giving you my answer key.
> Read ONLY `<REPO_ROOT>/AP_WH_Unit<N>_MCQ_EN.md`. Do NOT open any file whose name contains "Answers", and do not open the KR file. Do not modify any file.
> 1. Answer every question yourself, as a strong AP student or teacher would. For each, give your answer letter and your confidence (high/medium/low).
> 2. Flag every question where a second option is defensible, the stem is unclear, or the answer depends on a contested fact.
> 3. Check the facts in the stimuli and options: source attributions (author, date, translator, translation year), quotation wording, dates, and historical claims.
> 4. Note giveaway patterns: options that are wrong for non-historical reasons, answer-letter sequences, length cues.
> Report a compact table (Q#, answer, confidence, issue), then a short list of factual concerns, in under ~600 words.

Compare the reviewer's answers with the key. Any disagreement, or any "two answers are defensible" flag, means that question must be rewritten. In Unit 1 the reviewer matched all 30 answers but caught:
- a repeating answer sequence
- weak distractors
- a scope problem in Q3 (Goryeo was under military rule from 1170 to 1270)
- a translation-year error (Maudslay, 1908–1916)

## 5. Final cross-check of the output files
Parse the generated files and confirm:
- the quick key, the detailed answers, and the distribution table agree
- each "correct choice" text equals the option at that letter in the question sheet
- every question explains exactly the three other letters
- the answer sheet has one line per question
- the EN and KR keys are identical
