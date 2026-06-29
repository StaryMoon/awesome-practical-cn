#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
OUT_ROOT = ROOT.parent / "Practical_CN_Separate_Repos"
DATA = ROOT / "data" / "guides.json"
SCREENSHOTS = ROOT / "assets" / "screenshots"


REPOS: dict[str, dict[str, object]] = {
    "ai-coding-tools": {
        "repo": "cn-ai-coding-toolbox",
        "title": "中文 AI 编程工具箱",
        "desc": "Codex、Claude Code、Gemini CLI、Cursor、Cline、Aider 等 AI 编程工具的中文选型笔记。",
        "opening": "这几年写代码的工具变化太快了。以前大家争的是补全准不准，现在更麻烦，开始争 agent 能不能读仓库、会不会乱改文件、跑不跑测试、token 钱到底烧到哪里去。这个仓库只留下我觉得中文用户真的会用到的入口。",
        "take": "如果你只是写课程作业，先别急着把所有 agent 都装一遍；如果你已经在维护 repo，那终端 agent 和 Git diff 的配合反而比 IDE 花活更重要。",
        "first": "先从 Codex CLI / Claude Code / Cursor / Cline 四个方向各试一个小任务。",
    },
    "llm-api-platforms": {
        "repo": "cn-llm-api-map",
        "title": "中文 LLM API 入口地图",
        "desc": "常用大模型 API、控制台、聚合平台和模型托管入口的中文整理。",
        "opening": "做 LLM 应用最烦的不是写第一行代码，而是控制台、文档、模型名、价格、额度、地区限制全都散在不同地方。这个仓库就是一张入口地图，少讲概念，多给能点开的地方。",
        "take": "API 平台不要只看模型分数。真正做项目时，账单、限流、日志、地区和 key 管理经常比榜单名次更早把人卡死。",
        "first": "先把 OpenAI、Anthropic、Gemini、DeepSeek 和一个聚合平台的控制台都打开看一遍。",
    },
    "student-dev-perks": {
        "repo": "cn-student-dev-perks",
        "title": "中文学生开发者福利清单",
        "desc": "学生党能申请的 AI、开发、云服务、设计、笔记和域名福利入口。",
        "opening": "学生身份最值钱的时候，很多人反而不知道它能换什么。这个仓库只收官方教育入口和相对稳定的福利页面，不收来路不明的教育邮箱玩法。",
        "take": "先把 GitHub Student Developer Pack 搞定，它相当于学生开发者福利的总开关。云服务免费额度一定要设预算，不然免费两个字会变得很贵。",
        "first": "准备学校邮箱、学生证或学籍证明，然后从 GitHub Education 开始。",
    },
    "research-paper-tools": {
        "repo": "cn-research-paper-toolbox",
        "title": "中文科研论文工具箱",
        "desc": "论文检索、代码检索、文献管理、相关工作扩展和 LaTeX 写作工具整理。",
        "opening": "查文献这件事，最容易变成打开十几个标签页然后忘了自己原本要找什么。这里按真实写论文流程整理：先找种子论文，再扩相关工作，再进 Zotero 管起来。",
        "take": "不要指望一个网站解决全部问题。Google Scholar 找引用，Semantic Scholar 看推荐，Papers with Code 查代码，Zotero 负责最后别乱。",
        "first": "找一篇最核心的种子论文，用 Semantic Scholar 和 Connected Papers 向外扩两圈。",
    },
    "free-books-courses": {
        "repo": "cn-free-books-courses",
        "title": "中文免费编程书与公开课入口",
        "desc": "合法免费的编程书、公开课、大学课程和计算机自学路线整理。",
        "opening": "公开课和电子书最大的问题不是少，而是多到让人误以为收藏就是学习。这个仓库只放合法、稳定、适合长期学习的入口。",
        "take": "课程视频只是入口，作业和项目才是分水岭。一本书、一门课认真做完，比收藏 200 个链接有用。",
        "first": "如果没有路线，先从 CS50 或 CS 自学指南开始，不要同时开太多坑。",
    },
    "design-assets-icons": {
        "repo": "cn-design-assets-map",
        "title": "中文设计素材与图标地图",
        "desc": "README、PPT、论文图、网页和产品 demo 常用图标、模板、图片、动效资源。",
        "opening": "很多项目不是代码差，是第一眼太粗糙。图标不统一、封面像临时截的、README 没有视觉锚点，别人自然不想继续看。这个仓库整理的是能立刻改善第一印象的素材入口。",
        "take": "素材不是越多越好。图标风格统一、配图授权清楚、封面信息准确，比堆十个素材站更重要。",
        "first": "先选一套图标体系，再选一个截图/封面风格，别每页都换审美。",
    },
    "ai-media-tools": {
        "repo": "cn-ai-media-tools",
        "title": "中文 AI 图片视频音频工具清单",
        "desc": "AI 视频、图片、本地生图、语音、音乐和媒体生成工具入口整理。",
        "opening": "AI 媒体工具更新太快，今天还在排队试用，明天就多了一个新模型。这个仓库不追热点新闻，只留下能直接试、能做 demo、能继续跟进的入口。",
        "take": "公开传播前先看授权，尤其是人脸、声音、商业宣传和二创素材。工具能生成，不代表你一定能放心用。",
        "first": "公开视频先试 Runway/Pika/Luma，本地图片工作流先看 ComfyUI。",
    },
    "remote-dev-server": {
        "repo": "cn-remote-dev-handbook",
        "title": "中文远程开发与服务器手册",
        "desc": "SSH、远程编辑、文件同步、隧道、tmux 和跨设备组网工具整理。",
        "opening": "学生服务器、实验室 GPU、远程机器，出问题通常不是大问题，就是 SSH 连不上、端口转不出来、文件传一半断了。这个仓库按排障和日常使用来收工具。",
        "take": "长任务不上 tmux，迟早会吃一次亏。端口裸奔公网，也迟早会吃一次亏。",
        "first": "先把 SSH key、tmux、rsync 三件事弄稳，再考虑花哨的隧道和组网。",
    },
    "macos-productivity": {
        "repo": "cn-macos-productivity",
        "title": "中文 macOS 效率工具清单",
        "desc": "Mac 上常用的包管理、启动器、窗口管理、终端、截图、播放器和容器工具。",
        "opening": "Mac 效率工具很容易装成工具动物园。这个仓库不是为了列全，而是按日常频率保留那些装完真的会每天用的东西。",
        "take": "启动器、窗口管理、终端、截图，这四类先稳定下来，效率提升会比装一堆小菜单栏工具更明显。",
        "first": "Homebrew、Raycast、Rectangle、iTerm2 先装起来，再按需求补 OrbStack 和截图工具。",
    },
    "windows-productivity": {
        "repo": "cn-windows-productivity",
        "title": "中文 Windows 效率与开发工具清单",
        "desc": "Windows 上值得安装的官方效率工具、终端、包管理、WSL、搜索和截图工具。",
        "opening": "Windows 现在已经不是只能凑合写代码的系统了。PowerToys、Terminal、winget、WSL 配好之后，很多开发场景已经足够舒服。",
        "take": "先把微软官方工具链用顺，再装第三方工具。系统层面的热键脚本和清理工具要谨慎。",
        "first": "PowerToys、Windows Terminal、winget、Everything 是最值得先装的一组。",
    },
    "knowledge-management": {
        "repo": "cn-knowledge-workflow",
        "title": "中文知识管理与 Obsidian 工作流",
        "desc": "Obsidian、Logseq、Notion、Zotero、Readwise、Mermaid、Excalidraw 等知识管理工具整理。",
        "opening": "知识管理最容易变成装修软件。目录、标签、双链、模板、插件都很迷人，但最后能留下来的还是每天愿意写进去的那套流程。",
        "take": "别先设计第二大脑，先设计入口：网页怎么进来，论文怎么进来，项目记录怎么进来，每周怎么清一次。",
        "first": "先把 Obsidian/Zotero/Readwise 或同类组合跑通，再考虑插件美化。",
    },
    "pdf-ocr-docs": {
        "repo": "cn-pdf-ocr-toolbox",
        "title": "中文 PDF 与 OCR 工具箱",
        "desc": "PDF 合并拆分、OCR、格式转换、扫描件归档、电子书管理和公式识别工具。",
        "opening": "PDF 工具是那种平时想不起来，真要用时到处找的东西。这个仓库按论文、扫描件、办公文件和批量转换几个场景来收。",
        "take": "敏感文件不要随便上传在线工具。扫描件先 OCR 再归档，后面会少很多痛苦。",
        "first": "日常 PDF 处理看 Stirling PDF / PDF24；批量转换看 Pandoc；文献管理交给 Zotero。",
    },
    "selfhosted-nas": {
        "repo": "cn-selfhosted-nas",
        "title": "中文自托管与 NAS 工具清单",
        "desc": "家庭服务器、NAS、个人云、相册、媒体库、密码库和监控工具整理。",
        "opening": "自托管的乐趣是东西都在自己手里，麻烦也是东西都在自己手里。这个仓库会优先收成熟项目，不鼓励把半成品服务直接暴露公网。",
        "take": "先备份，再折腾。没有备份的 NAS 只是一个看起来很高级的单点故障。",
        "first": "Docker Compose、反向代理、备份策略先准备好，再上 Immich、Jellyfin、Nextcloud。",
    },
    "open-source-alternatives": {
        "repo": "cn-open-source-alternatives",
        "title": "中文开源替代软件清单",
        "desc": "办公、设计、绘画、3D、矢量图、录屏直播等常用商业软件的开源替代入口。",
        "opening": "找开源替代不是为了显得有信仰，而是为了在预算、隐私、可控性之间多一个选择。这个仓库按常见软件类别留入口。",
        "take": "开源替代要试文件兼容和团队协作，不要只看截图。能替代个人流程，不一定能替代团队流程。",
        "first": "先列出你每周都打开的软件，再逐个找替代品试用，不要一次性迁移。",
    },
    "quant-trading-backtest": {
        "repo": "cn-quant-trading-toolbox",
        "title": "中文量化交易与回测工具箱",
        "desc": "开源交易机器人、回测框架、行情数据接口和纸交易工具整理。",
        "opening": "量化工具很容易被包装成赚钱机器，但真正值得先看的永远是回测、手续费、滑点、最大回撤和风控。这个仓库只做工具入口，不做收益承诺。",
        "take": "先纸交易，后小资金；先风控，后策略。截图收益率没有意义，可复现记录才有意义。",
        "first": "加密货币机器人看 Freqtrade，Python 回测看 Backtrader/vectorbt/backtesting.py，中文数据看 AkShare。",
    },
    "data-visualization": {
        "repo": "cn-data-viz-toolbox",
        "title": "中文数据分析与可视化工具箱",
        "desc": "Jupyter、Pandas、Polars、DuckDB、Plotly、ECharts、Streamlit、Superset 等工具整理。",
        "opening": "数据工具不应该只为画一张好看的图服务。真正省时间的是从清洗、分析、查询到展示能连成一条线。",
        "take": "小数据别过度工程化，大数据别硬塞进 Pandas。面向别人展示时，交互和权限会比图表样式更重要。",
        "first": "Notebook 探索，DuckDB/Polars 处理，Plotly/ECharts 展示，Streamlit/Superset 交付。",
    },
    "api-backend-tools": {
        "repo": "cn-api-backend-tools",
        "title": "中文 API 调试与后端工具箱",
        "desc": "API 调试、接口文档、HTTP 命令行、后端框架和 BaaS 工具整理。",
        "opening": "后端项目写到最后，经常不是接口不会写，而是文档、调试、环境和 token 管理混在一起。这个仓库收的是能让接口开发少一点混乱的工具。",
        "take": "API collection 里不要放生产 token。接口文档如果不能跟代码一起更新，很快就会变成考古资料。",
        "first": "调试客户端选 Postman/Bruno/Hoppscotch；Python 快速后端看 FastAPI。",
    },
    "github-project-packaging": {
        "repo": "cn-github-project-polish",
        "title": "中文 GitHub 项目包装手册",
        "desc": "README、badge、release、GitHub Pages、部署、贡献者展示和 star 曲线工具整理。",
        "opening": "很多 GitHub 项目不是没人需要，而是别人点进来 10 秒内看不懂它能干嘛。这个仓库专门收那些能让项目更像正式作品的工具和做法。",
        "take": "README 首屏决定别人要不要继续看。截图、Quick Start、真实示例，比口号和愿景重要得多。",
        "first": "先补 README 首屏、截图、安装命令、示例输出、License，再考虑 Pages 和 badges。",
    },
    "privacy-security": {
        "repo": "cn-privacy-security-toolbox",
        "title": "中文隐私安全与密码管理工具箱",
        "desc": "密码管理、2FA、加密通信、隐私邮箱、泄露查询和文件加密工具整理。",
        "opening": "安全工具不是给极客摆着看的。密码复用、邮箱乱绑、恢复码乱放，这些普通问题比高级攻击更常见。",
        "take": "先把密码管理器和两步验证用起来，胜过收藏一堆隐私工具列表。",
        "first": "Bitwarden/KeePassXC 二选一，重要账号全开 2FA，然后查一次 Have I Been Pwned。",
    },
    "cn-mirrors-downloads": {
        "repo": "cn-mirrors-download-guide",
        "title": "中文开源镜像与下载加速指南",
        "desc": "国内高校镜像站、包管理镜像、conda/pip/npm 加速和常见下载入口整理。",
        "opening": "下载慢这件事太消耗心情了，尤其是配 Python、conda、npm、Linux 源的时候。这个仓库收国内常用镜像和官方配置入口。",
        "take": "镜像是加速，不是魔法。版本异常时先回官方源确认，不要把同步延迟当成包坏了。",
        "first": "优先看清华/中科大/上交/BFSU 镜像帮助页，再配置 pip、conda、npm。",
    },
}


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    index_rows = []
    for guide in payload["guides"]:
        meta = REPOS[guide["slug"]]
        repo_dir = OUT_ROOT / str(meta["repo"])
        build_repo(repo_dir, guide, meta)
        index_rows.append(f"| [{meta['repo']}](https://github.com/StaryMoon/{meta['repo']}) | {meta['title']} | {guide['category']} |")
    (OUT_ROOT / "README.md").write_text(
        "# Practical CN Separate Repos\n\n"
        "20 个从 `awesome-practical-cn` 拆出来的中文信息汇总独立仓库。\n\n"
        "| Repo | 标题 | 分类 |\n| --- | --- | --- |\n"
        + "\n".join(index_rows)
        + "\n",
        encoding="utf-8",
    )
    print(f"generated {len(payload['guides'])} repos under {OUT_ROOT}")


