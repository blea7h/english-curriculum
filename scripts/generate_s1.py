#!/usr/bin/env python3
"""
Generate curriculum-s1.json — 48-week S1 (斑马英语 S1) curriculum pack.
12 units × 4 weeks × 3 words = 144 words, 48 weeks.
Uses official 斑马英语 S1 word list.
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "curriculum-s1.json")

# ── Metadata ──────────────────────────────────────────────────────────
METADATA = {
    "id": "cn-eng-s1-v3",
    "title": "斑马英语 S1 · 48周课程",
    "ageGroup": "3",
    "description": "斑马英语S1体系：12单元×4周×3词=144词。涵盖身体、家庭、食物、动物、交通、颜色、动作等主题。",
    "language": "zh-CN",
    "targetLanguage": "en",
    "version": "3.0.0",
    "totalWeeks": 48,
    "totalPhases": 12,
    "createdAt": "2026-06-03"
}

# ── Resource Library ──────────────────────────────────────────────────
RESOURCE_LIBRARY = [
    {"id": "sss", "type": "SSS", "name": "Super Simple Songs", "url": "", "description": "英语启蒙儿歌金牌资源，语速慢、重复高、有配套闪卡"},
    {"id": "yd", "type": "YD", "name": "Yakka Dee! (BBC)", "url": "", "description": "BBC单词启蒙动画，每集聚焦一个词，真人+动画结合"},
    {"id": "lf", "type": "LF", "name": "Little Fox", "url": "", "description": "分级动画图书馆，Level 1语速极慢，适合零基础"},
    {"id": "pp", "type": "PP", "name": "Peppa Pig", "url": "", "description": "经典生活情景动画，语速适中，英音"},
    {"id": "pf", "type": "PF", "name": "Pinkfong", "url": "", "description": "Baby Shark出品方，儿歌动作感强"},
    {"id": "cc", "type": "CC", "name": "Cocomelon", "url": "", "description": "3D儿歌动画，节奏明快，美音"},
    {"id": "bb", "type": "BB", "name": "Barefoot Books", "url": "", "description": "绘本风格儿歌，画面精美，重复句多"},
    {"id": "ss", "type": "SS", "name": "Sesame Street", "url": "", "description": "经典综合启蒙节目"},
    {"id": "kf", "type": "KF", "name": "Khan Academy Kids", "url": "", "description": "免费互动学习App"},
    {"id": "word", "type": "WORD", "name": "单词认读", "url": "", "description": "核心词汇认读，建立音-义-形连接"},
    {"id": "quiz", "type": "QUIZ", "name": "小测验", "url": "", "description": "简单互动测验，检验理解"},
    {"id": "speaking", "type": "SPEAKING", "name": "跟读口语", "url": "", "description": "引导宝宝开口跟读"},
]

# ── Chinese Translations ──────────────────────────────────────────────
CN = {
    # Unit 1 — Body
    "nose":"鼻子", "mouth":"嘴巴", "eye":"眼睛", "face":"脸", "ear":"耳朵",
    "hair":"头发", "hand":"手", "arm":"手臂", "foot":"脚", "head":"头",
    "leg":"腿", "toe":"脚趾",
    # Unit 2 — Family
    "mommy":"妈妈", "daddy":"爸爸", "sister":"姐妹", "grandma":"奶奶",
    "grandpa":"爷爷", "brother":"兄弟", "baby":"宝宝", "cat":"猫", "dog":"狗",
    "teddy bear":"泰迪熊", "ball":"球", "doll":"娃娃",
    # Unit 3 — Personal Care
    "shirt":"衬衫", "pants":"裤子", "dress":"裙子", "shoes":"鞋子",
    "socks":"袜子", "mittens":"手套", "coat":"外套", "hat":"帽子",
    "scarf":"围巾", "wash":"洗", "brush":"刷", "comb":"梳",
    # Unit 4 — Food & Drink
    "bread":"面包", "jam":"果酱", "milk":"牛奶", "hot":"热的", "water":"水",
    "cold":"冷的", "spoon":"勺子", "plate":"盘子", "cup":"杯子",
    "apple":"苹果", "banana":"香蕉", "orange":"橙子",
    # Unit 5 — Daily Life
    "door":"门", "wall":"墙", "table":"桌子", "chair":"椅子", "sofa":"沙发",
    "bed":"床", "sit":"坐", "watch":"看", "smile":"微笑", "hug":"拥抱",
    "kiss":"亲吻", "sleep":"睡觉",
    # Unit 6 — Transport & Colors
    "green":"绿色", "yellow":"黄色", "red":"红色", "bike":"自行车",
    "car":"汽车", "bus":"公交车", "train":"火车", "ship":"轮船",
    "plane":"飞机", "walk":"走路", "run":"跑步", "fly":"飞",
    # Unit 7 — Play & Hobbies
    "one":"一", "two":"二", "three":"三", "jump":"跳", "row":"划船",
    "swim":"游泳", "look":"看", "listen":"听", "sing":"唱歌",
    "dance":"跳舞", "up":"向上", "down":"向下",
    # Unit 8 — More Food
    "pear":"梨", "peach":"桃子", "kiwi":"猕猴桃", "pea":"豌豆",
    "tomato":"番茄", "carrot":"胡萝卜", "rice":"米饭", "noodles":"面条",
    "egg":"鸡蛋", "drink":"喝", "play":"玩", "eat":"吃",
    # Unit 9 — Kindergarten
    "swing":"秋千", "slide":"滑梯", "seesaw":"跷跷板", "pink":"粉色",
    "brown":"棕色", "blue":"蓝色", "shake":"摇", "tap":"拍",
    "clap":"鼓掌", "happy":"开心", "sad":"伤心", "angry":"生气",
    # Unit 10 — Animals
    "bird":"鸟", "fish":"鱼", "turtle":"乌龟", "hen":"母鸡", "duck":"鸭子",
    "pig":"猪", "cow":"奶牛", "sheep":"羊", "horse":"马", "tiger":"老虎",
    "panda":"熊猫", "monkey":"猴子",
    # Unit 11 — Community
    "park":"公园", "zoo":"动物园", "farm":"农场", "teacher":"老师",
    "doctor":"医生", "baker":"面包师", "big":"大的", "small":"小的",
    "house":"房子", "good":"好的", "morning":"早上", "night":"晚上",
    # Unit 12 — Nature
    "tree":"树", "grass":"草", "flower":"花", "hill":"小山", "river":"河流",
    "lake":"湖", "cloud":"云", "rain":"雨", "snow":"雪", "star":"星星",
    "moon":"月亮", "sun":"太阳",
}

# ── Resource Map (word → best alt resource) ──────────────────────────
RESOURCE_MAP = {
    "nose":"sss","mouth":"sss","eye":"sss","face":"sss","ear":"sss",
    "hand":"sss","arm":"sss","foot":"sss","head":"sss","leg":"sss","toe":"sss",
    "mommy":"pp","daddy":"pp","sister":"pp","grandma":"pp","grandpa":"pp",
    "brother":"pp","baby":"pf",
    "teddy bear":"sss","ball":"sss","doll":"cc",
    "shirt":"sss","pants":"cc","dress":"cc","shoes":"sss","socks":"sss","mittens":"sss",
    "coat":"pf","hat":"sss","scarf":"pp",
    "wash":"sss","brush":"sss","comb":"cc",
    "bread":"sss","jam":"sss","milk":"sss","water":"sss","spoon":"pf","plate":"pf","cup":"sss",
    "apple":"sss","banana":"sss","orange":"sss",
    "door":"sss","wall":"sss","table":"pp","chair":"sss","sofa":"sss","bed":"sss",
    "sit":"sss","smile":"sss","hug":"sss","kiss":"sss","sleep":"sss",
    "green":"sss","yellow":"sss","red":"sss","bike":"sss","car":"sss","bus":"sss",
    "train":"sss","ship":"sss","plane":"sss","walk":"sss","run":"sss","fly":"sss",
    "one":"sss","two":"sss","three":"sss","jump":"sss","swim":"sss",
    "look":"sss","listen":"sss","sing":"sss","dance":"sss","up":"sss","down":"sss",
    "pear":"sss","peach":"sss","kiwi":"sss","pea":"sss","tomato":"sss","carrot":"sss",
    "rice":"pf","noodles":"sss","egg":"sss","drink":"sss","play":"sss","eat":"sss",
    "swing":"sss","slide":"pp","seesaw":"cc","pink":"pf","brown":"sss","blue":"sss",
    "shake":"sss","tap":"sss","clap":"sss","happy":"sss","sad":"sss","angry":"sss",
    "bird":"sss","fish":"sss","turtle":"sss","hen":"sss","duck":"sss","pig":"pp",
    "cow":"sss","sheep":"sss","horse":"pf","tiger":"sss","panda":"sss","monkey":"sss",
    "park":"pp","zoo":"sss","farm":"sss","teacher":"sss","doctor":"sss","baker":"sss",
    "big":"sss","small":"sss","house":"sss","good":"sss","morning":"sss","night":"sss",
    "tree":"sss","grass":"sss","flower":"sss","hill":"pp","river":"pp","lake":"pp",
    "cloud":"sss","rain":"sss","snow":"sss","star":"sss","moon":"sss","sun":"sss",
}

# ── Unit Definitions ──────────────────────────────────────────────────
# 12 units × 4 weeks × 3 words = 144 words total
UNITS = [
    {
        "number": 1, "theme": "初识身体部位，培养健康习惯",
        "phaseId": "phase-1",
        "weeks": [
            {"words": ["nose", "mouth", "eye"]},
            {"words": ["face", "ear", "hair"]},
            {"words": ["hand", "arm", "foot"]},
            {"words": ["head", "leg", "toe"]},
        ],
        "parentTips": [
            "这周学脸部：nose, mouth, eye。洗澡时玩\"Wash your nose!\"\"Where is your mouth?\"游戏，指认游戏最有效！",
            "这周继续脸部：face, ear, hair。梳头时说\"Comb your hair!\"，玩\"Where is your ear?\"指认游戏。",
            "这周学上半身和脚：hand, arm, foot。唱Head Shoulders边唱边指！玩\"Clap your hands!\"",
            "本周复习：head, leg, toe。用Simon Says游戏巩固全部身体词。\"Touch your head!\"\"Wiggle your toes!\"",
        ],
        "sssSongs": {"main": "Head Shoulders Knees & Toes", "sec": "One Little Finger"},
    },
    {
        "number": 2, "theme": "认识家庭，珍惜家人和朋友",
        "phaseId": "phase-2",
        "weeks": [
            {"words": ["mommy", "daddy", "sister"]},
            {"words": ["grandma", "grandpa", "brother"]},
            {"words": ["baby", "cat", "dog"]},
            {"words": ["teddy bear", "ball", "doll"]},
        ],
        "parentTips": [
            "用家庭相册学mommy和daddy！指着照片说\"This is mommy!\"，叫家人时说\"Come here, daddy!\"",
            "学祖辈grandma, grandpa和brother。打电话时说\"Hello grandma!\"，抱弟弟说\"Love brother!\"",
            "这周学宠物和宝宝：baby, cat, dog。看YD认识cat和dog，唱I Have A Pet。",
            "玩具周：teddy bear, ball, doll。玩球时说\"Throw the ball!\"，抱玩偶\"I love my teddy bear!\"",
        ],
        "sssSongs": {"main": "The Mommy Song", "sec": "I Have A Pet"},
    },
    {
        "number": 3, "theme": "熟悉个人形象，培养生活习惯",
        "phaseId": "phase-3",
        "weeks": [
            {"words": ["shirt", "pants", "dress"]},
            {"words": ["shoes", "socks", "mittens"]},
            {"words": ["coat", "hat", "scarf"]},
            {"words": ["wash", "brush", "comb"]},
        ],
        "parentTips": [
            "穿衣服时是最好的学习时机！\"Put on your shirt!\"\"These are your pants!\"边穿边说。",
            "出门前学shoes, socks, mittens。\"Put on your shoes!\"\"Wear your mittens!\"唱Put On Your Shoes。",
            "天气冷了学coat, hat, scarf！\"Put on your coat!\"\"Wear your hat!\"出门前边说边穿。",
            "卫生习惯周：wash, brush, comb。刷牙时说\"Brush your teeth!\"，洗手说\"Wash your hands!\"",
        ],
        "sssSongs": {"main": "Put On Your Shoes", "sec": "The Bath Song"},
    },
    {
        "number": 4, "theme": "熟悉饮食习惯，欣赏美食",
        "phaseId": "phase-4",
        "weeks": [
            {"words": ["bread", "jam", "milk"]},
            {"words": ["hot", "water", "cold"]},
            {"words": ["spoon", "plate", "cup"]},
            {"words": ["apple", "banana", "orange"]},
        ],
        "parentTips": [
            "早餐周：bread, jam, milk。\"Let's eat bread!\"\"Drink your milk!\"边吃边说最自然。",
            "温度概念：hot, water, cold。\"The water is hot!\"\"Cold ice cream!\"用实物感受温度。",
            "餐具周：spoon, plate, cup。摆餐具时\"This is your spoon!\"，\"Put the cup on the table!\"",
            "水果周：apple, banana, orange。吃水果时\"This is a red apple!\"\"Yellow banana!\"唱The Apple Is Red。",
        ],
        "sssSongs": {"main": "Do You Like Broccoli Ice Cream", "sec": "The Apple Is Red"},
    },
    {
        "number": 5, "theme": "走进日常生活，感受家的温暖",
        "phaseId": "phase-5",
        "weeks": [
            {"words": ["door", "wall", "table"]},
            {"words": ["chair", "sofa", "bed"]},
            {"words": ["sit", "watch", "smile"]},
            {"words": ["hug", "kiss", "sleep"]},
        ],
        "parentTips": [
            "认识家：door, wall, table。\"Open the door!\"\"The book is on the table!\"在家里边走边说。",
            "家具周：chair, sofa, bed。\"Sit on the chair!\"\"Time for bed!\"\"Jump on the sofa!\"",
            "动作周：sit, watch, smile。\"Sit down please!\"\"Watch me!\"\"Show me your smile!\"",
            "情感周：hug, kiss, sleep。睡前\"Give me a hug!\"\"Good night, sleep well!\"",
        ],
        "sssSongs": {"main": "Are You Hungry", "sec": "Bedtime Song"},
    },
    {
        "number": 6, "theme": "初识交通工具，培养规则意识",
        "phaseId": "phase-6",
        "weeks": [
            {"words": ["green", "yellow", "red"]},
            {"words": ["bike", "car", "bus"]},
            {"words": ["train", "ship", "plane"]},
            {"words": ["walk", "run", "fly"]},
        ],
        "parentTips": [
            "颜色周：green, yellow, red。玩交通灯游戏\"Red light stop, green light go!\"用蜡笔画色。",
            "车车周：bike, car, bus。\"Look! A red car!\"\"Big bus!\"唱The Wheels On The Bus！",
            "交通工具周：train, ship, plane。\"Choo choo train!\"\"The plane is flying!\"用玩具演示。",
            "动作周：walk, run, fly。唱Walking Walking边唱边做！\"Let's run!\"\"Fly like a bird!\"",
        ],
        "sssSongs": {"main": "The Wheels On The Bus", "sec": "Walking Walking"},
    },
    {
        "number": 7, "theme": "体验游戏之乐，培养兴趣爱好",
        "phaseId": "phase-7",
        "weeks": [
            {"words": ["one", "two", "three"]},
            {"words": ["jump", "row", "swim"]},
            {"words": ["look", "listen", "sing"]},
            {"words": ["dance", "up", "down"]},
        ],
        "parentTips": [
            "数字周：one, two, three！\"How many fingers? One, two, three!\"边数边做。",
            "运动周：jump, row, swim。\"Jump up high!\"\"Row row row your boat!\"边唱边做动作。",
            "感官周：look, listen, sing。\"Look at that!\"\"Listen to the music!\"\"Let's sing together!\"",
            "律动周：dance, up, down。\"Let's dance!\"\"Hands up! Hands down!\"唱Stand Up Song。",
        ],
        "sssSongs": {"main": "One Two Three Song", "sec": "Row Row Row Your Boat"},
    },
    {
        "number": 8, "theme": "认识多样美食，感受美好生活",
        "phaseId": "phase-8",
        "weeks": [
            {"words": ["pear", "peach", "kiwi"]},
            {"words": ["pea", "tomato", "carrot"]},
            {"words": ["rice", "noodles", "egg"]},
            {"words": ["drink", "play", "eat"]},
        ],
        "parentTips": [
            "水果周：pear, peach, kiwi。\"Sweet pear!\"\"Yummy peach!\"吃水果时边吃边说。",
            "蔬菜周：pea, tomato, carrot。\"Green pea!\"\"Red tomato!\"\"Orange carrot!\"吃饭时指认。",
            "主食周：rice, noodles, egg。\"Eat your rice!\"\"Yummy noodles!\"\"Good egg!\"",
            "综合动作周：drink, play, eat。\"Drink some water!\"\"Let's play!\"\"Time to eat!\"",
        ],
        "sssSongs": {"main": "Do You Like Broccoli Ice Cream", "sec": "Are You Hungry"},
    },
    {
        "number": 9, "theme": "认识幼儿园环境，感受与伙伴游戏的乐趣",
        "phaseId": "phase-9",
        "weeks": [
            {"words": ["swing", "slide", "seesaw"]},
            {"words": ["pink", "brown", "blue"]},
            {"words": ["shake", "tap", "clap"]},
            {"words": ["happy", "sad", "angry"]},
        ],
        "parentTips": [
            "游乐场周：swing, slide, seesaw！去公园边玩边说\"Push the swing!\"\"Go down the slide!\"",
            "颜色周：pink, brown, blue。\"Pink flower!\"\"Brown bear!\"\"Blue sky!\"在环境中找颜色。",
            "动作周：shake, tap, clap。\"Shake your body!\"\"Tap your nose!\"\"Clap your hands!\"",
            "情绪周：happy, sad, angry。唱If You're Happy！\"Are you happy?\"\"Don't be sad!\"",
        ],
        "sssSongs": {"main": "If You're Happy", "sec": "I See Something Blue"},
    },
    {
        "number": 10, "theme": "初识动物，培养爱护动物的意识",
        "phaseId": "phase-10",
        "weeks": [
            {"words": ["bird", "fish", "turtle"]},
            {"words": ["hen", "duck", "pig"]},
            {"words": ["cow", "sheep", "horse"]},
            {"words": ["tiger", "panda", "monkey"]},
        ],
        "parentTips": [
            "小动物周：bird, fish, turtle。看鸟说\"Look! A bird!\"养金鱼说\"Pretty fish!\"",
            "农场动物1：hen, duck, pig。学动物叫声\"The duck says quack quack!\"唱Old MacDonald。",
            "农场动物2：cow, sheep, horse。\"The cow says moo!\"\"White sheep!\"\"Fast horse!\"",
            "野生动物周：tiger, panda, monkey。通过闪卡和绘本认识！\"Big tiger!\"\"Cute panda!\"",
        ],
        "sssSongs": {"main": "Old MacDonald Had A Farm", "sec": "I Have A Pet"},
    },
    {
        "number": 11, "theme": "认识社区环境，感受社区生活",
        "phaseId": "phase-11",
        "weeks": [
            {"words": ["park", "zoo", "farm"]},
            {"words": ["teacher", "doctor", "baker"]},
            {"words": ["big", "small", "house"]},
            {"words": ["good", "morning", "night"]},
        ],
        "parentTips": [
            "地点周：park, zoo, farm。\"Let's go to the park!\"\"See the animals at the zoo!\"",
            "职业周：teacher, doctor, baker。玩角色扮演\"My teacher!\"\"Doctor!\"\"Baker makes bread!\"",
            "概念周：big, small, house。\"Big elephant!\"\"Small mouse!\"\"This is our house!\"",
            "礼貌用语周：good, morning, night。每天\"Good morning!\"\"Good night!\"养成礼貌习惯。",
        ],
        "sssSongs": {"main": "Good Morning Song", "sec": "Let's Go To The Zoo"},
    },
    {
        "number": 12, "theme": "感受自然环境，培养热爱自然的意识",
        "phaseId": "phase-12",
        "weeks": [
            {"words": ["tree", "grass", "flower"]},
            {"words": ["hill", "river", "lake"]},
            {"words": ["cloud", "rain", "snow"]},
            {"words": ["star", "moon", "sun"]},
        ],
        "parentTips": [
            "自然周：tree, grass, flower。去公园\"Tall tree!\"\"Green grass!\"\"Pretty flower!\"",
            "地貌周：hill, river, lake。看PP剧集认识！\"Climb the hill!\"\"The river flows!\"",
            "天气周：cloud, rain, snow。\"White clouds!\"\"Rain rain go away!\"\"Let's play in the snow!\"",
            "天空周：star, moon, sun。唱Twinkle Twinkle！\"Good morning, sun!\"\"Good night, moon!\"S1结业啦！",
        ],
        "sssSongs": {"main": "Mr. Sun", "sec": "Twinkle Twinkle Little Star"},
    },
]

# ── Activity Helpers ──────────────────────────────────────────────────

def resource_type_for(resource_id):
    if resource_id in ("pp","pf","cc","sss","lf","bb","ss"):
        return resource_id.upper()
    if resource_id == "yd":
        return "YD"
    return "WORD"

def make_sss_activity(words, title, desc):
    return {"priority":"core","resourceId":"sss","resourceType":"SSS","title":title,"description":desc,"wordsFocus":words}

def make_word_activity(words):
    return {"priority":"core","resourceId":"word","resourceType":"WORD","title":f"核心词汇：{' '.join(words)}","description":f"跟着妈妈读单词：{' '.join(words)}","wordsFocus":words}

def make_yd_activity(word, ref):
    return {"priority":"core","resourceId":"yd","resourceType":"YD","title":f"{word.title()}","description":f"看Dee学{word}，观察真人小朋友怎么说。{ref}","wordsFocus":[word]}

def make_alt_activity(word, rid):
    if rid == "word":
        return {"priority":"core","resourceId":"word","resourceType":"WORD","title":f"图片卡：{word}","description":f"展示{word}的图片卡，家长说{word}孩子指认。","wordsFocus":[word]}
    rtype = resource_type_for(rid)
    return {"priority":"core","resourceId":rid,"resourceType":rtype,"title":f"{rtype}: {word.title()}","description":f"通过{rtype}资源学习{word}。","wordsFocus":[word]}

def make_quiz_activity(word, question=None):
    q = question or f"『Where is {word}?』——宝宝能找到{word}对应的图片或做出动作吗？"
    return {"priority":"core","resourceId":"quiz","resourceType":"QUIZ","title":"小测验","description":q,"wordsFocus":[word]}

def make_speaking_activity(word):
    return {"priority":"core","resourceId":"speaking","resourceType":"SPEAKING","title":"跟读练习","description":f"和妈妈一起说：{word}！大声说出来吧～","wordsFocus":[word]}

def make_parent_activity(title, desc, words):
    return {"priority":"core","resourceId":None,"resourceType":"PARENT","title":title,"description":desc,"wordsFocus":words}

def make_review_activity(prep, steps, script, words):
    return {"priority":"core","resourceId":None,"resourceType":"REVIEW","title":"本周综合复习","description":f"【准备】{prep}\n【步骤】{steps}\n【话术】{script}","wordsFocus":words}


# ── Input Day Builder ─────────────────────────────────────────────────

def build_input_day(unit, week_words, day_words, day_num):
    activities = []
    sss_main = unit["sssSongs"]["main"]
    sss_sec = unit["sssSongs"]["sec"]

    if day_num == 1:
        activities.append(make_sss_activity(week_words, f"SSS: {sss_main}", f"边唱边做动作，引入本周新词{'、'.join(week_words)}。重复2-3遍。"))
    elif day_num == 2:
        activities.append(make_sss_activity(week_words, f"SSS: {sss_sec or sss_main}（拓展）", f"继续巩固{'、'.join(week_words)}，配合闪卡复习。"))
    else:
        activities.append(make_sss_activity(week_words, f"SSS: {sss_main}（复习）/ {sss_sec or ''}", f"综合复习本周词汇{'、'.join(week_words)}。"))

    activities.append(make_word_activity(day_words))

    for w in day_words:
        rid = RESOURCE_MAP.get(w, "sss")
        activities.append(make_alt_activity(w, rid))

    qw = day_words[0]
    activities.append(make_quiz_activity(qw))
    sw = day_words[-1]
    activities.append(make_speaking_activity(sw))
    activities.append(make_parent_activity(
        "亲子互动：指认练习",
        f"家长说{'、'.join(week_words)}，孩子指认对应物品或图片。",
        week_words
    ))
    return activities


# ── Review Day Builder (Thu) ──────────────────────────────────────────

def build_review_day(unit, week_words):
    prep = f"本周闪卡({'、'.join(week_words)})、SSS歌曲音频/视频"
    steps = "①摊开闪卡，家长说词孩子指 ②播放本周学过的SSS歌曲边唱边做动作 ③用闪卡玩'找找看'游戏"
    script = "\"Can you find...?\" / \"Point to...!\" / \"What's this?\""
    activities = [make_review_activity(prep, steps, script, week_words)]
    activities.append({
        "priority":"core","resourceId":"sss","resourceType":"SSS",
        "title":"配套闪卡配对",
        "description":f"【准备】{unit['theme']}闪卡\n【步骤】①展示一张说英文名 ②摊开3-4张说'Find...!' ③孩子指对后鼓励 ④让孩子自己翻牌说出名字\n【话术】\"Look, this is...\" / \"Where is...? Point to...!\"",
        "wordsFocus": week_words
    })
    activities.append(make_quiz_activity(week_words[0], f"『Can you find {week_words[0]}?』——在闪卡/图片中找一找吧！"))
    activities.append(make_speaking_activity(week_words[-1]))
    return activities


# ── Output Day Builder (Fri) ──────────────────────────────────────────

def build_output_day(unit, week_words):
    return [
        {"priority":"core","resourceId":"speaking","resourceType":"SPEAKING",
         "title":"口语展示",
         "description":f"宝宝来展示一下这周学的内容吧！说给妈妈听：{' '.join(week_words)}",
         "wordsFocus": week_words},
        make_parent_activity(f"{unit['theme']}角色扮演",
            f"用玩偶/实物进行{unit['theme']}主题的角色扮演。家长引导对话：What's this? It's a...",
            week_words),
        make_parent_activity(f"画{unit['theme']}",
            f"画一幅与{unit['theme']}相关的画，边画边说{'、'.join(week_words)}。", week_words),
        make_quiz_activity(week_words[0], f"『Can you find {week_words[0]}?』——本周综合测验。")
    ]


# ── Week Builder ──────────────────────────────────────────────────────

def build_week(unit, week_idx, week_words, parent_tip, global_week_number):
    days = []
    w = week_words

    # Mon: Input word 1
    days.append({"dayOfWeek":1,"label":"周一","type":"input",
                 "activities": build_input_day(unit, w, [w[0]], 1)})
    # Tue: Input word 2
    days.append({"dayOfWeek":2,"label":"周二","type":"input",
                 "activities": build_input_day(unit, w, [w[1]], 2)})
    # Wed: Input word 3
    days.append({"dayOfWeek":3,"label":"周三","type":"input",
                 "activities": build_input_day(unit, w, [w[2]], 3)})
    # Thu: Review
    days.append({"dayOfWeek":4,"label":"周四","type":"review",
                 "activities": build_review_day(unit, w)})
    # Fri: Output
    days.append({"dayOfWeek":5,"label":"周五","type":"output",
                 "activities": build_output_day(unit, w)})

    # Theme: English words / Chinese words
    cn_words = [CN.get(word, word) for word in w]
    theme = " / ".join(w)
    themeCn = " / ".join(cn_words)

    return {
        "number": global_week_number,
        "theme": theme,
        "themeCn": themeCn,
        "phaseId": unit["phaseId"],
        "keyWords": w,
        "parentTips": parent_tip,
        "days": days
    }


# ── Main ──────────────────────────────────────────────────────────────

PHASES = []
# Phase colors cycle: units 1-3 → phase-1, 4-6 → phase-2, 7-9 → phase-3, 10-12 → phase-4
PHASE_NAMES = {
    1: "初识身体部位，培养健康习惯",
    2: "认识家庭，珍惜家人和朋友",
    3: "熟悉个人形象，培养生活习惯",
    4: "熟悉饮食习惯，欣赏美食",
    5: "走进日常生活，感受家的温暖",
    6: "初识交通工具，培养规则意识",
    7: "体验游戏之乐，培养兴趣爱好",
    8: "认识多样美食，感受美好生活",
    9: "认识幼儿园环境，感受与伙伴游戏的乐趣",
    10: "初识动物，培养爱护动物的意识",
    11: "认识社区环境，感受社区生活",
    12: "感受自然环境，培养热爱自然的意识",
}

PHASE_DESCS = {
    1: "从最熟悉的自己出发：认识身体部位。",
    2: "认识家人，培养亲情和友情感知。",
    3: "学习穿衣和卫生习惯，建立生活自理概念。",
    4: "认识常见食物和饮料，培养健康饮食习惯。",
    5: "熟悉家中物品和日常活动，感受家的温暖。",
    6: "认识交通工具和交通规则，建立安全意识。",
    7: "通过游戏和律动学习数字和动作。",
    8: "认识更多美食，丰富饮食词汇。",
    9: "认识游乐场和幼儿园环境，学习社交情感。",
    10: "认识常见动物，培养爱护动物的意识。",
    11: "认识社区场所和职业，学习礼貌用语。",
    12: "认识自然景物，培养热爱自然的意识。",
}

PHASE_ID_BY_GROUP = {1:"phase-1",2:"phase-1",3:"phase-1",
                     4:"phase-2",5:"phase-2",6:"phase-2",
                     7:"phase-3",8:"phase-3",9:"phase-3",
                     10:"phase-4",11:"phase-4",12:"phase-4"}

global_week_number = 1

for ui, unit in enumerate(UNITS):
    uidx = ui + 1  # 1-indexed
    weeks = []
    for wi, wdata in enumerate(unit["weeks"]):
        words = wdata["words"]
        parent_tip = unit["parentTips"][wi] if wi < len(unit["parentTips"]) else unit["parentTips"][0]
        w = build_week(unit, wi, words, parent_tip, global_week_number)
        weeks.append(w)
        global_week_number += 1

    pid = f"phase-{uidx}"
    PHASES.append({
        "id": pid,
        "name": PHASE_NAMES[uidx],
        "description": PHASE_DESCS[uidx],
        "order": uidx,
        "weeks": weeks
    })

pack = {
    "metadata": METADATA,
    "resourceLibrary": RESOURCE_LIBRARY,
    "phases": PHASES
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(pack, f, ensure_ascii=False, indent=2)

total_weeks = sum(len(p['weeks']) for p in PHASES)
total_activities = sum(len(day['activities']) for p in PHASES for w in p['weeks'] for day in w['days'])
print(f"✅ Written: {OUT}")
print(f"   Phases: {len(PHASES)}")
print(f"   Weeks: {total_weeks}")
print(f"   Activities: {total_activities}")
