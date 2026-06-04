#!/usr/bin/env python3
"""Enrich parentTips in curriculum-s1.json.

Each parentTip currently is 1-2 sentences. Expand to 3-4 sentences
with practical play ideas, daily routine integration, and TPR suggestions.
"""
import json, re

with open('data/curriculum-s1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Enriched parentTips for each week
enriched_tips = {
    1: "这周学脸部：nose, mouth, eye。🅰 洗澡时玩\"Wash your nose!\"\"Where is your mouth?\"指认游戏。🅱 唱Head Shoulders Knees & Toes边唱边指，重点放慢nose和mouth。🅲 用镜子玩Face Game——指着自己的nose说\"Mommy's nose\"，再指宝宝的说\"Baby's nose\"。",
    2: "这周继续脸部：face, ear, hair。🅰 梳头时说\"Comb your hair!\"，玩\"Where is your ear?\"指认。🅱 画人脸简笔画，边画边说\"This is the face\"\"Two ears\"，让孩子帮忙画。🅲 唱One Little Finger，唱到\"point to the ceiling\"时改成\"point to your ear\"。",
    3: "这周学上半身和脚：hand, arm, foot。🅰 唱Head Shoulders边唱边指，熟练后加快速度挑战反应。🅱 玩\"Touch Game\"——\"Touch your hand!\"\"Touch your arm!\"看谁反应快。🅲 画手印脚印，边画边说\"This is my hand!\"\"Big foot!\"",
    4: "本周复习：head, leg, toe。🅰 用Simon Says游戏巩固全部身体词。\"Simon says touch your head!\"\"Wiggle your toes!\"🅱 唱Head Shoulders Knees & Toes完整版，特别强调knees和toes。🅲 睡前玩身体歌谣，边指边唱强化记忆。",
    5: "家庭主题：mommy, daddy, sister。🅰 翻家庭相册，指着照片说\"This is mommy!\"\"Where is daddy?\"🅱 玩Who's Calling游戏——假装打电话\"Hello, mommy!\"\"Bye bye, daddy!\"🅲 唱The Mommy Song，边唱边做家庭角色动作。",
    6: "祖辈周：grandma, grandpa, brother。🅰 打视频电话时让孩子说\"Hello, grandma!\"\"Love you, grandpa!\"🅱 看Peppa Pig——Peppa's Grandma和Grandpa的片段，指认角色。🅲 抱弟弟/玩偶说\"Love brother!\"，拍全家福时学称谓。",
    7: "宠物和宝宝：baby, cat, dog。🅰 看Yakka Dee!认识cat和dog，边看边模仿叫声。🅱 走路上看到猫狗马上指出\"Look! A cat!\"\"Big dog!\"🅲 唱I Have A Pet，用玩偶当道具比划。",
    8: "玩具周：teddy bear, ball, doll。🅰 玩球时说\"Throw the ball!\"\"Catch the ball!\"抱玩偶说\"I love my teddy bear!\"🅱 把玩具藏起来玩Hide & Seek——\"Where is the ball?\"\"Find teddy bear!\"🅲 用3个玩具练习数数和指认。",
    9: "穿衣周：shirt, pants, dress。🅰 穿衣服时是最好的学习时机！\"Put on your shirt!\"\"These are your pants!\"边穿边说。🅱 整理衣柜时玩配对——\"Where is the blue shirt?\"\"Baby's dress!\"🅲 唱Put On Your Shoes改编版，把歌词换成shirt/pants/dress。",
    10: "出门装备：shoes, socks, mittens。🅰 出门前\"Put on your shoes!\"\"Wear your mittens!\"边穿边互动。🅱 穿鞋比赛——\"Find your shoes!\"\"Put on your socks!\"看谁穿得快。🅲 唱Put On Your Shoes完整版，跟着视频做动作。",
    11: "保暖穿搭：coat, hat, scarf。🅰 出门前\"Put on your coat!\"\"Wear your hat!\"边说边帮孩子穿。🅱 玩角色扮演——给玩偶穿衣服\"Teddy needs his scarf!\"🅲 唱天气相关歌曲，结合本周词汇。",
    12: "卫生习惯：wash, brush, comb。🅰 早晚刷牙时说\"Brush your teeth!\"洗手说\"Wash your hands!\"餐前必说。🅱 唱The Bath Song边唱边做动作，强化wash概念。🅲 梳头比赛——\"Comb mommy's hair!\"\"Comb your hair!\"用梳子互动。",
    13: "早餐周：bread, jam, milk。🅰 \"Let's eat bread!\"\"Drink your milk!\"边吃边说最自然。🅱 摆餐桌时问\"Do you want jam on your bread?\"让孩子点头或说yes。🅲 用玩具厨房过家家，假装做早餐。",
    14: "温度概念：hot, water, cold。🅰 喝热水说\"Hot water!\"吃冰淇淋\"Cold ice cream!\"用实物感受温度。🅱 洗澡时玩冷热水——\"Hot water\"(热水出) \"Cold water\"(冷水出)。🅲 唱有关天气/温度的歌谣。",
    15: "餐具周：spoon, plate, cup。🅰 摆餐具时\"This is your spoon!\"\"Put the cup on the table!\"让孩子帮忙。🅱 吃饭时问\"Where is your spoon?\"\"Can you find your cup?\"🅲 玩角色扮演餐厅游戏，用玩具餐具练习。",
    16: "水果周：apple, banana, orange。🅰 吃水果时\"This is a red apple!\"\"Yellow banana!\"边切边说。🅱 唱The Apple Is Red，用真实水果当道具。🅲 玩水果猜猜看——摸一摸、闻一闻，猜\"What fruit is this?\"",
    17: "认识家：door, wall, table。🅰 \"Open the door!\"\"The book is on the table!\"在家里边走边说。🅱 玩找东西游戏——\"Touch the door!\"\"Where is the wall?\"🅲 画家里的平面图，标记door/wall/table的位置。",
    18: "家具周：chair, sofa, bed。🅰 \"Sit on the chair!\"\"Time for bed!\"\"Jump on the sofa!\"日常指令融入。🅱 玩家具配对卡——图片和实物对应。🅲 睡前唱摇篮曲，在床上说\"Good night, bed!\"",
    19: "动作周：sit, watch, smile。🅰 \"Sit down please!\"\"Watch me!\"\"Show me your smile!\"用动作强化理解。🅱 拍照片时\"Say cheese and smile!\"一起做笑脸。🅲 看电视时\"Let's watch together!\"用遥控器指认。",
    20: "情感周：hug, kiss, sleep。🅰 睡前\"Give me a hug!\"\"Good night, sleep well!\"🅱 玩情感卡片——\"Show me hug!\"\"Give a kiss!\"🅲 唱甜蜜的晚安歌曲，用玩偶演示hug和sleep。",
    21: "颜色周：green, yellow, red。🅰 玩交通灯游戏\"Red light stop! Green light go!\"🅱 用蜡笔画画——\"Let's color a red apple!\"\"Yellow banana!\"🅲 在家里找颜色——\"Find something green!\"\"Where is yellow?\"",
    22: "车车周：bike, car, bus。🅰 路上看到车马上指出\"Look! A red car!\"\"Big bus!\"🅱 唱The Wheels On The Bus，用动作模拟车轮和喇叭。🅲 用玩具车排排队——\"Red car, blue car, yellow bus\"边排边数。",
    23: "交通工具：train, ship, plane。🅰 \"Choo choo train!\"\"The plane is flying!\"用玩具演示声音和动作。🅱 看相关的SSS歌曲视频，指认train/ship/plane。🅲 折纸飞机飞出去——\"Fly, plane, fly!\"",
    24: "动作动词：walk, run, fly。🅰 唱Walking Walking边唱边做！\"Let's run!\"\"Fly like a bird!\"🅱 户外活动时——\"Walk to the tree!\"\"Run to mommy!\"🅲 玩Simon Says——\"Simon says walk!\"\"Simon says fly!\"",
    25: "数字周：one, two, three。🅰 \"How many fingers? One, two, three!\"边数边伸出手指。🅱 爬楼梯时数数——\"One step, two steps, three steps!\"🅲 用积木搭高塔——\"One block, two blocks, three!\"推倒说\"All fall down!\"",
    26: "运动周：jump, row, swim。🅰 \"Jump up high!\"\"Row row row your boat!\"边唱边做动作。🅱 洗澡时玩游泳——\"The baby is swimming!\"用动作演示。🅲 在床上/垫子上——\"Let's jump like a frog!\"",
    27: "感官周：look, listen, sing。🅰 \"Look at that!\"\"Listen to the music!\"\"Let's sing together!\"日常引导观察。🅱 玩感官游戏——\"Look! What's this?\"摇铃铛\"Listen!\"🅲 一起唱本周学过SSS歌曲，鼓励跟唱。",
    28: "律动周：dance, up, down。🅰 \"Let's dance!\"\"Hands up! Hands down!\"放音乐跳舞。🅱 唱Stand Up Song，按歌词做up/down动作。🅲 玩高矮游戏——\"Stand up tall!\"\"Sit down low!\"对比up和down。",
    29: "水果周B：pear, peach, kiwi。🅰 \"Sweet pear!\"\"Yummy peach!\"吃水果时边吃边说颜色和味道。🅱 切水果——\"Cut the pear!\"\"Open the kiwi!\"触摸不同质感。🅲 做水果沙拉，边做边学水果名称。",
    30: "蔬菜周：pea, tomato, carrot。🅰 吃饭时指认\"Green pea!\"\"Red tomato!\"\"Orange carrot!\"🅱 玩超市游戏——\"Buy some carrots!\"\"I want tomatoes!\"用玩具菜篮假装购物。🅲 给蔬菜涂色——\"Color the carrot orange!\"",
    31: "主食周：rice, noodles, egg。🅰 \"Eat your rice!\"\"Yummy noodles!\"\"Good egg!\"三餐自然融入。🅱 用筷子/勺子玩Pretend Play——假装做饭。🅲 打开鸡蛋做早餐——\"Crack the egg!\"看蛋黄流出。",
    32: "综合动作：drink, play, eat。🅰 \"Drink some water!\"\"Let's play!\"\"Time to eat!\"日常高频指令。🅱 玩角色扮演——给娃娃\"喂食\"\"喝水\"。🅲 唱日常作息歌曲，按时间段做drink/play/eat动作。",
    33: "游乐场周：swing, slide, seesaw。🅰 去公园边玩边说\"Push the swing!\"\"Go down the slide!\"🅱 在家用枕头搭\"滑梯\"让玩偶滑下去。🅲 看相关动画片段，指认游乐设施。",
    34: "颜色周B：pink, brown, blue。🅰 在家里找颜色——\"Find something pink!\"\"Blue sky!\"\"Brown bear!\"🅱 用彩色粘土做不同颜色的球。🅲 唱颜色歌曲，拿出对应颜色的物品。",
    35: "动作周B：shake, tap, clap。🅰 \"Shake your body!\"\"Tap your nose!\"\"Clap your hands!\"全部用动作回应。🅱 用沙锤或装豆子的瓶子——\"Let's shake!\"做节奏练习。🅲 拍手游戏——\"Clap once! Clap twice!\"边拍边数。",
    36: "情绪周：happy, sad, angry。🅰 唱If You're Happy完整版，做happy/sad/angry表情。🅱 看情绪闪卡\"Are you happy?\"\"Don't be sad!\"用表情回应。🅲 讲故事时问\"How is the bear? Happy or sad?\"启蒙情商。",
    37: "小动物A：bird, fish, turtle。🅰 看窗外\"Look! A bird!\"养金鱼\"Pretty fish!\"🅱 唱Little Bird/Baby Shark，用动作模仿动物。🅲 用手偶玩角色扮演——小鸟飞、小鱼游、乌龟爬。",
    38: "农场动物A：hen, duck, pig。🅰 学动物叫声\"The duck says quack quack!\"让孩子模仿声音。🅱 唱Old MacDonald Had A Farm，每段一种动物。🅲 用闪卡玩配对游戏——动物和叫声配对。",
    39: "农场动物B：cow, sheep, horse。🅰 \"The cow says moo!\"\"White sheep!\"\"Fast horse!\"边走边学。🅱 用积木搭农场，把动物放进去。🅲 唱Old MacDonald续集，加入cow/sheep/horse。",
    40: "野生动物：tiger, panda, monkey。🅰 通过闪卡和绘本认识！\"Big tiger!\"\"Cute panda!\"\"Funny monkey!\"🅱 看相关动画片段（PP等），指认动物。🅲 模仿动物动作——\"Stomp like a tiger!\"\"Jump like a monkey!\"",
    41: "地点周：park, zoo, farm。🅰 \"Let's go to the park!\"\"See the animals at the zoo!\"去之前先说要去哪里。🅱 看绘本故事，找出park/zoo/farm场景。🅲 玩地图游戏——玩具小车开去不同的地点。",
    42: "职业周：teacher, doctor, baker。🅰 玩角色扮演——\"My teacher says hello!\"\"Doctor, I'm sick!\"\"Baker bakes bread!\"🅱 看相关绘本和动画，指认不同职业。🅲 收集日常生活中的职业元素——听诊器、围裙等。",
    43: "概念周：big, small, house。🅰 \"Big elephant!\"\"Small mouse!\"用夸张手势对比大小。🅱 在家里找大小物品——\"Big chair, small chair!\"\"This is our house!\"🅲 玩大小配对——大小盒子、大小球排序。",
    44: "礼貌用语：good, morning, night。🅰 每天\"Good morning!\"\"Good night!\"养成礼貌习惯。🅱 玩角色扮演——打电话\"Good morning!\"告别\"Goodbye!\"🅲 唱Good Morning Song和Good Night Song，建立作息仪式。",
    45: "自然周：tree, grass, flower。🅰 去公园\"Tall tree!\"\"Green grass!\"\"Pretty flower!\"用五感观察。🅱 收集树叶花瓣做手工——\"This is a tree leaf!\"🅲 唱自然主题歌曲，配合动作。",
    46: "地貌周：hill, river, lake。🅰 看Peppa Pig剧集——Peppa去hills/rivers/lakes的片段。🅱 用沙盘/粘土做hill和river的模型。🅲 唱Row Row Row Your Boat，想象在river上划船。",
    47: "天气周：cloud, rain, snow。🅰 \"White clouds!\"\"Rain rain go away!\"\"Let's play in the snow!\"🅱 做天气观察——每天看窗外\"Is it rainy? Cloudy?\"🅲 唱Rain Rain Go Away和Little Snowflake，配合手指动作。",
    48: "天空周：star, moon, sun。🅰 唱Twinkle Twinkle Little Star！\"Good morning, sun!\"\"Good night, moon!\"🅱 睡前看窗外——\"Can you find the moon?\"\"Where are the stars?\"🅲 S1结业啦！翻看这周的所有闪卡，一起回顾这一年的学习成果！"
}

stats = 0
for phase in data['phases']:
    for week in phase['weeks']:
        n = week['number']
        if n in enriched_tips:
            week['parentTips'] = enriched_tips[n]
            stats += 1

print(f"Enriched {stats} parentTips")

with open('data/curriculum-s1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to data/curriculum-s1.json")