def build_repo(repo_dir: Path, guide: dict, meta: dict) -> None:
    repo_dir.mkdir(parents=True, exist_ok=True)
    assets = repo_dir / "assets"
    data_dir = repo_dir / "data"
    assets.mkdir(exist_ok=True)
    data_dir.mkdir(exist_ok=True)
    source_image = SCREENSHOTS / f"{guide['slug']}.png"
    if source_image.exists():
        shutil.copy2(source_image, assets / "preview.png")
    (data_dir / "links.json").write_text(json.dumps(guide, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (repo_dir / "README.md").write_text(render_readme(guide, meta), encoding="utf-8")
    (repo_dir / "CONTRIBUTING.md").write_text(render_contributing(), encoding="utf-8")
    (repo_dir / "LICENSE").write_text(render_license(), encoding="utf-8")
    (repo_dir / ".gitignore").write_text("__pycache__/\n*.pyc\n.DS_Store\n", encoding="utf-8")


def render_readme(guide: dict, meta: dict) -> str:
    rows = "\n".join(f"| [{name}]({url}) | {desc} |" for name, url, desc in guide["entries"])
    quick = "\n".join(f"- {item}" for item in guide["quick_start"])
    pitfalls = "\n".join(f"- {item}" for item in guide["pitfalls"])
    names = " / ".join(item[0] for item in guide["entries"][:4])
    return f"""# {meta['title']}

![preview](assets/preview.png)

{meta['opening']}

{meta['take']}

## 先看这几个

{names}

{meta['first']}

## 入口

| 名称 | 我为什么留它 |
| --- | --- |
{rows}

## 我的使用顺序

{quick}

## 别踩坑

{pitfalls}

## 截图来源

这张图来自公开页面：[{guide['hero_url']}]({guide['hero_url']})。如果页面改版，截图可能会和当前官网略有出入。

## 维护方式

链接数据放在 [`data/links.json`](data/links.json)。我倾向于少而准：入口失效就换，说明过时就改，不把这里做成什么都往里塞的大杂烩。

## License

MIT. 第三方商标、页面截图和网站内容归原权利方所有；本仓库只做中文导航和使用笔记。
"""


def render_contributing() -> str:
    return """# Contributing

欢迎补链接，但希望按这几个标准来：

- 优先官方入口、官方文档、稳定开源仓库。
- 每个链接都写一句它解决什么问题。
- 不放盗版、破解、返利、网盘搬运和来源不明的安装包。
- 截图只用公开页面，别截付费课、私密页面和需要登录的信息。
"""


def render_license() -> str:
    return dedent(
        """\
        MIT License

        Copyright (c) 2026 Minghao Liu

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
    )


if __name__ == "__main__":
    main()
