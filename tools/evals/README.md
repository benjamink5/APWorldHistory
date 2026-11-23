# Skill evals

Test cases for the project skills in `.claude/skills/`. They live here, not inside the skill folders, so an agent that reads a skill cannot see the expected answers.

- `essay-grader/evals.json`: three graded practice answers (Unit 3 DBQ 1, Unit 3 LEQ 3, a 3-part SAQ), each with the score it was designed to earn and the assertions used to check a grading run. The student answers are in `essay-grader/inputs/`.

Write run results to `Output/<skill>-workspace/` (gitignored), not here.
