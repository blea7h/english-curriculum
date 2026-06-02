# English Curriculum App

## Quick Start

```bash
# Option 1: Python
python3 -m http.server 8080 --directory /root/english-curriculum-app
# → http://localhost:8080

# Option 2: Node
npx serve /root/english-curriculum-app
```

## Project Structure

```
english-curriculum-app/
├── index.html              ← 单页 Web App（零依赖）
├── data/
│   ├── schema.md           ← 数据层设计文档
│   └── curriculum-3yo.json ← 3岁内容包（24周）
└── README.md
```

## Content Pack 替换方式

```js
// 未来加入 4岁、5岁内容包后，在 index.html 的 select 中：
data/curriculum-4yo.json
data/curriculum-5yo.json
```

每个内容包独立 JSON 文件，结构相同，App 自动渲染。
