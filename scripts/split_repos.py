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
    },
    "llm-api-platforms": {
        "repo": "cn-llm-api-map",
        "title": "中文 LLM API 入口地图",
        "desc": "常用大模型 API、控制台、聚合平台和模型托管入口的中文整理。",
    },
    "student-dev-perks": {
        "repo": "cn-student-dev-perks",
        "title": "中文学生开发者福利清单",
        "desc": "学生开发者可申请的 AI、开发、云服务、设计、笔记和域名福利入口。",
    },
    "research-paper-tools": {
        "repo": "cn-research-paper-toolbox",
        "title": "中文科研论文工具箱",
        "desc": "论文检索、代码检索、文献管理、相关工作扩展和 LaTeX 写作工具整理。",
    },
    "free-books-courses": {
        "repo": "cn-free-books-courses",
        "title": "中文免费编程书与公开课入口",
        "desc": "合法免费的编程书、公开课、大学课程和计算机自学路线整理。",
    },
    "design-assets-icons": {
        "repo": "cn-design-assets-map",
        "title": "中文设计素材与图标地图",
        "desc": "README、PPT、论文图、网页和产品 demo 常用图标、模板、图片、动效资源。",
    },
    "ai-media-tools": {
        "repo": "cn-ai-media-tools",
        "title": "中文 AI 图片视频音频工具清单",
        "desc": "AI 视频、图片、本地生图、语音、音乐和媒体生成工具入口整理。",
    },
    "remote-dev-server": {
        "repo": "cn-remote-dev-handbook",
        "title": "中文远程开发与服务器手册",
        "desc": "SSH、远程编辑、文件同步、隧道、tmux 和跨设备组网工具整理。",
    },
    "macos-productivity": {
        "repo": "cn-macos-productivity",
        "title": "中文 macOS 效率工具清单",
        "desc": "Mac 上常用的包管理、启动器、窗口管理、终端、截图、播放器和容器工具。",
    },
    "windows-productivity": {
        "repo": "cn-windows-productivity",
        "title": "中文 Windows 效率与开发工具清单",
        "desc": "Windows 上值得安装的官方效率工具、终端、包管理、WSL、搜索和截图工具。",
    },
    "knowledge-management": {
        "repo": "cn-knowledge-workflow",
        "title": "中文知识管理与 Obsidian 工作流",
        "desc": "Obsidian、Logseq、Notion、Zotero、Readwise、Mermaid、Excalidraw 等知识管理工具整理。",
    },
    "pdf-ocr-docs": {
        "repo": "cn-pdf-ocr-toolbox",
        "title": "中文 PDF 与 OCR 工具箱",
        "desc": "PDF 合并拆分、OCR、格式转换、扫描件归档、电子书管理和公式识别工具。",
    },
    "selfhosted-nas": {
        "repo": "cn-selfhosted-nas",
        "title": "中文自托管与 NAS 工具清单",
        "desc": "家庭服务器、NAS、个人云、相册、媒体库、密码库和监控工具整理。",
    },
    "open-source-alternatives": {
        "repo": "cn-open-source-alternatives",
        "title": "中文开源替代软件清单",
        "desc": "办公、设计、绘画、3D、矢量图、录屏直播等常用商业软件的开源替代入口。",
    },
    "quant-trading-backtest": {
        "repo": "cn-quant-trading-toolbox",
        "title": "中文量化交易与回测工具箱",
        "desc": "开源交易机器人、回测框架、行情数据接口和纸交易工具整理。",
    },
    "data-visualization": {
        "repo": "cn-data-viz-toolbox",
        "title": "中文数据分析与可视化工具箱",
        "desc": "Jupyter、Pandas、Polars、DuckDB、Plotly、ECharts、Streamlit、Superset 等工具整理。",
    },
    "api-backend-tools": {
        "repo": "cn-api-backend-tools",
        "title": "中文 API 调试与后端工具箱",
        "desc": "API 调试、接口文档、HTTP 命令行、后端框架和 BaaS 工具整理。",
    },
    "github-project-packaging": {
        "repo": "cn-github-project-polish",
        "title": "中文 GitHub 项目包装手册",
        "desc": "README、badge、release、GitHub Pages、部署、贡献者展示和 star 曲线工具整理。",
    },
    "privacy-security": {
        "repo": "cn-privacy-security-toolbox",
        "title": "中文隐私安全与密码管理工具箱",
        "desc": "密码管理、2FA、加密通信、隐私邮箱、泄露查询和文件加密工具整理。",
    },
    "cn-mirrors-downloads": {
        "repo": "cn-mirrors-download-guide",
        "title": "中文开源镜像与下载加速指南",
        "desc": "国内高校镜像站、包管理镜像、conda/pip/npm 加速和常见下载入口整理。",
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
        "Index of 20 focused Chinese resource repositories generated from `awesome-practical-cn`.\n\n"
        "| Repo | Title | Category |\n| --- | --- | --- |\n"
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
    quick = "\n".join(f"{idx}. {item}" for idx, item in enumerate(guide["quick_start"], start=1))
    pitfalls = "\n".join(f"- {item}" for item in guide["pitfalls"])
    names = " / ".join(item[0] for item in guide["entries"][:4])
    return f"""# {meta['title']}

> {meta['desc']}

![preview](assets/preview.png)

## Overview

{guide['summary']}

本仓库只保留与主题直接相关、入口稳定、说明清晰的资源。优先收录官方文档、主流开源仓库、长期可访问的产品页面和常用工具链。

## Key Resources

{names}

## Resources

| Resource | Use case |
| --- | --- |
{rows}

## Recommended Path

{quick}

## Notes

{pitfalls}

## Screenshot

Source: [{guide['hero_url']}]({guide['hero_url']})

## Data

Structured resource data is available in [`data/links.json`](data/links.json).

## Contributing

PRs are welcome for official links, documentation updates, screenshot refreshes, and concise use-case descriptions. Please avoid mirrors, cracked software, referral links, and unverified downloads.

## License

MIT. Third-party trademarks, screenshots, and website content belong to their respective owners.
"""


def render_contributing() -> str:
    return """# Contributing

欢迎提交资源补充、链接修复和说明更新。

## Scope

- 优先官方入口、官方文档、稳定开源仓库和长期可访问的资源页。
- 每个链接必须包含清晰的使用场景。
- 不收录盗版资源、破解软件、返利链接、网盘搬运和来源不明的安装包。
- 截图必须来自公开页面，不使用付费课程、私密页面或登录后内容。

## Checklist

- 确认链接可访问。
- 确认说明简洁、具体、无营销语。
- 确认新增资源与本仓库主题直接相关。
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
