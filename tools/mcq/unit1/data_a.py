# Unit 1 MCQ data, sets 1-6 (questions 1-14). Each text field is (EN, KR).

SETS_A = [
# ---------------------------------------------------------------- Set 1
dict(
  n=1, stype="primary",
  kind=("Primary source (philosophical text)", "1차 사료 (철학 문헌)"),
  stim_en="""> “The Master said, ‘If the people be led by laws, and uniformity sought to be given them by punishments, they will try to avoid the punishment, but have no sense of shame. If they be led by virtue, and uniformity sought to be given them by the rules of propriety, they will have the sense of shame, and moreover will become good.’”
>
> — Confucius, *The Analects*, Book 2, Chapter 3 (compiled c. 5th–4th century B.C.E.), translated by James Legge (1861). *The Analects* was one of the core texts studied for the civil service examinations of the Song dynasty (960–1279).""",
  stim_kr="""> 번역: “공자께서 말씀하셨다. ‘백성을 법으로 이끌고 형벌로 다스리면, 백성은 형벌을 피하려고만 할 뿐 부끄러움을 모른다. 백성을 덕으로 이끌고 예로 다스리면, 백성은 부끄러움을 알고 나아가 선해진다.’”
>
> — 공자 (Confucius), 『논어 (The Analects)』 제2편 제3장 (기원전 5–4세기 무렵 편찬), 제임스 레그 (James Legge) 영역 (1861). 『논어』는 송나라 (960–1279) 과거 시험을 준비하는 사람들이 공부한 핵심 경전 가운데 하나였다.""",
  qs=[
    dict(n=1, topic="1.1", ans="B", skill="S1", qtype="src", diff="E", review="1.1 §2",
      stem=("The ideas in the passage were most directly reflected in which practice of the Song dynasty?",
            "이 글의 생각이 가장 직접적으로 반영된 송나라의 제도는?"),
      opts=[("Granting land to warrior nobles in exchange for military service and loyalty", "충성과 군사 봉사의 대가로 무사 귀족에게 땅을 주는 것"),
            ("Selecting government officials through examinations on Confucian texts", "유교 경전 시험으로 관리를 뽑는 것"),
            ("Ruling conquered peoples through local leaders who paid tribute", "조공을 바치는 지역 지도자를 통해 정복민을 다스리는 것"),
            ("Requiring every adult man to perform labor for the state each year", "모든 성인 남성에게 해마다 국가를 위한 노동을 시키는 것")],
      why=("The Song expanded the civil service examinations, which tested candidates on Confucian classics such as the Analects. Officials were chosen for learning and virtue, matching the passage's ideal of ruling by virtue and propriety rather than by punishment.",
           "송나라는 『논어』 같은 유교 경전으로 시험을 치르는 과거제를 크게 넓혔다. 학식과 덕으로 관리를 뽑았으므로, 형벌이 아니라 덕과 예로 다스린다는 이 글의 이상과 맞는다."),
      wrong={"A": ("This describes feudalism in Japan and Europe; the Song placed civil officials above military commanders.", "일본과 유럽의 봉건제에 대한 설명이다. 송나라는 문관을 무관보다 위에 두었다."),
             "C": ("This describes the Mexica tribute system, not the Song.", "송나라가 아니라 메시카의 조공 제도에 대한 설명이다."),
             "D": ("This describes the Inca mit'a labor system.", "잉카의 미타 노동 제도에 대한 설명이다.")},
      note=("The Analects 2.3 passage itself is not quoted in the notes; the notes cover Confucianism and the exams in §2–§3.",
            "『논어』 2.3의 이 구절 자체는 노트에 없다. 노트는 §2–§3에서 유교와 과거제를 다룬다.")),
    dict(n=2, topic="1.1", ans="D", skill="S4", qtype="ctx", diff="M", review="1.1 §2 (How the Song Justified Its Rule)",
      stem=("Which of the following best explains why Song rulers promoted Confucian ideas like those in the passage?",
            "송나라 통치자들이 이 글과 같은 유교 사상을 장려한 이유를 가장 잘 설명하는 것은?"),
      opts=[("To prepare officials to govern newly conquered lands in Central Asia", "중앙아시아에서 새로 정복한 땅을 다스릴 관리를 기르려고"),
            ("To win the loyalty of the Jurchen and Mongol armies that threatened the northern frontier", "북쪽 국경을 위협하던 여진과 몽골 군대의 충성을 얻으려고"),
            ("To raise merchants to the top of the social order", "상인을 사회 질서의 맨 위로 올리려고"),
            ("To justify their rule and govern through officials trained in Confucian values", "유교 가치를 익힌 관리를 통해 다스리며 통치를 정당화하려고")],
      why=("The CED states that the Song used traditional Confucianism and an imperial bureaucracy to maintain and justify its rule. Confucian ideas of virtuous rule and the Mandate of Heaven gave the emperor legitimacy, and exam-trained officials carried out his policies.",
           "CED는 송나라가 전통적인 유교와 황제 관료제를 이용해 통치를 유지하고 정당화했다고 쓴다. 덕치와 천명 사상은 황제에게 정당성을 주었고, 과거로 뽑힌 관리들이 정책을 실행했다."),
      wrong={"A": ("The Song did not conquer Central Asia; it lost northern China to the Jurchen and later fell to the Mongols.", "송나라는 중앙아시아를 정복하지 않았다. 오히려 북중국을 여진에게 잃었고 뒤에 몽골에 멸망했다."),
             "B": ("The Song lost the north to the Jurchen and was later conquered by the Mongols; Confucian ideals were aimed at its own officials and subjects.", "송나라는 북쪽을 여진에게 잃었고 뒤에 몽골에 정복되었다. 유교 이념은 자기 관리와 백성을 향한 것이었다."),
             "C": ("Confucian social ranking placed merchants at the bottom.", "유교의 신분 질서는 상인을 맨 아래에 두었다.")},
      note=None),
    dict(n=3, topic="1.1", ans="A", skill="S5P", qtype="comp", diff="H", review="1.1 §5 (Japan; Vietnam); Comparison Table (Japan vs. Korea vs. Vietnam)",
      stem=("Compared with Vietnam (Đại Việt) from c. 1200 to c. 1450, Japan was different in that Japan",
            "c. 1200–1450년 베트남(다이비엣)과 비교할 때 일본이 달랐던 점은?"),
      opts=[("was ruled in practice by shoguns and a military aristocracy, not a civilian bureaucracy", "문관 관료제가 아니라 쇼군과 무사 귀족이 실제로 다스렸다"),
            ("rejected Buddhism after contact with China", "중국과 접촉한 뒤 불교를 거부했다"),
            ("was conquered by the Song dynasty and governed directly as a province of the Chinese empire", "송나라에 정복되어 중국 제국의 한 지방으로 직접 다스려졌다"),
            ("adopted Chinese writing, Buddhism, and Confucian ideas from its contacts with China", "중국과의 접촉을 통해 중국 문자, 불교, 유교 사상을 받아들였다")],
      why=("From 1192 the Kamakura shogunate held real power in Japan while the emperor had little authority, and regional rivalries continued for centuries. Vietnam, by contrast, adopted a Chinese-style bureaucracy with civil service exams and Confucian scholar-officials. (Korea is left out of the comparison because Goryeo was itself under military rule from 1170 to 1270.)",
           "1192년부터 일본에서는 가마쿠라 막부가 실권을 쥐었고 천황의 권한은 약했으며, 지역 간 경쟁이 수백 년 이어졌다. 반면 베트남은 과거제와 유학자 관리를 갖춘 중국식 관료제를 받아들였다. (고려도 1170–1270년에 무신 정권 아래 있었기 때문에 한국은 비교 대상에서 뺐다.)"),
      wrong={"B": ("Japan embraced Buddhism, including Zen, alongside Shinto.", "일본은 신토와 함께 선종을 포함한 불교를 받아들였다."),
             "C": ("Neither Japan nor Vietnam was ruled by the Song; the Mongol invasions of both also failed.", "일본도 베트남도 송나라의 지배를 받지 않았고, 두 나라에 대한 몽골의 침공도 실패했다."),
             "D": ("Japan did adopt Chinese writing, Buddhism, and Confucian ideas, but so did Vietnam, so this is a similarity, not a difference.", "일본도 중국 문자, 불교, 유교를 받아들였지만 베트남도 마찬가지였으므로, 차이점이 아니라 공통점이다.")},
      note=None),
  ]),
# ---------------------------------------------------------------- Set 2
dict(
  n=2, stype="chart",
  kind=("Chart (estimates)", "표 (추정치)"),
  stim_en="""**China's Population and Iron Output, Tang and Song (estimates)**

| Indicator | Earlier estimate | Later estimate |
|---|---|---|
| Population of China | about 50 million (c. 750, Tang) | more than 100 million (c. 1100, Song) |
| Iron output per year | about 13,500 tons (806, Tang) | about 125,000 tons (1078, Song) |

*Practice chart created for this set from commonly cited estimates (iron figures follow historian Robert Hartwell). All figures are rounded and approximate.*""",
  stim_kr="""**당·송 시기 중국의 인구와 철 생산량 (추정치)**

| 항목 | 이전 추정치 | 이후 추정치 |
|---|---|---|
| 중국 인구 | 약 5,000만 명 (c. 750년, 당) | 1억 명 이상 (c. 1100년, 송) |
| 연간 철 생산량 | 약 13,500톤 (806년, 당) | 약 125,000톤 (1078년, 송) |

*널리 인용되는 추정치로 이 세트를 위해 만든 연습용 표 (철 생산량은 역사가 로버트 하트웰 (Robert Hartwell)의 추정을 따름). 모든 수치는 반올림한 대략값이다.*""",
  qs=[
    dict(n=4, topic="1.1", ans="C", skill="S5C", qtype="cause", diff="E", review="1.1 §6",
      stem=("Which development most directly contributed to the change in population shown in the chart?",
            "표에 나타난 인구 변화에 가장 직접적으로 기여한 것은?"),
      opts=[("The Mongol conquest of China", "몽골의 중국 정복"),
            ("The spread of Buddhism from India", "인도에서 온 불교의 확산"),
            ("The introduction of fast-ripening, drought-resistant Champa rice", "빨리 익고 가뭄에 강한 참파 벼의 도입"),
            ("The Ming dynasty's maritime voyages", "명나라의 해상 원정")],
      why=("Champa rice from central Vietnam ripened quickly and resisted drought, allowing two (sometimes three) harvests a year in some areas. The larger food supply supported rapid population growth under the Song.",
           "베트남 중부에서 온 참파 벼는 빨리 익고 가뭄에 강해, 어떤 지역에서는 한 해에 두 번(때로 세 번) 수확할 수 있었다. 늘어난 식량이 송나라의 빠른 인구 증가를 뒷받침했다."),
      wrong={"A": ("The Mongol conquest came later (completed 1279) and caused great loss of life.", "몽골 정복은 더 뒤(1279년 완료)의 일이고 큰 인명 피해를 냈다."),
             "B": ("Buddhism spread to China centuries earlier and did not directly increase the food supply.", "불교는 수백 년 전에 중국에 전해졌고, 식량을 직접 늘리지 않았다."),
             "D": ("The Ming voyages (1405–1433) came long after the change shown.", "명나라의 원정(1405–1433)은 표의 변화보다 훨씬 뒤의 일이다.")},
      note=("The Tang figures (c. 750 population, 806 iron output) are not in the notes; the notes give only the Song estimates.",
            "당나라 수치(c. 750년 인구, 806년 철 생산량)는 노트에 없다. 노트에는 송나라 추정치만 있다.")),
    dict(n=5, topic="1.1", ans="A", skill="S5T", qtype="ccot", diff="M", review="1.1 §6 (Proto-Industrialization)",
      stem=("The change in iron output shown in the chart best reflects which broader development in Song China?",
            "표에 나타난 철 생산량의 변화가 가장 잘 보여 주는 송나라의 더 큰 흐름은?"),
      opts=[("Growing manufacturing and commercialization (proto-industrialization)", "제조업과 상업화의 성장 (원산업화)"),
            ("A shift from a money economy back to barter", "화폐 경제에서 물물교환으로의 후퇴"),
            ("Falling demand for tools and weapons after the Jurchen invasions of the north", "북쪽에 대한 여진의 침입 이후 도구와 무기 수요의 감소"),
            ("A decline in trade after the government banned the use of paper money", "정부가 지폐 사용을 금지한 뒤 교역이 줄어든 것")],
      why=("Song China had the world's greatest manufacturing capability. Iron and steel output, porcelain, and silk production expanded for growing markets, and paper money and trade spread, a change historians call a commercial revolution or proto-industrialization.",
           "송나라는 세계에서 가장 큰 제조 능력을 가졌다. 커지는 시장을 위해 철·강철, 도자기, 비단 생산이 늘었고 지폐와 교역도 퍼졌다. 역사가들은 이를 상업 혁명 또는 원산업화라고 부른다."),
      wrong={"B": ("The Song moved further toward a money economy, including paper money.", "송나라는 지폐를 포함한 화폐 경제로 더 나아갔다."),
             "C": ("The chart shows output rising, which reflects growing demand.", "표는 생산량이 늘었음을 보여 주며, 이는 수요가 커졌다는 뜻이다."),
             "D": ("The Song issued and used paper money, and trade grew rather than declined.", "송나라는 지폐를 발행해 썼고, 교역은 줄지 않고 늘었다.")},
      note=None),
  ]),
# ---------------------------------------------------------------- Set 3
dict(
  n=3, stype="secondary",
  kind=("Secondary source (practice passage)", "2차 사료 (연습용 글)"),
  stim_en="""> *Practice passage written for this set (not a quotation from a published historian):*
>
> By the eleventh century the Abbasid caliph in Baghdad was still honored as the head of the Sunni community, but he no longer commanded armies or collected most of the taxes. Real power had passed to men of the sword, many of them Turks from Central Asia who had first entered the Islamic world as slave-soldiers or nomadic warriors. These new rulers did not abolish the caliphate. Instead, they took the title of sultan, governed through Persian-trained officials, and presented themselves as defenders of Islam and of sharia.""",
  stim_kr="""> *이 세트를 위해 작성한 연습용 글 (출판된 역사가의 글을 인용한 것이 아님):*
>
> 번역: 11세기가 되어도 바그다드의 아바스 칼리프는 여전히 수니파 공동체의 우두머리로 존중받았지만, 더는 군대를 지휘하거나 세금 대부분을 걷지 못했다. 실제 권력은 무인들에게 넘어갔는데, 그 가운데 다수는 처음에 노예 군인이나 유목 전사로 이슬람 세계에 들어온 중앙아시아 출신 튀르크인이었다. 이 새 통치자들은 칼리프 제도를 없애지 않았다. 대신 술탄이라는 칭호를 쓰고, 페르시아식 교육을 받은 관리를 통해 다스리며, 자신을 이슬람과 샤리아의 수호자로 내세웠다.""",
  qs=[
    dict(n=6, topic="1.2", ans="D", skill="S3", qtype="src", diff="E", review="1.2 §3 (The Seljuks and the Caliph)",
      stem=("Which of the following best describes the author's main argument?",
            "글쓴이의 핵심 주장을 가장 잘 설명하는 것은?"),
      opts=[("The Abbasid Caliphate ended in the eleventh century when Turkic nomads captured and destroyed Baghdad", "11세기에 튀르크 유목민이 바그다드를 점령해 파괴하면서 아바스 칼리프조가 끝났다"),
            ("Turkic rulers replaced Islamic law with the customary law of the steppe", "튀르크 통치자들이 이슬람 법을 초원의 관습법으로 바꾸었다"),
            ("Persian officials seized power from both the caliph and the Turkic sultans", "페르시아인 관리들이 칼리프와 튀르크 술탄 모두에게서 권력을 빼앗았다"),
            ("Political and military power shifted to Turkic rulers, while the caliph kept a religious role", "정치·군사 권력은 튀르크 통치자에게 넘어갔고, 칼리프는 종교적 역할을 지켰다")],
      why=("The passage says the caliph was still honored as head of the Sunni community but no longer commanded armies, and that Turkic sultans held real power without abolishing the caliphate.",
           "글은 칼리프가 여전히 수니파 공동체의 우두머리로 존중받았지만 군대를 지휘하지 못했고, 튀르크 술탄들이 칼리프 제도를 없애지 않은 채 실권을 쥐었다고 말한다."),
      wrong={"A": ("The passage says the new rulers did not abolish the caliphate; Baghdad was sacked by the Mongols in 1258.", "글은 새 통치자들이 칼리프 제도를 없애지 않았다고 말한다. 바그다드는 1258년 몽골에게 약탈당했다."),
             "B": ("The passage says they presented themselves as defenders of sharia.", "글은 그들이 자신을 샤리아의 수호자로 내세웠다고 말한다."),
             "C": ("Persian-trained officials served the sultans; they did not take power from them.", "페르시아식 교육을 받은 관리들은 술탄을 섬겼지, 술탄에게서 권력을 빼앗지 않았다.")},
      note=None),
    dict(n=7, topic="1.2", ans="B", skill="S5C", qtype="cause", diff="M", review="1.2 §4 (The Mamluk Sultanate)",
      stem=("Which of the following most strengthened the legitimacy of the Mamluk Sultanate of Egypt, a later state of the kind the passage describes?",
            "글에 나온 것과 같은 종류의 후대 국가인 이집트 맘루크 술탄국의 정당성을 가장 크게 높인 것은?"),
      opts=[("Its conversion of most of Egypt's Christian population to Islam during the 1200s", "1200년대에 이집트 기독교인 대부분을 이슬람으로 개종시킨 것"),
            ("Its victory over the Mongols at Ain Jalut and its support of a “shadow caliph”", "아인잘루트에서 몽골을 물리치고 “그림자 칼리프”를 후원한 것"),
            ("Its alliance with the Byzantine Empire against the Seljuk Turks", "셀주크 튀르크에 맞서 비잔티움 제국과 동맹한 것"),
            ("Its founding of the House of Wisdom as a center of translation", "번역의 중심지인 지혜의 집을 세운 것")],
      why=("Defeating the Mongols at Ain Jalut (1260) protected Egypt, Mecca, and Medina and gave the new sultanate great prestige. In 1261 Baybars brought a surviving Abbasid to Cairo as a “shadow caliph,” giving the Mamluks religious legitimacy.",
           "아인잘루트 전투(1260)에서 몽골을 물리쳐 이집트와 메카·메디나를 지킨 일은 새 술탄국에 큰 명성을 주었다. 1261년 바이바르스는 살아남은 아바스 왕족을 카이로로 데려와 “그림자 칼리프”로 세워 맘루크에게 종교적 정당성을 더했다."),
      wrong={"A": ("The notes do not describe a Mamluk mass conversion of Egyptians; this was not the source of their legitimacy.", "노트는 맘루크가 이집트인을 대규모로 개종시켰다고 설명하지 않는다. 이것은 정당성의 근거가 아니었다."),
             "C": ("The Mamluks did not ally with Byzantium against the Seljuks.", "맘루크는 셀주크에 맞서 비잔티움과 동맹하지 않았다."),
             "D": ("The House of Wisdom was an Abbasid institution in Baghdad, founded centuries earlier.", "지혜의 집은 수백 년 전 바그다드에 세워진 아바스 왕조의 기관이다.")},
      note=None),
  ]),
# ---------------------------------------------------------------- Set 4
dict(
  n=4, stype="map",
  kind=("Map (description)", "지도 (설명)"),
  stim_en="""> *Map description written for this practice set:*
>
> A map of the Mediterranean and the Middle East, c. 800–1250. Arrows run from Byzantium and Persia toward **Baghdad**, labeled “Greek and Persian texts translated into Arabic.” An arrow from **India** to Baghdad is labeled “mathematics and numerals.” An arrow from **China** through Central Asia to Baghdad is labeled “papermaking.” From Baghdad, an arrow runs west across North Africa to **Córdoba** and **Toledo** in Spain, then north into France and Italy, labeled “Arabic works translated into Latin (after 1085).”""",
  stim_kr="""> *이 연습 세트를 위해 작성한 지도 설명:*
>
> 번역: c. 800–1250년의 지중해와 중동 지도. 비잔티움과 페르시아에서 **바그다드**로 향하는 화살표에는 “그리스어·페르시아어 문헌을 아랍어로 번역”이라고 적혀 있다. **인도**에서 바그다드로 가는 화살표에는 “수학과 숫자”, **중국**에서 중앙아시아를 거쳐 바그다드로 가는 화살표에는 “제지술”이라고 적혀 있다. 바그다드에서 시작한 화살표는 북아프리카를 가로질러 서쪽의 스페인 **코르도바**와 **톨레도**로 갔다가, 다시 북쪽의 프랑스와 이탈리아로 이어진다. 이 화살표에는 “아랍어 저작을 라틴어로 번역 (1085년 이후)”이라고 적혀 있다.""",
  qs=[
    dict(n=8, topic="1.2", ans="C", skill="S4", qtype="ctx", diff="M", review="1.2 §1, §6, §7",
      stem=("The movement of knowledge shown on the map was most directly made possible by",
            "지도에 나타난 지식의 이동을 가장 직접적으로 가능하게 한 것은?"),
      opts=[("the Pax Mongolica, which protected trade routes across Eurasia", "유라시아의 교역로를 보호한 팍스 몽골리카"),
            ("the Crusades, which first brought Greek learning to Europe through Jerusalem", "그리스 학문을 예루살렘을 거쳐 처음 유럽에 들여온 십자군"),
            ("the reach of Dar al-Islam across Afro-Eurasia, including Muslim rule in Spain", "스페인의 무슬림 지배를 포함해 아프로-유라시아에 걸친 다르 알 이슬람의 범위"),
            ("the Song dynasty's tributary system", "송나라의 조공 체제")],
      why=("Dar al-Islam stretched from al-Andalus to northern India and remained one cultural region with shared Arabic learning. Scholars in Baghdad gathered Greek, Persian, Indian, and Chinese knowledge, and Muslim Spain held these Arabic works; after Christian Castile took Toledo in 1085, scholars there translated them into Latin.",
           "다르 알 이슬람은 알안달루스에서 북인도까지 이어졌고, 아랍어 학문을 공유하는 하나의 문화 지역으로 남았다. 바그다드의 학자들이 그리스·페르시아·인도·중국의 지식을 모았고, 이슬람 스페인에 이 아랍어 저작들이 모여 있었다. 1085년 기독교 왕국 카스티야가 톨레도를 차지한 뒤, 그곳 학자들이 이를 라틴어로 번역했다."),
      wrong={"A": ("The Pax Mongolica (c. 1250–1350) came after most of the transfer shown, and the Mongols never ruled North Africa or Spain.", "팍스 몽골리카(c. 1250–1350)는 지도에 나온 전달 대부분보다 뒤의 일이고, 몽골은 북아프리카나 스페인을 다스린 적이 없다."),
             "B": ("The map's route runs through North Africa and Spain, not Jerusalem, and the translations began before the Crusades (1095 onward).", "지도의 경로는 예루살렘이 아니라 북아프리카와 스페인을 지나며, 번역은 십자군(1095년 이후)보다 먼저 시작되었다."),
             "D": ("The Song tributary system linked China to East and Southeast Asian states, not to the Mediterranean.", "송나라의 조공 체제는 중국과 동아시아·동남아시아 국가를 이었지, 지중해와 잇지 않았다.")},
      note=None),
    dict(n=9, topic="1.2", ans="A", skill="S5C", qtype="cause", diff="M", review="1.2 §7, §8; 1.6 §2 (Scholasticism)",
      stem=("Which of the following was a result of the transfer shown by the westward arrows?",
            "서쪽으로 향하는 화살표가 보여 주는 전달의 결과로 알맞은 것은?"),
      opts=[("Thomas Aquinas and other scholars used Aristotle to develop scholasticism", "토마스 아퀴나스 등 학자들이 아리스토텔레스를 이용해 스콜라 철학을 발전시켰다"),
            ("Christian kingdoms in Spain banned the translation of Arabic books into Latin", "스페인의 기독교 왕국들이 아랍어 책을 라틴어로 번역하는 것을 금지했다"),
            ("Europeans began growing Champa rice", "유럽인이 참파 벼를 재배하기 시작했다"),
            ("The Abbasid caliphs moved their capital from Baghdad to Córdoba", "아바스 칼리프들이 수도를 바그다드에서 코르도바로 옮겼다")],
      why=("Latin translations made in Toledo brought Aristotle and the commentaries of Ibn Rushd into European universities. Thomas Aquinas used them to build scholasticism, and this learning later fed the Renaissance.",
           "톨레도에서 만든 라틴어 번역은 아리스토텔레스와 이븐 루시드의 주석을 유럽 대학에 들여왔다. 토마스 아퀴나스는 이를 이용해 스콜라 철학을 세웠고, 이 학문은 뒤에 르네상스의 밑거름이 되었다."),
      wrong={"B": ("Christian Castile made Toledo a center for translating Arabic works after 1085.", "기독교 왕국 카스티야는 1085년 이후 톨레도를 아랍어 저작 번역의 중심지로 만들었다."),
             "C": ("Champa rice spread from Vietnam to China, not to Europe.", "참파 벼는 베트남에서 중국으로 퍼졌지, 유럽으로 가지 않았다."),
             "D": ("Córdoba was the capital of the rival Umayyad rulers of Spain, not the Abbasids.", "코르도바는 아바스 왕조가 아니라 경쟁 세력인 스페인 우마이야 왕조의 수도였다.")},
      note=None),
  ]),
# ---------------------------------------------------------------- Set 5
dict(
  n=5, stype="primary",
  kind=("Primary source (devotional poem)", "1차 사료 (신앙 시)"),
  stim_en="""> “O servant, where dost thou seek Me?
> Lo! I am beside thee.
> I am neither in temple nor in mosque: I am neither in Kaaba nor in Kailash:
> Neither am I in rites and ceremonies, nor in Yoga and renunciation.”
>
> — Kabir, weaver and poet of northern India (c. 15th century), *Songs of Kabir*, translated by Rabindranath Tagore (1915). *Kaaba:* the shrine in Mecca that Muslims face in prayer. *Kailash:* a mountain sacred to Hindus as the home of the god Shiva.""",
  stim_kr="""> 번역: “오, 종이여, 너는 어디에서 나를 찾느냐?
> 보라! 나는 네 곁에 있다.
> 나는 사원에도 모스크에도 없다. 카바에도 카일라스에도 없다.
> 의례와 의식에도, 요가와 금욕에도 나는 없다.”
>
> — 카비르 (Kabir), 북인도의 직조공이자 시인 (c. 15세기), 『카비르의 노래 (Songs of Kabir)』, 라빈드라나트 타고르 (Rabindranath Tagore) 영역 (1915). *카바 (Kaaba):* 무슬림이 기도할 때 향하는 메카의 성소. *카일라스 (Kailash):* 시바 신이 사는 곳으로 힌두교도가 신성하게 여기는 산.""",
  qs=[
    dict(n=10, topic="1.3", ans="C", skill="S2", qtype="src", diff="E", review="1.3 §3 (The Bhakti Movement)",
      stem=("The poem best reflects which belief associated with the Bhakti movement?",
            "이 시가 가장 잘 보여 주는 박티 운동의 믿음은?"),
      opts=[("Salvation comes through strict observance of caste duties and temple rituals", "카스트 의무와 사원 의례를 엄격히 지켜야 구원받는다"),
            ("Only Brahmin priests can reach the divine", "브라만 사제만 신에게 닿을 수 있다"),
            ("Personal devotion to God matters more than religious rituals and holy places", "종교 의례나 성지보다 신에 대한 개인의 헌신이 더 중요하다"),
            ("Hindus should convert to Islam to escape the caste system", "힌두교도는 카스트 제도에서 벗어나려면 이슬람으로 개종해야 한다")],
      why=("Bhakti stressed loving devotion to a single god, open to anyone regardless of caste or gender. Kabir says God is found neither in temples nor mosques nor in rituals, but close beside the seeker.",
           "박티는 카스트나 성별과 관계없이 누구에게나 열린, 한 신에 대한 사랑의 헌신을 강조했다. 카비르는 신이 사원에도 모스크에도 의례에도 없고, 찾는 사람 바로 곁에 있다고 말한다."),
      wrong={"A": ("The poem rejects rites and ceremonies, and Bhakti challenged caste hierarchy.", "시는 의례와 의식을 거부하며, 박티는 카스트 위계에 도전했다."),
             "B": ("Bhakti taught that anyone could reach God through devotion, not only priests.", "박티는 사제만이 아니라 누구나 헌신으로 신에게 닿을 수 있다고 가르쳤다."),
             "D": ("Kabir rejects both the mosque and the temple; he does not call for conversion.", "카비르는 모스크와 사원을 모두 거부하며, 개종을 요구하지 않는다.")},
      note=("The poem's text and the explanations of the Kaaba and Kailash are not in the notes; the notes describe Kabir as blending Hindu and Muslim ideas and criticizing empty ritual (1.3 §3–§4).",
            "시의 원문과 카바·카일라스 설명은 노트에 없다. 노트는 카비르를 힌두교와 이슬람의 생각을 섞고 형식적인 의례를 비판한 인물로 설명한다 (1.3 §3–§4).")),
    dict(n=11, topic="1.3", ans="B", skill="S4", qtype="ctx", diff="M", review="1.3 §4–§5",
      stem=("The poem was most likely written in the context of",
            "이 시가 쓰인 배경으로 가장 알맞은 것은?"),
      opts=[("the Gupta Empire's support for Hindu temple building and Sanskrit learning", "힌두 사원 건축과 산스크리트 학문을 후원한 굽타 제국"),
            ("Muslim rule in northern India and growing contact between Hindu and Muslim communities", "북인도의 무슬림 지배와 힌두·무슬림 공동체 사이의 접촉 증가"),
            ("the arrival of Christian missionaries from Portugal", "포르투갈에서 온 기독교 선교사의 도착"),
            ("the Khmer Empire's conquest of the Indian subcontinent", "크메르 제국의 인도 아대륙 정복")],
      why=("After 1206 the Delhi Sultanate brought Muslim rule to northern India. Sufis and Bhakti poets lived side by side, and figures such as Kabir blended Hindu and Muslim ideas, teaching that God is one whether called Rama or Allah.",
           "1206년 이후 델리 술탄국이 북인도에 무슬림 지배를 가져왔다. 수피와 박티 시인들이 함께 살았고, 카비르 같은 인물은 힌두교와 이슬람의 생각을 섞어 신을 라마라 부르든 알라라 부르든 하나라고 가르쳤다."),
      wrong={"A": ("The Gupta Empire collapsed around 550, centuries before Kabir, and the poem rejects temple worship.", "굽타 제국은 카비르보다 수백 년 앞선 550년 무렵 무너졌고, 시는 사원 숭배를 거부한다."),
             "C": ("Portuguese missionaries arrived only after 1498.", "포르투갈 선교사는 1498년 이후에야 왔다."),
             "D": ("The Khmer Empire ruled mainland Southeast Asia, not India.", "크메르 제국은 인도가 아니라 동남아시아 본토를 다스렸다.")},
      note=None),
    dict(n=12, topic="1.3", ans="D", skill="S5P", qtype="comp", diff="M", review="1.3 Comparison Table (Bhakti vs. Sufism)",
      stem=("The ideas in the poem are most similar to the ideas of which other group in the same period?",
            "이 시의 생각과 가장 비슷한 생각을 가진 같은 시기의 집단은?"),
      opts=[("Confucian scholar-officials who stressed proper rituals and social hierarchy", "올바른 예와 사회 위계를 강조한 유교 사대부"),
            ("Mamluk rulers who supported an Abbasid caliph in Cairo", "카이로의 아바스 칼리프를 후원한 맘루크 통치자"),
            ("Catholic scholastics who used Aristotle's logic to explain Christian doctrine", "아리스토텔레스의 논리로 기독교 교리를 설명한 가톨릭 스콜라 학자"),
            ("Sufi mystics who sought a direct, personal experience of God", "신에 대한 직접적이고 개인적인 체험을 추구한 수피 신비주의자")],
      why=("Like Bhakti poets, Sufis were mystics who sought closeness to God through devotion, poetry, and music rather than formal ritual, and both movements appealed to ordinary people and outsiders.",
           "박티 시인처럼 수피도 형식적인 의례보다 헌신, 시, 음악으로 신과 가까워지려 한 신비주의자였다. 두 운동 모두 평범한 사람들과 소외된 사람들에게 호소했다."),
      wrong={"A": ("Confucian scholars stressed ritual propriety and hierarchy, which the poem rejects.", "유교 학자들은 시가 거부하는 의례와 위계를 강조했다."),
             "B": ("Supporting a shadow caliph was a political strategy for legitimacy, not a devotional idea.", "그림자 칼리프를 세운 것은 정당성을 얻기 위한 정치 전략이지, 신앙에 관한 생각이 아니다."),
             "C": ("Scholastics stressed reason and logic, not the inner devotion the poem describes.", "스콜라 학자들은 시가 말하는 내면의 헌신이 아니라 이성과 논리를 강조했다.")},
      note=None),
  ]),
# ---------------------------------------------------------------- Set 6
dict(
  n=6, stype="map",
  kind=("Map (description)", "지도 (설명)"),
  stim_en="""> *Map description written for this practice set:*
>
> A map of Southeast Asia, c. 1000. A shaded area labeled **Srivijaya** covers southern Sumatra, the Malay Peninsula, and both shores of the narrow **Strait of Malacca**, through which arrows marked “ships between India and China” pass. Farther north, a second shaded area labeled **Khmer Empire** covers the lowlands along the **Mekong River**. Its capital, **Angkor**, is marked with symbols for large reservoirs and canals.""",
  stim_kr="""> *이 연습 세트를 위해 작성한 지도 설명:*
>
> 번역: c. 1000년의 동남아시아 지도. **스리위자야**라고 적힌 색칠된 지역은 수마트라 남부, 말레이반도, 그리고 좁은 **말라카 해협**의 양쪽 해안을 덮고 있으며, “인도와 중국 사이를 오가는 배”라고 적힌 화살표가 이 해협을 지나간다. 더 북쪽에는 **크메르 제국**이라고 적힌 두 번째 색칠된 지역이 **메콩강**을 따라 펼쳐진 저지대를 덮고 있다. 수도 **앙코르**에는 큰 저수지와 운하를 나타내는 기호가 있다.""",
  qs=[
    dict(n=13, topic="1.3", ans="A", skill="S5P", qtype="comp", diff="M", review="1.3 §7–§9; Comparison Table (Four States)",
      stem=("Based on the map, which of the following best describes a difference between the two states?",
            "지도를 바탕으로 할 때 두 나라의 차이점을 가장 잘 설명하는 것은?"),
      opts=[("Srivijaya relied on taxing sea trade, while the Khmer relied more on irrigated rice farming", "스리위자야는 해상 교역 과세에, 크메르는 관개 벼농사에 더 의존했다"),
            ("Srivijaya was ruled by Hindu priests, while the Khmer Empire rejected Indian religions", "스리위자야는 힌두 사제가 다스렸고, 크메르 제국은 인도 종교를 거부했다"),
            ("Srivijaya was ruled directly by the Song dynasty, while the Khmer Empire was independent", "스리위자야는 송나라의 직접 지배를 받았고, 크메르 제국은 독립국이었다"),
            ("Srivijaya refused to trade with China, while the Khmer Empire depended heavily on Chinese merchants", "스리위자야는 중국과의 교역을 거부했고, 크메르 제국은 중국 상인에게 크게 의존했다")],
      why=("Srivijaya controlled the Strait of Malacca and used its navy to tax ships traveling between India and China, making it a sea-based state. The Khmer Empire was land-based; its reservoirs (barays) and canals supported rice farming with several harvests a year.",
           "스리위자야는 말라카 해협을 장악하고 해군을 이용해 인도와 중국 사이를 오가는 배에 세금을 걷은 해상 국가였다. 크메르 제국은 육상 국가로, 저수지(바라이)와 운하가 한 해에 여러 번 수확하는 벼농사를 뒷받침했다."),
      wrong={"B": ("Both were shaped by Indian religions: Srivijaya was mainly Buddhist (the textbook's 1.3 reading agrees), and the Khmer were Hindu and later Buddhist.", "두 나라 모두 인도 종교의 영향을 받았다. 스리위자야는 주로 불교 국가였고(교재 1.3도 같음), 크메르는 힌두교, 뒤에 불교 국가였다."),
             "C": ("Srivijaya sent tribute to China but was not ruled by it.", "스리위자야는 중국에 조공을 보냈지만 중국의 지배를 받지는 않았다."),
             "D": ("Srivijaya grew rich from ships traveling between India and China and sent tribute to China; the map shows the Khmer's wealth in farmland and reservoirs.", "스리위자야는 인도와 중국을 오가는 배로 부유해졌고 중국에 조공을 보냈다. 지도는 크메르의 부가 농지와 저수지에 있었음을 보여 준다.")},
      note=None),
    dict(n=14, topic="1.7", ans="C", skill="S5P", qtype="comp", diff="H", review="1.7 §5–§6; 1.5 §2",
      stem=("Srivijaya's main method of gaining wealth was most similar to that of which state in the period c. 1200–c. 1450?",
            "스리위자야가 부를 얻은 주된 방법과 가장 비슷한 방법을 쓴 c. 1200–1450년의 국가는?"),
      opts=[("The Inca Empire, which required labor service from its subjects through the mit'a", "미타로 백성에게 노동 봉사를 요구한 잉카 제국"),
            ("The Song dynasty, which chose officials through examinations", "과거로 관리를 뽑은 송나라"),
            ("The Mali Empire, which taxed the gold and salt trade crossing its lands", "자기 땅을 지나는 금·소금 교역에 세금을 매긴 말리 제국"),
            ("The Holy Roman Empire, whose emperors were elected by German princes", "독일 제후들이 황제를 선출한 신성 로마 제국")],
      why=("Both Srivijaya and Mali grew rich by controlling a major trade route and taxing the goods that passed through it: ships in the Strait of Malacca for Srivijaya, and trans-Saharan gold, salt, and copper for Mali.",
           "스리위자야와 말리는 모두 큰 교역로를 장악하고 그곳을 지나는 상품에 세금을 매겨 부유해졌다. 스리위자야는 말라카 해협을 지나는 배에, 말리는 사하라 횡단 교역의 금·소금·구리에 세금을 매겼다."),
      wrong={"A": ("The mit'a was a labor tax used to build roads and farm state lands, not a tax on trade.", "미타는 도로 건설과 국가 농지 경작에 쓰인 노동세이지, 교역에 대한 세금이 아니다."),
             "B": ("Examinations were a way to staff the government, not a way to gain wealth.", "과거는 관리를 뽑는 방법이지, 부를 얻는 방법이 아니다."),
             "D": ("Election of emperors concerns how power was transferred, not how wealth was gained.", "황제 선출은 권력이 넘어가는 방식이지, 부를 얻는 방법이 아니다.")},
      note=None),
  ]),
]
