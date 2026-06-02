# Curriculum Content Pack Schema

## 核心理念

Curriculum = 内容包。每个包对应一个年龄段（3yo / 4yo / 5yo），整体可替换。
包内结构标准化，引擎层做渲染，不关心具体内容。

```
curriculum-3yo.json
curriculum-4yo.json
curriculum-5yo.json  ← 换文件即可切换
```

## 顶层结构

```
CurriculumPack
 ├── metadata         ← 包的标识、版本、年龄标签
 ├── resourceLibrary  ← 本包用到的全部资源的索引
 └── phases[]         ← 阶段（Phase 1-4）
      └── weeks[]     ← 周
           └── days[] ← 周一至周五（每天 1-3 个活动）
```

## 面向替换的设计要点

| 需求 | 设计方案 |
|------|---------|
| 不同年龄内容不同 | 一个 CurriculumPack = 一个年龄，整体替换 |
| 同一年龄可迭代 | metadata.version 管理版本，metadata.replaces 标识前版本 |
| 资源统一管理 | resourceLibrary 集中管理所有歌曲/视频，每日活动通过 resourceId 引用 |
| 周数可变 | phases[].weeks 长度自由，3岁 24 周 vs 4岁 36 周均可 |
| 每日结构可变 | days[].activities 自由数组，不固定 3 个 |
| 多语言扩展 | vocabulary 中可扩展其他语言字段 |
