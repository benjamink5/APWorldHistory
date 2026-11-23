"""Generate AP_WH_Unit<N>_MCQ_{EN,KR}.md and AP_WH_Unit<N>_MCQ_Answers_{EN,KR}.md.

Usage (from the repo root):
    python3 -I tools/mcq/gen.py tools/mcq/unit1 Unit1/Tests

<unit_dir> holds meta.py (UNIT, TOPICS, TARGET) and data_*.py modules, each defining one list
named SETS_* of stimulus sets (see unit1/data_a.py for the schema; every text field is an
(EN, KR) pair). Modules are loaded in file-name order. Prints counts and pattern checks at the end.
"""
import collections
import glob
import importlib.util
import itertools
import os
import sys

UNIT_DIR, OUT = sys.argv[1], sys.argv[2]


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.splitext(os.path.basename(path))[0], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


META = load(os.path.join(UNIT_DIR, "meta.py"))
N, TOPICS, TARGET = META.UNIT, META.TOPICS, META.TARGET
SETS = []
for path in sorted(glob.glob(os.path.join(UNIT_DIR, "data_*.py"))):
    mod = load(path)
    for name in sorted(v for v in vars(mod) if v.startswith("SETS")):
        SETS += getattr(mod, name)
QS = [q for s in SETS for q in s["qs"]]
LET = "ABCD"

# ---------------------------------------------------------------- answer positions
# The correct option is moved to its TARGET slot (see meta.py); distractors keep their order.
assert len(TARGET) == len(QS), (len(TARGET), len(QS))
for q, t in zip(QS, TARGET):
    a = LET.index(q["ans"])
    others = [j for j in range(4) if j != a]
    order = others[:LET.index(t)] + [a] + others[LET.index(t):]   # order[new_pos] = old_index
    q["opts"] = [q["opts"][j] for j in order]
    q["wrong"] = {LET[new]: q["wrong"][LET[old]] for new, old in enumerate(order) if old != a}
    q["ans"] = t

# ---------------------------------------------------------------- checks
assert [s["n"] for s in SETS] == list(range(1, len(SETS) + 1))
assert [q["n"] for q in QS] == list(range(1, len(QS) + 1)), [q["n"] for q in QS]
for s in SETS:
    assert 2 <= len(s["qs"]) <= 4, s["n"]
for q in QS:
    assert len(q["opts"]) == 4 and q["ans"] in LET
    assert sorted(q["wrong"]) == sorted(set(LET) - {q["ans"]}), q["n"]
    for o in q["opts"]:
        low = o[0].lower()
        assert "all of the above" not in low and "none of the above" not in low

SKILL = {
    "S1": ("Skill 1: Developments & Processes", "기술 1: 역사적 전개와 과정"),
    "S2": ("Skill 2: Sourcing & Situation", "기술 2: 출처와 상황 분석"),
    "S3": ("Skill 3: Claims & Evidence in Sources", "기술 3: 자료 속 주장과 근거"),
    "S4": ("Skill 4: Contextualization", "기술 4: 맥락화"),
    "S5C": ("Skill 5: Making Connections (Causation)", "기술 5: 연결하기 (인과관계)"),
    "S5P": ("Skill 5: Making Connections (Comparison)", "기술 5: 연결하기 (비교)"),
    "S5T": ("Skill 5: Making Connections (Continuity & Change)", "기술 5: 연결하기 (지속과 변화)"),
}
QTYPE = {
    "src": ("Source analysis", "자료 해석"),
    "cause": ("Causation", "인과관계"),
    "comp": ("Comparison", "비교"),
    "ccot": ("Continuity & change", "지속과 변화"),
    "ctx": ("Contextualization", "배경(맥락)"),
}
DIFF = {"E": ("Easy", "쉬움"), "M": ("Medium", "보통"), "H": ("Hard", "어려움")}
STYPE = {
    "primary": ("Primary source", "1차 사료"),
    "secondary": ("Secondary source", "2차 사료"),
    "map": ("Map", "지도"),
    "chart": ("Chart", "표"),
    "image": ("Image", "그림"),
}
I = {"en": 0, "kr": 1}


def compress(nums):
    nums = sorted(nums)
    out, start, prev = [], nums[0], nums[0]
    for x in nums[1:] + [None]:
        if x is not None and x == prev + 1:
            prev = x
            continue
        out.append(f"{start}–{prev}" if prev != start else f"{start}")
        if x is not None:
            start = prev = x
    return ", ".join(out)


def quote(block):
    return "\n".join(l if l.startswith(">") else ("> " + l if l else ">") for l in block.splitlines())


