#!/usr/bin/env python3
"""Fix 144 generic activity descriptions in curriculum-s1.json.

Activity 3 of each day (Mon-Wed) has generic descriptions like:
  "通过SSS资源学习nose。"
  
Replace them with meaningful descriptions referencing the actual show/context.
"""
import json, re, copy

with open('data/curriculum-s1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

resource_names = {
    'SSS': 'Super Simple Songs',
    'YD': 'Yakka Dee!',
    'PP': 'Peppa Pig',
    'PF': 'Pinkfong',
    'CC': 'Cocomelon',
    'LF': 'Little Fox',
    'BB': 'Barefoot Books',
    'SS': 'Sesame Street',
    'KF': 'Khan Academy Kids',
}

# Mapping of resourceType to description templates
description_templates = {
    'SSS': [
        "观看Super Simple Songs动画片段，跟着音乐和动作学习{word}的发音。",
        "在SSS经典歌曲中找出{word}，边看边唱边指认，加深印象！",
        "Super Simple Songs动画片段——用欢快的旋律帮宝宝记住{word}。",
    ],
    'PP': [
        "看Peppa Pig动画片段，听听Peppa一家是怎么说{word}的。",
        "和Peppa Pig一起学{word}，在生活情景中理解这个词的意思！",
        "Peppa Pig动画片段——跟着可爱的小猪Peppa学习{word}。",
    ],
    'PF': [
        "跟着Pinkfong的节奏学习{word}，边唱边跳，动起来吧！",
        "Pinkfong动画时间到了！用欢快的歌舞帮宝宝记住{word}。",
        "Pinkfong主题动画，在蹦蹦跳跳中学会{word}。",
    ],
    'CC': [
        "看Cocomelon动画片段，和JJ一起学{word}，跟着唱起来！",
        "Cocomelon动画时间——用熟悉的节奏和画面帮宝宝巩固{word}。",
        "和Cocomelon一起互动，在歌曲中反复听到{word}，自然习得。",
    ],
    'YD': [
        "看Yakka Dee!动画——和Dee一起大声说{word}！",
        "Yakka Dee!时间：跟着Dee和她的朋友们学说{word}。",
        "BBC启蒙动画Yakka Dee!——每集聚焦一个词，帮宝宝自信开口说{word}。",
    ],
    'default': [
        "观看动画片段，重点学习{word}的发音和用法。",
        "动画时间到！在有趣的故事中认识{word}。",
    ],
}

# Game types to rotate through for PARENT activities
parent_games = [
    {
        'title': '亲子互动：指认练习',
        'desc': '家长说{words}，孩子指认对应物品或图片。',
    },
    {
        'title': '亲子互动：Simon Says',
        'desc': '玩Simon Says游戏——家长说"Simon says touch {word1}"，孩子做出动作；不定期只说"{word1}"让孩子判断是否该做。',
    },
    {
        'title': '亲子互动：闪卡配对',
        'desc': '把{words}的闪卡摊开，家长说出一个词，让孩子找出对应的卡片并大声读出来。',
    },
    {
        'title': '亲子互动：我说你做',
        'desc': '家长发指令"Show me {word1}!" "Where is {word2}?"，孩子用动作或指认回应。',
    },
    {
        'title': '亲子互动：寻宝游戏',
        'desc': '把{words}相关的物品/卡片藏在家里各处，让孩子"Find {word1}!" "Find {word2}!" 找到后一起说。',
    },
    {
        'title': '亲子互动：动作模仿',
        'desc': '家长做动作（如指鼻子、梳头），问"What is this?" 让孩子回答，然后互换角色。',
    },
    {
        'title': '亲子互动：翻牌记忆',
        'desc': '将{words}的卡片面朝下摆放，每次翻一张并说出英文名，说对则保留，说错放回。',
    },
]

stats = {'descriptions_fixed': 0, 'parent_enriched': 0}

for phase in data['phases']:
    for week in phase['weeks']:
        for day in week['days']:
            acts = day['activities']
            
            # ── Fix activity 3 (index 2) descriptions ──
            if len(acts) >= 3:
                act3 = acts[2]
                rt = act3.get('resourceType', '')
                # Check if description matches the generic pattern
                desc = act3.get('description', '')
                if re.match(r'^通过(SSS|YD|PP|PF|CC|LF|BB|SS|KF)资源学习[\w\s]+[。.]?$', desc):
                    # Extract the word from title or wordsFocus
                    word = ''
                    if act3.get('wordsFocus') and len(act3['wordsFocus']) > 0:
                        word = act3['wordsFocus'][0]
                    elif act3.get('title'):
                        # Extract from title after ": " or "："
                        m = re.search(r'[:：]\s*(\w+)', act3['title'])
                        if m:
                            word = m.group(1)
                    
                    if word:
                        # Pick template based on resource type
                        templates = description_templates.get(rt, description_templates['default'])
                        # Use week number to rotate through templates for variety
                        idx = (week['number'] + day['dayOfWeek']) % len(templates)
                        new_desc = templates[idx].format(word=word)
                        act3['description'] = new_desc
                        stats['descriptions_fixed'] += 1
                        print(f"W{week['number']}D{day['dayOfWeek']}: [{rt}] {act3['title']} → {new_desc}")
            
            # ── Fix activity 6 (PARENT, index 5) enrichment ──
            if len(acts) >= 6:
                act6 = acts[5]
                if act6.get('resourceType') == 'PARENT' and act6.get('title', '').startswith('亲子互动：指认练习'):
                    words = act6.get('wordsFocus', [])
                    word1 = words[0] if len(words) >= 1 else ''
                    word2 = words[1] if len(words) >= 2 else word1
                    words_str = '、'.join(words)
                    
                    # Pick a game type based on week+day to get variety
                    game_idx = (week['number'] + day['dayOfWeek']) % len(parent_games)
                    game = parent_games[game_idx]
                    
                    new_title = game['title']
                    new_desc = game['desc'].format(word1=word1, word2=word2, words=words_str)
                    
                    act6['title'] = new_title
                    act6['description'] = new_desc
                    stats['parent_enriched'] += 1
                    print(f"W{week['number']}D{day['dayOfWeek']}: PARENT → {new_title}")

print(f"\nDone! Fixed {stats['descriptions_fixed']} descriptions, enriched {stats['parent_enriched']} PARENT activities.")

# Save
with open('data/curriculum-s1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to data/curriculum-s1.json")
