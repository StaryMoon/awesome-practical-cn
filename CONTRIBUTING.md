# Contributing

欢迎补充中文实用工具与资源索引。

## 收录标准

- 优先官方入口、官方文档、知名开源仓库和长期稳定的资源页。
- 每个链接必须说明用途。
- 不收盗版、破解、灰产、返利链接和来源不明的安装包。
- 截图优先来自官方公开页面，并保留来源链接。

## 修改方式

主要数据在 `scripts/build_guides.py` 的 `GUIDES` 列表里。修改后运行：

```bash
python3 scripts/build_guides.py
python3 scripts/validate_links.py
```

如果需要更新截图：

```bash
python3 scripts/capture_screenshots.py
```
