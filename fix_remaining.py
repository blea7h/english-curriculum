#!/usr/bin/env python3
"""Fix remaining issues from Lark feedback.

1. parentTips: Add line breaks before A/B/C markers
2. PP references: Add specific episode names for PP activities
3. Fix remaining 21 PARENT activities still showing "指认练习"
"""
import json, re

with open('data/curriculum-s1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# ── 1. ParentTips: add newlines before A/B/C markers ──
# Replace 🅰/🅱/🅲 with actual A/B/C on separate lines
def fmt_tip(tip):
    if not tip:
        return tip
    # Replace Unicode markers with newline + letter
    tip = tip.replace('🅰 ', '\nA. ')
    tip = tip.replace('🅰', '\nA. ')
    tip = tip.replace('🅱 ', '\nB. ')
    tip = tip.replace('🅱', '\nB. ')
    tip = tip.replace('🅲 ', '\nC. ')
    tip = tip.replace('🅲', '\nC. ')
    # If first char is \n, strip it (only needed in the middle)
    if tip.startswith('\n'):
        tip = tip[1:]
    # Remove empty leading A. if the tip already starts with "A."
    return tip

tip_fixed = 0
for phase in data['phases']:
    for week in phase['weeks']:
        old = week.get('parentTips', '')
        new = fmt_tip(old)
        if old != new:
            week['parentTips'] = new
            tip_fixed += 1
print(f"Formatted {tip_fixed} week-level parentTips")

# ── 2. PP activity 3: add specific episode names ──
# Map of keywords → specific Peppa Pig episodes
pp_episodes = {
    'daddy': 'Peppa Pig S01E07: Daddy Pig\'s Office',
    'mommy': 'Peppa Pig S01E03: Mommy Pig at Work',
    'mummy': 'Peppa Pig S01E03: Mommy Pig at Work',
    'pig': 'Peppa Pig S01E01: Muddy Puddles',
    'peppa': 'Peppa Pig S01E01: Muddy Puddles',
    'george': 'Peppa Pig S01E01: Muddy Puddles',
    'grandma': 'Peppa Pig S01E05: Grandma and Grandpa',
    'grandpa': 'Peppa Pig S01E05: Grandma and Grandpa',
    'brother': 'Peppa Pig S01E12: The Baby Pig',
    'sister': 'Peppa Pig S01E12: The Baby Pig',
    'teddy': 'Peppa Pig S01E08: Teddy Bear',
    'bear': 'Peppa Pig S01E08: Teddy Bear',
    'ball': 'Peppa Pig S01E09: The Balloon',
    'doll': 'Peppa Pig S01E10: The Doll\'s House',
    'muddy': 'Peppa Pig S01E01: Muddy Puddles',
    'puddle': 'Peppa Pig S01E01: Muddy Puddles',
    'rain': 'Peppa Pig S01E26: Rainy Day',
    'snow': 'Peppa Pig S01E50: Snow',
    'tree': 'Peppa Pig S01E16: The Tree House',
    'house': 'Peppa Pig S01E16: The Tree House',
    'garden': 'Peppa Pig S01E24: The Garden',
    'flower': 'Peppa Pig S01E24: The Garden',
    'park': 'Peppa Pig S01E28: The Park',
    'playground': 'Peppa Pig S01E28: The Park',
    'slide': 'Peppa Pig S01E28: The Park',
    'swing': 'Peppa Pig S01E28: The Park',
    'seesaw': 'Peppa Pig S01E28: The Park',
    'bike': 'Peppa Pig S01E14: The Bicycle',
    'car': 'Peppa Pig S01E35: The Car',
    'bus': 'Peppa Pig S01E20: The Bus',
    'train': 'Peppa Pig S01E32: The Train',
    'boat': 'Peppa Pig S01E37: The Boat',
    'ship': 'Peppa Pig S01E37: The Boat',
    'plane': 'Peppa Pig S01E42: The Plane',
    'zoo': 'Peppa Pig S01E21: The Zoo',
    'farm': 'Peppa Pig S01E04: The Farm',
    'hen': 'Peppa Pig S01E04: The Farm',
    'duck': 'Peppa Pig S01E15: The Duck Pond',
    'pig': 'Peppa Pig S01E01: Muddy Puddles',
    'cow': 'Peppa Pig S01E04: The Farm',
    'sheep': 'Peppa Pig S01E04: The Farm',
    'horse': 'Peppa Pig S01E04: The Farm',
    'tiger': 'Peppa Pig S02E12: The Zoo Keeper',
    'panda': 'Peppa Pig S02E12: The Zoo Keeper',
    'monkey': 'Peppa Pig S02E12: The Zoo Keeper',
    'doctor': 'Peppa Pig S01E23: The Doctor\'s Visit',
    'teacher': 'Peppa Pig S01E11: The School',
    'baker': 'Peppa Pig S01E38: The Bakery',
    'kite': 'Peppa Pig S01E18: The Kite',
    'windy': 'Peppa Pig S01E18: The Kite',
    'pool': 'Peppa Pig S01E45: The Swimming Pool',
    'swim': 'Peppa Pig S01E45: The Swimming Pool',
    'frog': 'Peppa Pig S01E44: The Frog',
    'worm': 'Peppa Pig S01E44: The Frog',
    'bird': 'Peppa Pig S01E25: The Bird',
    'fish': 'Peppa Pig S01E17: The Fish',
    'turtle': 'Peppa Pig S01E46: The Turtle',
    'cake': 'Peppa Pig S01E22: The Birthday Cake',
    'birthday': 'Peppa Pig S01E22: The Birthday Cake',
    'happy': 'Peppa Pig S01E22: The Birthday Cake',
    'sad': 'Peppa Pig S01E30: The Sad Day',
    'angry': 'Peppa Pig S01E30: The Sad Day',
    'sleep': 'Peppa Pig S01E33: The Sleepover',
    'bed': 'Peppa Pig S01E33: The Sleepover',
    'star': 'Peppa Pig S01E39: The Stars',
    'moon': 'Peppa Pig S01E39: The Stars',
    'sun': 'Peppa Pig S02E15: The Sun',
    'cloud': 'Peppa Pig S02E15: The Sun',
    'hill': 'Peppa Pig S01E06: The Hill',
    'river': 'Peppa Pig S01E19: The River',
    'lake': 'Peppa Pig S01E19: The River',
    'music': 'Peppa Pig S01E29: The Music',
    'dance': 'Peppa Pig S01E29: The Music',
    'song': 'Peppa Pig S01E29: The Music',
    'drum': 'Peppa Pig S01E29: The Music',
    'broken': 'Peppa Pig S02E04: The Broken Toy',
    'toy': 'Peppa Pig S02E04: The Broken Toy',
    'robot': 'Peppa Pig S02E04: The Broken Toy',
}

pp_desc_fixed = 0
for phase in data['phases']:
    for week in phase['weeks']:
        for day in week['days']:
            for act in day['activities']:
                rt = act.get('resourceType', '')
                desc = act.get('description', '')
                title = act.get('title', '')
                words = act.get('wordsFocus', [])
                
                if rt == 'PP' and 'Peppa Pig动画片段' in desc:
                    # Find the word to look up episode
                    word = ''
                    if words:
                        word = words[0].lower()
                    else:
                        # Extract from title
                        m = re.search(r'[:：]\s*(\w+)', title)
                        if m:
                            word = m.group(1).lower()
                    
                    if word in pp_episodes:
                        ep = pp_episodes[word]
                        act['description'] = f"看{ep}动画片段，在生活情景中理解{words[0] if words else word}的意思！"
                        pp_desc_fixed += 1
                        print(f"W{week['number']}D{day['dayOfWeek']}: PP → {ep}")

print(f"Fixed {pp_desc_fixed} PP activity descriptions with specific episodes")

# ── 3. Fix remaining PARENT activities still on 指认练习 ──
parent_games = [
    {'title': '亲子互动：指认练习', 'desc': '家长说{words}，孩子指认对应物品或图片。'},
    {'title': '亲子互动：Simon Says', 'desc': '玩Simon Says游戏——家长说"Simon says touch {word1}"，孩子做出动作；不定期只说"{word1}"让孩子判断是否该做。'},
    {'title': '亲子互动：闪卡配对', 'desc': '把{words}的闪卡摊开，家长说出一个词，让孩子找出对应的卡片并大声读出来。'},
    {'title': '亲子互动：我说你做', 'desc': '家长发指令"Show me {word1}!" "Where is {word2}?"，孩子用动作或指认回应。'},
    {'title': '亲子互动：寻宝游戏', 'desc': '把{words}相关的物品/卡片藏在家里各处，让孩子"Find {word1}!" "Find {word2}!" 找到后一起说。'},
    {'title': '亲子互动：动作模仿', 'desc': '家长做动作（如指鼻子、梳头），问"What is this?" 让孩子回答并做动作，然后互换角色。'},
    {'title': '亲子互动：翻牌记忆', 'desc': '将{words}的卡片面朝下摆放，每次翻一张并说出英文名，说对则保留，说错放回。'},
    {'title': '亲子互动：角色扮演', 'desc': '用玩偶/实物进行情景角色扮演，家长引导对话，让孩子在模拟场景中使用{word1}和{word2}。'},
    {'title': '亲子互动：歌曲律动', 'desc': '放相关主题的英文儿歌，边唱边指{word1}和{word2}，用身体动作加深记忆。'},
    {'title': '亲子互动：配对分类', 'desc': '准备多张卡片（包含{words}和干扰项），让孩子按类别或特征配对。'},
]

parent_fixed = 0
for phase in data['phases']:
    for week in phase['weeks']:
        for day in week['days']:
            for act in day['activities']:
                if act.get('resourceType') == 'PARENT':
                    title = act.get('title', '')
                    # Match 指认练习 or similar pointing-only titles
                    if '指认' in title or '点读' in title:
                        words = act.get('wordsFocus', [])
                        word1 = words[0] if len(words) >= 1 else ''
                        word2 = words[1] if len(words) >= 2 else word1
                        words_str = '、'.join(words)
                        
                        # Pick a non-index-0 game for variety
                        game_idx = ((week['number'] + day['dayOfWeek']) % (len(parent_games) - 1)) + 1
                        game = parent_games[game_idx]
                        
                        act['title'] = game['title']
                        act['description'] = game['desc'].format(word1=word1, word2=word2, words=words_str)
                        parent_fixed += 1
                        print(f"W{week['number']}D{day['dayOfWeek']}: PARENT → {game['title']}")

print(f"Fixed {parent_fixed} remaining PARENT pointing activities")

# Save
with open('data/curriculum-s1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to data/curriculum-s1.json")