def qrange(s):
    ns = [q["n"] for q in s["qs"]]
    return f"{ns[0]}–{ns[-1]}"


def header(lang):
    i = I[lang]
    if lang == "en":
        lines = [f"# AP World History: Modern — Unit {N} Multiple-Choice Practice Set", "",
                 f"> Source: Based on the existing Unit {N} notes and flashcards (textbook incorporated) and the CED learning objectives", "",
                 f"**Time limit: 30 minutes** ({len(QS)} questions · about 1 minute per question, as on the real exam)  ",
                 f"**Directions:** Read each source and choose the **one** best answer, A–D. Answers and explanations are in `AP_WH_Unit{N}_MCQ_Answers_EN.md`.", "",
                 "## Topic Breakdown", "", "| Topic | Title | Stimulus sets | Questions | Count |", "|---|---|---|---|---|"]
    else:
        lines = [f"# AP 세계사: 모던 — Unit {N} 객관식(MCQ) 연습 세트", "",
                 f"> 출처: 기존 Unit {N} 노트·플래시카드(교재 반영)와 CED 학습 목표 기준 · 문제와 보기는 영어 원문, 아래에 한국어 번역", "",
                 f"**제한 시간: 30분** ({len(QS)}문제 · 실제 시험 기준 1문제당 약 1분)  ",
                 f"**방법:** 자료를 읽고 가장 알맞은 답을 A–D 중 **하나** 고르세요. 정답과 해설은 `AP_WH_Unit{N}_MCQ_Answers_KR.md`에 있습니다.", "",
                 "## 토픽 구성표", "", "| 토픽 | 제목 | 자료 세트 | 문제 번호 | 문제 수 |", "|---|---|---|---|---|"]
    for t, names in TOPICS.items():
        qn = [q["n"] for q in QS if q["topic"] == t]
        sn = sorted({s["n"] for s in SETS for q in s["qs"] if q["topic"] == t})
        lines.append(f"| {t} | {names[i]} | {', '.join(map(str, sn))} | {compress(qn)} | {len(qn)} |")
    lines.append(f"| **{'Total' if lang == 'en' else '합계'}** | | **{len(SETS)}** | | **{len(QS)}** |")
    cnt = collections.Counter(s["stype"] for s in SETS)
    label = "**Stimulus types:** " if lang == "en" else "**자료 종류:** "
    lines += ["", label + ", ".join(f"{STYPE[k][i]} {cnt[k]}" for k in STYPE if cnt[k])]
    lines += ["", "## Answer Sheet" if lang == "en" else "## 답안 기록표", ""]
    lines += [f"- [ ] {q['n']}. A B C D" for q in QS]
    return lines


def question_file(lang):
    i = I[lang]
    L = header(lang)
    for s in SETS:
        L += ["", "---", ""]
        if lang == "en":
            L += [f"## Set {s['n']} · Questions {qrange(s)} refer to the source below.", f"*{s['kind'][0]}*", "", quote(s["stim_en"])]
        else:
            L += [f"## 자료 세트 {s['n']} · 문제 {qrange(s)}에 답하려면 아래 자료를 참고하세요.", f"*{s['kind'][0]} · {s['kind'][1]}*", "",
                  quote(s["stim_en"]), "", quote(s["stim_kr"])]
        for q in s["qs"]:
            L += ["", f"**{q['n']}.** {q['stem'][0]}  "]
            if lang == "kr":
                L.append(f"*{q['stem'][1]}*")
            L.append("")
            for k, o in zip(LET, q["opts"]):
                if lang == "en":
                    L.append(f"- ({k}) {o[0]}")
                else:
                    L += [f"- ({k}) {o[0]}  ", f"  *({k}) {o[1]}*"]
    return "\n".join(L) + "\n"


