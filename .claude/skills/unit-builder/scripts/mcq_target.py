#!/usr/bin/env python3
"""Pick the MCQ answer-position sequence (TARGET in tools/mcq/unit<N>/meta.py).

usage: python3 -I .claude/skills/unit-builder/scripts/mcq_target.py --sets 3,2,2,3,2 [--seed 7]
       python3 -I .claude/skills/unit-builder/scripts/mcq_target.py --check DBAADACB... --sets 3,2,...

--sets is the number of questions in each stimulus set, in order. A seeded random search
returns the first sequence that obeys the rules in tools/briefs/4_mcq_design_and_review.md:
  - balanced: every letter appears floor(n/4) or ceil(n/4) times
  - no run of the same letter longer than 2
  - no 4-letter window that appears twice
  - no xyxy alternation (ABAB)
  - no letter repeated inside one stimulus set
"""
import argparse, random, sys

L = "ABCD"


def problems(seq, sets):
    n, out = len(seq), []
    lo, hi = n // 4, -(-n // 4)
    for c in L:
        if not lo <= seq.count(c) <= hi:
            out.append(f"letter {c} appears {seq.count(c)} times (want {lo}–{hi})")
    for i in range(n - 2):
        if seq[i] == seq[i + 1] == seq[i + 2]:
            out.append(f"run of 3 at Q{i + 1}")
    seen = {}
    for i in range(n - 3):
        w = seq[i:i + 4]
        if w in seen:
            out.append(f"window {w} at Q{seen[w] + 1} and Q{i + 1}")
        seen.setdefault(w, i)
        if w[0] == w[2] and w[1] == w[3] and w[0] != w[1]:
            out.append(f"alternation {w} at Q{i + 1}")
    pos = 0
    for k, size in enumerate(sets, 1):
        part = seq[pos:pos + size]
        if len(set(part)) < len(part):
            out.append(f"set {k} (Q{pos + 1}–Q{pos + size}) repeats a letter: {part}")
        pos += size
    return out


def search(sets, seed, tries=200000):
    n = sum(sets)
    rng = random.Random(seed)
    for _ in range(tries):
        seq = ""
        for size in sets:
            seq += "".join(rng.sample(L, size)) if size <= 4 else "".join(rng.choice(L) for _ in range(size))
        if not problems(seq, sets):
            return seq
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sets", required=True, help="questions per stimulus set, comma-separated")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--check", help="check an existing sequence instead of searching")
    a = ap.parse_args()
    sets = [int(x) for x in a.sets.split(",")]
    if a.check:
        if len(a.check) != sum(sets):
            sys.exit(f"sequence has {len(a.check)} letters but the sets add up to {sum(sets)}")
        p = problems(a.check, sets)
        print("ok" if not p else "\n".join(p))
        sys.exit(1 if p else 0)
    seq = search(sets, a.seed)
    if not seq:
        sys.exit("no sequence found; try another --seed")
    counts = ", ".join(f"{c} {seq.count(c)}" for c in L)
    print(f'TARGET = "{seq}"  # seed {a.seed}; {counts}')


if __name__ == "__main__":
    main()
