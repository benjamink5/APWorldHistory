"""PROVENANCE ONLY — already applied. Do not rerun on the JSON files in this folder.

The region JSON here is the output of this script. It filled the reign/lifespan dates that
the Unit 1 notes did not give (standard reference dates; Genghis and Kublai match the Unit 2
mind map) and unified Korean spellings. Keep it as the record of which dates came from
outside the notes. Original usage: python3 -I fix_data.py <raw_dir> <out_dir>
Dates: standard reference dates (Unit 2 mind map where the person also appears there).
"""
import glob
import json
import os
import re
import sys

in_dir, out_dir = sys.argv[1], sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

# (order, English name prefix) -> (EN parenthetical, KR parenthetical)
DATES = {
    (1, "Xuanzang"): ("602–664", "602–664"),
    (1, "Zhao Kuangyin"): ("r. 960–976", "재위 960–976"),
    (1, "Bi Sheng"): ("c. 990–1051", "c. 990–1051"),
    (1, "Kublai Khan"): ("r. 1260–1294", "재위 1260–1294"),
    (1, "Phagpa"): ("1235–1280", "1235–1280"),
    (1, "Zhu Yuanzhang"): ("r. 1368–1398", "재위 1368–1398"),
    (1, "Zheng He"): ("1371–c. 1433", "1371–c. 1433"),
    (2, "Murasaki Shikibu"): ("c. 973–c. 1014", "c. 973–c. 1014"),
    (2, "Minamoto no Yoritomo"): ("1147–1199", "1147–1199"),
    (3, "Yi Seong-gye"): ("r. 1392–1398", "재위 1392–1398"),
    (3, "King Sejong"): ("r. 1418–1450", "재위 1418–1450"),
    (4, "Lê Lợi"): ("r. 1428–1433", "재위 1428–1433"),
    (5, "Genghis Khan"): ("b. 1162; r. 1206–1227", "1162년 출생, 재위 1206–1227"),
    (5, "Hulagu"): ("r. 1256–1265", "재위 1256–1265"),
    (5, "Timur"): ("r. 1370–1405", "재위 1370–1405"),
    (6, "Muhammad"): ("c. 570–632", "c. 570–632"),
    (7, "Tughril Beg"): ("r. 1037–1063", "재위 1037–1063"),
    (7, "Nizam al-Mulk"): ("1018–1092", "1018–1092"),
    (7, "Osman"): ("r. c. 1299–1324", "재위 c. 1299–1324"),
    (7, "Mehmed II"): ("r. 1451–1481", "재위 1451–1481"),
    (8, "Saladin"): ("r. 1174–1193", "재위 1174–1193"),
    (8, "Shajar al-Durr"): ("r. 1250", "재위 1250"),
    (8, "Qutuz"): ("r. 1259–1260", "재위 1259–1260"),
    (8, "Baybars"): ("r. 1260–1277", "재위 1260–1277"),
    (8, "Qalawun"): ("r. 1279–1290", "재위 1279–1290"),
    (10, "Qutb al-Din Aibak"): ("r. 1206–1210", "재위 1206–1210"),
    (10, "Moinuddin Chishti"): ("1143–1236", "1143–1236"),
    (10, "Alauddin Khalji"): ("r. 1296–1316", "재위 1296–1316"),
    (10, "Nizamuddin Auliya"): ("1238–1325", "1238–1325"),
    (11, "Harihara and Bukka"): ("Harihara I r. 1336–1356; Bukka I r. 1356–1377", "하리하라 1세 재위 1336–1356, 부카 1세 재위 1356–1377"),
    (13, "Raden Wijaya"): ("r. 1293–1309", "재위 1293–1309"),
    (13, "Gajah Mada"): ("d. c. 1364", "c. 1364년 사망"),
    (14, "Jayavarman II"): ("r. from 802", "802년 즉위"),
    (20, "Itzcoatl"): ("r. 1427–1440", "재위 1427–1440"),
    (21, "Topa Inca"): ("r. 1471–1493", "재위 1471–1493"),
    (21, "Huayna Capac"): ("r. 1493–1527", "재위 1493–1527"),
    (21, "Huáscar and Atahualpa"): ("Huáscar r. 1527–1532; Atahualpa r. 1532–1533", "우아스카르 재위 1527–1532, 아타우알파 재위 1532–1533"),
    (23, "Sundiata Keita"): ("r. c. 1235–c. 1255", "재위 c. 1235–c. 1255"),
    (23, "Abu Ishaq al-Sahili"): ("d. 1346", "1346년 사망"),
    (23, "Mansa Sulayman"): ("r. c. 1341–1360", "재위 c. 1341–1360"),
    (25, "Ezana"): ("r. 4th century", "4세기 재위"),
    (25, "Yekuno Amlak"): ("r. 1270–1285", "재위 1270–1285"),
    (27, "Pope Urban II"): ("pope 1088–1099", "교황 재위 1088–1099"),
    (27, "Pope Innocent III"): ("pope 1198–1216", "교황 재위 1198–1216"),
    (27, "Pope Boniface VIII"): ("pope 1294–1303", "교황 재위 1294–1303"),
    (27, "Pope Clement VI"): ("pope 1342–1352", "교황 재위 1342–1352"),
    (28, "William the Conqueror"): ("r. 1066–1087", "재위 1066–1087"),
    (28, "King John"): ("r. 1199–1216", "재위 1199–1216"),
    (28, "Simon de Montfort"): ("c. 1208–1265", "c. 1208–1265"),
    (28, "Edward I"): ("r. 1272–1307", "재위 1272–1307"),
    (28, "Edward III"): ("r. 1327–1377", "재위 1327–1377"),
    (28, "Wat Tyler and John Ball"): ("both d. 1381", "두 사람 모두 1381년 사망"),
    (29, "Christine de Pizan"): ("1364–c. 1430", "1364–c. 1430"),
    (29, "Joan of Arc"): ("c. 1412–1431", "c. 1412–1431"),
    (30, "Charlemagne"): ("r. 768–814; crowned emperor 800", "재위 768–814, 800년 황제 대관"),
    (30, "Otto I"): ("r. 936–973; crowned emperor 962", "재위 936–973, 962년 황제 대관"),
    (30, "Marco Polo"): ("1254–1324", "1254–1324"),
    (30, "Charles IV"): ("r. 1346–1378", "재위 1346–1378"),
    (30, "Johannes Gutenberg"): ("c. 1400–1468", "c. 1400–1468"),
    (31, "Gerard of Cremona"): ("c. 1114–1187", "c. 1114–1187"),
    (31, "Ferdinand and Isabella"): ("Isabella r. 1474–1504; Ferdinand r. 1479–1516", "이사벨 재위 1474–1504, 페르난도 재위 1479–1516"),
    (32, "Ivan the Great"): ("r. 1462–1505", "재위 1462–1505"),
}

