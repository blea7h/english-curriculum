# 本地视频存放目录

把下载的歌曲/视频 `.mp4` 文件放入此目录，然后在 `data/curriculum-*.json` 中对应活动的 `localPath` 字段引用即可。

## 命名约定

```
videos/week01/hello-hello.mp4
videos/week01/hows-the-weather.mp4
videos/week02/head-shoulders-knees-toes.mp4
```

## 使用方法

1. 从 YouTube / 小小优趣 / B站 下载视频（MP4 格式）
2. 放入对应 `videos/week{NN}/` 子目录
3. 在 JSON 活动数据中添加 `"localPath": "videos/weekNN/xxx.mp4"`
4. 刷新页面 → 出现 ▶ 播放按钮 → 点击即播

> 提示：如果文件不存在，浏览器会显示"无法播放"。放好视频文件后自动生效。