def answer_file(lang):
    i = I[lang]
    en = lang == "en"
    L = [f"# AP World History: Modern — Unit {N} MCQ Answers & Explanations" if en else f"# AP 세계사: 모던 — Unit {N} 객관식(MCQ) 정답·해설", "",
         f"> Source: Based on the existing Unit {N} notes and flashcards and the CED learning objectives · 📌 = includes content not in the notes" if en
         else f"> 출처: 기존 Unit {N} 노트·플래시카드와 CED 학습 목표 기준 · 📌 = 노트에 없는 내용이 들어간 문제", "",
         "## Answer Key" if en else "## 빠른 정답표", "", "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in range(0, len(QS), 10):
        L.append("| " + " | ".join(f"{q['n']}. {q['ans']}" for q in QS[r:r + 10]) + " |")
    for s in SETS:
        L += ["", "---", "", f"## {'Set' if en else '자료 세트'} {s['n']} · {s['kind'][i]}"]
        for q in s["qs"]:
            k = LET.index(q["ans"])
            L += ["", f"### {q['n']}. {'Answer' if en else '정답'}: **{q['ans']}**", f"*{q['stem'][i]}*", ""]
            L.append(f"- **{'Correct choice' if en else '정답 보기'}:** ({q['ans']}) {q['opts'][k][i]}")
            L.append(f"- **{'Why it is correct' if en else '정답인 이유'}:** {q['why'][i]}")
            L.append(f"- **{'Why the others are wrong' if en else '오답 해설'}:**")
            for w in sorted(q["wrong"]):
                L.append(f"  - ({w}) {q['wrong'][w][i]}")
            tag = f"`{q['topic']}` · {SKILL[q['skill']][i]} · {QTYPE[q['qtype']][i]} · {DIFF[q['diff']][i]} · {'Review' if en else '복습'}: {q['review']}"
            L.append(f"- **{'Tags' if en else '태그'}:** {tag}")
            if q.get("note"):
                L.append(f"- 📌 **{'Not in the notes' if en else '노트에 없는 내용'}:** {q['note'][i]}")
    dist = collections.Counter(q["ans"] for q in QS)
    L += ["", "---", "", "## Answer Distribution" if en else "## 정답 분포표", "", "| A | B | C | D | " + ("Total" if en else "합계") + " |", "|---|---|---|---|---|",
          f"| {dist['A']} | {dist['B']} | {dist['C']} | {dist['D']} | {len(QS)} |"]

    def table(title, groups):
        hdr = "| Category | Questions | Count | Missed (write numbers) | Correct |" if en else "| 구분 | 문제 번호 | 문제 수 | 틀린 문제 번호 | 맞힌 수 |"
        out = ["", title, "", hdr, "|---|---|---|---|---|"]
        for name, ns in groups:
            out.append(f"| {name} | {', '.join(map(str, ns))} | {len(ns)} | | /{len(ns)} |")
        return out

    L += table("## Score by Topic" if en else "## 토픽별 채점표",
               [(f"{t} {TOPICS[t][i]}", [q["n"] for q in QS if q["topic"] == t]) for t in TOPICS])
    L += table("## Score by Question Type" if en else "## 유형별 채점표",
               [(QTYPE[k][i], [q["n"] for q in QS if q["qtype"] == k]) for k in QTYPE])
    L += table("## Score by Difficulty" if en else "## 난이도별 채점표",
               [(DIFF[k][i], [q["n"] for q in QS if q["diff"] == k]) for k in DIFF])
    L += ["", "**How to use:** As you grade, write each missed question number in the \"Missed\" column. Start reviewing with the topic or type that has the lowest score, using the \"Review\" section in each question's tags." if en
          else "**사용법:** 채점하면서 틀린 문제 번호를 \"틀린 문제 번호\" 칸에 적으세요. 맞힌 비율이 가장 낮은 토픽이나 유형부터, 각 문제 태그의 \"복습\" 섹션을 다시 보세요."]
    return "\n".join(L) + "\n"


files = {
    f"AP_WH_Unit{N}_MCQ_EN.md": question_file("en"),
    f"AP_WH_Unit{N}_MCQ_KR.md": question_file("kr"),
    f"AP_WH_Unit{N}_MCQ_Answers_EN.md": answer_file("en"),
    f"AP_WH_Unit{N}_MCQ_Answers_KR.md": answer_file("kr"),
}
for name, text in files.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", name, text.count("\n"), "lines")

# ---------------------------------------------------------------- report
print("answers:", "".join(q["ans"] for q in QS))
print("distribution:", dict(sorted(collections.Counter(q["ans"] for q in QS).items())))
runs = max(len(list(g)) for _, g in itertools.groupby(q["ans"] for q in QS))
print("longest same-letter run:", runs)
print("difficulty:", dict(collections.Counter(q["diff"] for q in QS)))
print("types:", dict(collections.Counter(q["qtype"] for q in QS)))
print("topics:", dict(collections.Counter(q["topic"] for q in QS)))
print("stimulus types:", dict(collections.Counter(s["stype"] for s in SETS)))
print("pinned notes:", [q["n"] for q in QS if q.get("note")])
# correct option length vs. distractors (avoid 'longest answer is right' pattern)
longest = sum(1 for q in QS if max(range(4), key=lambda j: len(q["opts"][j][0])) == LET.index(q["ans"]))
print("questions where the correct option is the longest:", longest, "of", len(QS))
