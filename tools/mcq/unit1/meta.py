"""Unit 1 MCQ metadata: unit number, topic titles, and the answer-position sequence.

TARGET was chosen by a seeded random search under these rules: balanced counts, no run longer
than 2, no repeated 4-letter window, no xyxy alternation, and no repeated letter inside one
stimulus set. gen.py moves each question's correct option to its TARGET letter and keeps the
distractors in their relative order, so the data files can be written with any answer position.
"""
UNIT = 1
TOPICS = {
    "1.1": ("Developments in East Asia from c. 1200 to c. 1450", "동아시아의 발전, c. 1200–1450"),
    "1.2": ("Developments in Dar al-Islam from c. 1200 to c. 1450", "다르 알 이슬람의 발전, c. 1200–1450"),
    "1.3": ("Developments in South and Southeast Asia from c. 1200 to c. 1450", "남아시아와 동남아시아의 발전, c. 1200–1450"),
    "1.4": ("State Building in the Americas", "아메리카의 국가 형성"),
    "1.5": ("State Building in Africa", "아프리카의 국가 형성"),
    "1.6": ("Developments in Europe from c. 1200 to c. 1450", "유럽의 발전, c. 1200–1450"),
    "1.7": ("Comparison in the Period from c. 1200 to c. 1450", "c. 1200–1450년 시기의 비교"),
}
TARGET = "DBAADACBDCABACCBADBCADCCBDBABD"