EN_PAR = re.compile(r"\((?:dates unknown|crowned emperor \d+|ruling by \d+|d\. \d+)\)")
KR_PAR = re.compile(r"\((?:생몰 미상|생몰년 미상|연도 미상|미상|\d+년 황제 대관|\d+년에는 재위 중|\d+년 사망)\)")

KR_SPELL = [
    ("레콩키스타", "레콘키스타"),
    ("칭기스 칸", "칭기즈 칸"),
    ("아인 잘루트", "아인잘루트"),
    ("비자야나가라", "비자야나가르"),
    ("믈라카", "말라카"),
]

used, missing = set(), []
for path in sorted(glob.glob(os.path.join(in_dir, "*.json"))):
    with open(path, encoding="utf-8") as f:
        regions = json.load(f)
    for r in regions:
        for it in r["people"]:
            key = next((k for k in DATES if k[0] == r["order"] and it["en"].startswith(k[1] + " (")), None)
            if key:
                en_p, kr_p = DATES[key]
                new_en, n1 = EN_PAR.subn(f"({en_p})", it["en"], count=1)
                new_kr, n2 = KR_PAR.subn(f"({kr_p})", it["kr"], count=1)
                if n1 != 1 or n2 != 1:
                    missing.append((key, n1, n2, it["kr"][:80]))
                    continue
                it["en"], it["kr"] = new_en, new_kr
                used.add(key)
            elif EN_PAR.search(it["en"]) or KR_PAR.search(it["kr"]):
                missing.append(("NO DATE ENTRY", r["order"], it["en"][:80]))
        for kind in ("people", "events", "institutions"):
            for it in r[kind]:
                for a, b in KR_SPELL:
                    it["kr"] = it["kr"].replace(a, b)
        for a, b in KR_SPELL:
            r["name_kr"] = r["name_kr"].replace(a, b)
    with open(os.path.join(out_dir, os.path.basename(path)), "w", encoding="utf-8") as f:
        json.dump(regions, f, ensure_ascii=False, indent=1)

unused = set(DATES) - used
print("filled:", len(used), "| unused keys:", sorted(unused), "| problems:", missing)
sys.exit(1 if missing or unused else 0)
