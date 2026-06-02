"""Restructure curriculum: insert WORD, QUIZ, SPEAKING activities per day."""
import json
import copy

with open('data/curriculum-3yo.json') as f:
    data = json.load(f)

# ─── 1. Add resource library entries ───
existing_ids = {r['id'] for r in data['resourceLibrary']}
NEW_LIB = [
    {
        "id": "word",
        "type": "WORD",
        "name": "单词认读",
        "url": "",
        "description": "核心词汇认读，建立音-义-形连接"
    },
    {
        "id": "quiz",
        "type": "QUIZ",
        "name": "小测验",
        "url": "",
        "description": "简单互动测验，检验理解"
    },
    {
        "id": "speaking",
        "type": "SPEAKING",
        "name": "跟读口语",
        "url": "",
        "description": "引导宝宝开口跟读"
    }
]
added = 0
for entry in NEW_LIB:
    if entry['id'] not in existing_ids:
        data['resourceLibrary'].append(entry)
        added += 1
print(f"Added {added} new library entries")

# ─── 2. Helpers ───
def pick_words(week_kw, day_idx, count=3):
    if not week_kw:
        return []
    start = (day_idx * count) % len(week_kw)
    return [week_kw[(start + i) % len(week_kw)] for i in range(count)]

def word_title(words):
    return "核心词汇：" + "、".join(words) if words else "核心词汇"

def word_desc(words):
    return f"跟着妈妈读单词：{' '.join(words)}" if words else "复习本周核心词汇"

def quiz_desc(song_title, words):
    if words:
        w = words[0]
        return f"『Where is {w}?』——宝宝能指出{w}对应的图片或做出动作吗？"
    return "问宝宝：刚刚的歌/动画里看到了什么？一起来说说吧！"

def speaking_desc(words):
    if words:
        return f"和妈妈一起说：{words[0]}！大声说出来吧～"
    return "和妈妈一起大声说单词吧！"

def review_quiz_desc(week_kw):
    if week_kw:
        return f"『Can you find {week_kw[0]}?』——在闪卡/图片中找一找吧！"
    return "和宝宝一起回顾这周学过的内容吧！"

def review_speaking_desc(week_kw):
    if week_kw:
        return f"大声说出来：{week_kw[0]}！你真棒！"
    return "和妈妈一起回顾这周学过的单词吧！"

# ─── 3. Process days ───
stats = {'input': 0, 'review': 0, 'output': 0}
for p in data['phases']:
    for w in p['weeks']:
        week_kw = w.get('keyWords', [])
        for di, d in enumerate(w['days']):
            acts = d['activities']
            dtype = d['type']

            if dtype == 'input':
                # SSS/song → WORD → YD/video → QUIZ → SPEAKING → PARENT
                new_acts = []
                for ai, a in enumerate(acts):
                    new_acts.append(a)
                    if ai == 0:  # after first (song)
                        words = pick_words(week_kw, di, 2)
                        new_acts.append({
                            "priority": "core",
                            "resourceId": "word",
                            "resourceType": "WORD",
                            "title": word_title(words),
                            "description": word_desc(words),
                            "wordsFocus": words
                        })
                    elif ai == 1:  # after second (video)
                        quiz_words = pick_words(week_kw, di, 1)
                        new_acts.append({
                            "priority": "core",
                            "resourceId": "quiz",
                            "resourceType": "QUIZ",
                            "title": "小测验",
                            "description": quiz_desc(acts[0]['title'], quiz_words),
                            "wordsFocus": quiz_words
                        })
                        spk_words = pick_words(week_kw, di + 2, 1)
                        new_acts.append({
                            "priority": "core",
                            "resourceId": "speaking",
                            "resourceType": "SPEAKING",
                            "title": "跟读练习",
                            "description": speaking_desc(spk_words),
                            "wordsFocus": spk_words
                        })
                d['activities'] = new_acts
                stats['input'] += 1

            elif dtype == 'review':
                # Keep existing, add QUIZ + SPEAKING at end
                quiz_words = pick_words(week_kw, di, 2)
                spk_words = pick_words(week_kw, di + 1, 1)
                d['activities'].extend([
                    {
                        "priority": "core",
                        "resourceId": "quiz",
                        "resourceType": "QUIZ",
                        "title": "复习小测验",
                        "description": review_quiz_desc(quiz_words),
                        "wordsFocus": quiz_words
                    },
                    {
                        "priority": "core",
                        "resourceId": "speaking",
                        "resourceType": "SPEAKING",
                        "title": "复习跟读",
                        "description": review_speaking_desc(spk_words),
                        "wordsFocus": spk_words
                    }
                ])
                stats['review'] += 1

            elif dtype == 'output':
                # Add SPEAKING at beginning, plus review QUIZ
                spk_words = pick_words(week_kw, di, 2)
                d['activities'].insert(0, {
                    "priority": "core",
                    "resourceId": "speaking",
                    "resourceType": "SPEAKING",
                    "title": "口语展示",
                    "description": f"宝宝来展示一下这周学的内容吧！说给妈妈听：{' '.join(spk_words)}",
                    "wordsFocus": spk_words
                })
                quiz_words = pick_words(week_kw, di + 1, 2)
                d['activities'].append({
                    "priority": "core",
                    "resourceId": "quiz",
                    "resourceType": "QUIZ",
                    "title": "综合小测验",
                    "description": review_quiz_desc(quiz_words),
                    "wordsFocus": quiz_words
                })
                stats['output'] += 1

print(f"Processed: input={stats['input']}  review={stats['review']}  output={stats['output']}")

# ─── 4. Save ───
with open('data/curriculum-3yo.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved!")
