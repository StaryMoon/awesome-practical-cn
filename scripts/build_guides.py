#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "guides.json"
GUIDES_DIR = ROOT / "docs" / "guides"
ASSETS = ROOT / "assets"
SCREENSHOTS = ASSETS / "screenshots"


GUIDES = [
    {
        "title": "AI 编程工具中文选型",
        "slug": "ai-coding-tools",
        "category": "AI / 编程",
        "audience": "学生、研究生、开发者、开源维护者",
        "hero_url": "https://github.com/openai/codex",
        "summary": "把 Codex、Claude Code、Gemini CLI、Cursor、Cline、Aider、Continue 等工具按工作流重新分类，帮助中文用户快速判断该装什么、该避开什么。",
        "why_hot": "AI coding 工具正在从补全走向 agent，中文资料常常只讲情绪不讲选型，这类页面很适合被搜索和收藏。",
        "entries": [
            ["OpenAI Codex CLI", "https://github.com/openai/codex", "终端 coding agent，适合本地仓库修改、测试、PR 小修。"],
            ["Claude Code", "https://docs.anthropic.com/en/docs/claude-code/overview", "Claude 生态 coding agent，适合长上下文和复杂任务拆解。"],
            ["Gemini CLI", "https://github.com/google-gemini/gemini-cli", "Google Gemini 生态终端 agent，开源且热度高。"],
            ["Cursor", "https://cursor.com/", "AI-first editor，适合想要开箱即用 IDE 体验的人。"],
            ["Cline", "https://github.com/cline/cline", "VS Code 内开源 autonomous coding agent。"],
            ["Aider", "https://github.com/Aider-AI/aider", "Git/diff 驱动的经典终端 AI pair programmer。"],
            ["Continue", "https://github.com/continuedev/continue", "开源 AI coding assistant 平台，适合团队自定义。"],
            ["Qwen Code", "https://github.com/QwenLM/qwen-code", "Qwen 生态终端 coding agent，中文用户值得关注。"],
        ],
        "quick_start": ["先选一种工作流：终端 agent、AI IDE、VS Code 插件。", "小仓库试用：让工具读 README、修 bug、跑测试。", "确认成本和权限后再交给它改大仓库。"],
        "pitfalls": ["不要把生产密钥交给 agent。", "不要只看 star，要看是否适合你的编辑器和模型生态。"],
    },
    {
        "title": "LLM API 与模型平台入口",
        "slug": "llm-api-platforms",
        "category": "AI / API",
        "audience": "做 AI 应用、机器人、Agent、论文实验的人",
        "hero_url": "https://openrouter.ai/",
        "summary": "整理常用大模型 API 平台、聚合平台和模型托管入口，方便快速比较模型、文档、控制台和定价入口。",
        "why_hot": "LLM 应用开发最容易卡在账号、额度、模型入口和文档分散，这种导航页天然适合收藏。",
        "entries": [
            ["OpenAI Platform", "https://platform.openai.com/docs/overview", "OpenAI API 文档和控制台入口。"],
            ["Anthropic Console", "https://console.anthropic.com/", "Claude API 控制台入口。"],
            ["Google AI Studio", "https://aistudio.google.com/", "Gemini API 原型和 key 管理入口。"],
            ["DeepSeek Platform", "https://platform.deepseek.com/", "DeepSeek API 平台入口。"],
            ["阿里云百炼 DashScope", "https://bailian.console.aliyun.com/", "通义千问等模型调用与应用开发平台。"],
            ["OpenRouter", "https://openrouter.ai/", "多模型聚合平台，适合快速切换 provider。"],
            ["Hugging Face Models", "https://huggingface.co/models", "模型权重、demo、社区模型搜索入口。"],
            ["Replicate", "https://replicate.com/", "托管模型 API 和 demo 平台。"],
        ],
        "quick_start": ["先确定模型用途：文本、代码、视觉、语音或 embedding。", "把控制台、定价页、API 文档一起收藏。", "先写最小 demo，再接入生产。"],
        "pitfalls": ["不要忽视地区、支付方式、速率限制。", "聚合平台方便，但生产场景要评估稳定性和隐私。"],
    },
    {
        "title": "学生党 AI 与开发者福利",
        "slug": "student-dev-perks",
        "category": "学生 / 福利",
        "audience": "本科生、研究生、刚开始做项目的学生",
        "hero_url": "https://github.com/github-education-resources",
        "summary": "整理学生身份可申请的开发工具、云服务、设计工具、笔记工具和教育优惠入口。",
        "why_hot": "学生福利长期有搜索需求，且很多入口分散、资格规则变化快，中文总表非常容易被转发。",
        "entries": [
            ["GitHub Student Developer Pack", "https://education.github.com/pack", "学生开发者福利总入口。"],
            ["GitHub Education", "https://education.github.com/", "GitHub 教育认证与校园资源。"],
            ["JetBrains for Students", "https://www.jetbrains.com/community/education/#students", "JetBrains 全家桶学生授权。"],
            ["Azure for Students", "https://azure.microsoft.com/en-us/free/students", "微软学生云资源。"],
            ["Notion for Education", "https://www.notion.so/product/notion-for-education", "Notion 学生教育计划。"],
            ["Figma Education", "https://www.figma.com/education/", "Figma 教育计划。"],
            ["Canva Education", "https://www.canva.com/education/", "Canva 教育资源。"],
            ["Namecheap Education", "https://nc.me/", "学生域名相关优惠入口。"],
        ],
        "quick_start": ["准备学校邮箱、学生证或学信/学校证明。", "先申请 GitHub Student Pack，因为它会解锁一串开发工具。", "记录每个福利的续期时间。"],
        "pitfalls": ["不要用来路不明的教育邮箱。", "免费额度也可能产生付费账单，云服务一定要设预算告警。"],
    },
    {
        "title": "科研论文检索与阅读工具",
        "slug": "research-paper-tools",
        "category": "科研 / 论文",
        "audience": "研究生、科研党、写综述和开题的人",
        "hero_url": "https://www.semanticscholar.org/",
        "summary": "把论文检索、引用管理、相关工作扩展、代码检索、LaTeX 写作和 AI 阅读工具放在一张表里。",
        "why_hot": "科研工具总是碎片化，导师只说去查文献，但不会告诉你工具链怎么搭。",
        "entries": [
            ["Google Scholar", "https://scholar.google.com/", "经典学术搜索和引用入口。"],
            ["Semantic Scholar", "https://www.semanticscholar.org/", "带推荐和 TLDR 的学术搜索。"],
            ["arXiv", "https://arxiv.org/", "预印本论文入口。"],
            ["Papers with Code", "https://paperswithcode.com/", "论文、代码、榜单三合一。"],
            ["Zotero", "https://www.zotero.org/", "开源文献管理工具。"],
            ["Connected Papers", "https://www.connectedpapers.com/", "根据论文扩展相关工作图谱。"],
            ["ResearchRabbit", "https://www.researchrabbit.ai/", "论文推荐和文献网络。"],
            ["Overleaf", "https://www.overleaf.com/", "在线 LaTeX 协作写作。"],
        ],
        "quick_start": ["先用 Semantic Scholar/Papers with Code 找种子论文。", "用 Connected Papers 扩展相关工作。", "全部进 Zotero，再用标签和笔记管理。"],
        "pitfalls": ["不要只看引用数，高引用老论文和最新强相关论文都要看。", "AI 摘要不能替代读方法和实验设置。"],
    },
    {
        "title": "免费电子书与公开课程",
        "slug": "free-books-courses",
        "category": "学习 / 课程",
        "audience": "自学编程、数学、AI、计算机基础的人",
        "hero_url": "https://github.com/EbookFoundation/free-programming-books",
        "summary": "整理合法免费的编程书、公开课、大学课程和自学路线，避免被盗版资源和低质课浪费时间。",
        "why_hot": "电子书和课程资源是 GitHub 上最容易爆的题材之一，长期有搜索需求。",
        "entries": [
            ["free-programming-books", "https://github.com/EbookFoundation/free-programming-books", "GitHub 超高星免费编程书列表。"],
            ["MIT OpenCourseWare", "https://ocw.mit.edu/", "MIT 官方公开课程。"],
            ["CS50", "https://cs50.harvard.edu/", "哈佛 CS50 系列课程。"],
            ["CS 自学指南", "https://csdiy.wiki/", "中文计算机自学路线。"],
            ["OpenStax", "https://openstax.org/", "开放教材平台。"],
            ["Stanford Online", "https://online.stanford.edu/free-courses", "斯坦福免费课程入口。"],
            ["Khan Academy", "https://www.khanacademy.org/", "数学和基础学科学习。"],
            ["edX", "https://www.edx.org/", "大学和机构在线课程平台。"],
        ],
        "quick_start": ["先选一条路线，不要同时收藏 200 门课。", "课程配套作业比视频更重要。", "用 GitHub README 记录已完成章节。"],
        "pitfalls": ["不要把收藏当学习。", "不要下载侵权盗版包，官方公开课已经足够多。"],
    },
    {
        "title": "设计素材、图标与配图资源",
        "slug": "design-assets-icons",
        "category": "设计 / 素材",
        "audience": "做 README、论文图、PPT、网页和产品 demo 的人",
        "hero_url": "https://github.com/tailwindlabs/heroicons",
        "summary": "整理图标、插图、字体、图片、动效和设计模板入口，强调授权和可商用边界。",
        "why_hot": "很多项目 README 差在视觉第一眼，这类资源贴能立刻提升开源项目质感。",
        "entries": [
            ["Figma Templates", "https://www.figma.com/templates/", "Figma 官方模板入口。"],
            ["Material Symbols", "https://fonts.google.com/icons", "Google 官方图标库。"],
            ["Iconify", "https://iconify.design/", "统一搜索海量开源图标。"],
            ["Lucide", "https://lucide.dev/", "简洁线性图标库。"],
            ["Heroicons", "https://heroicons.com/", "Tailwind 团队图标。"],
            ["Unsplash", "https://unsplash.com/", "免费摄影图片。"],
            ["Pexels", "https://www.pexels.com/", "免费图片和视频素材。"],
            ["LottieFiles", "https://lottiefiles.com/", "Lottie 动效素材和工具。"],
        ],
        "quick_start": ["README 首屏先做一张清晰封面图。", "图标统一风格，不要混用太多体系。", "每次使用素材都检查 license。"],
        "pitfalls": ["不要默认网上图片都可商用。", "不要在论文或商业项目里使用来源不明素材。"],
    },
    {
        "title": "AI 图片、视频与音频生成工具",
        "slug": "ai-media-tools",
        "category": "AI / 生成",
        "audience": "做短视频、演示图、产品宣传、视觉实验的人",
        "hero_url": "https://runwayml.com/",
        "summary": "整理主流 AI 生成媒体工具：视频、图片、音乐、语音和本地工作流。",
        "why_hot": "AI 生成内容天然有传播性，工具变化快，中文整理贴有持续更新价值。",
        "entries": [
            ["Runway", "https://runwayml.com/", "AI 视频生成和编辑平台。"],
            ["Pika", "https://pika.art/", "AI 视频生成平台。"],
            ["Luma Dream Machine", "https://lumalabs.ai/dream-machine", "视频生成模型入口。"],
            ["Kling AI", "https://klingai.com/", "视频生成工具。"],
            ["ComfyUI", "https://github.com/comfyanonymous/ComfyUI", "节点式本地 Stable Diffusion 工作流。"],
            ["AUTOMATIC1111", "https://github.com/AUTOMATIC1111/stable-diffusion-webui", "经典 Stable Diffusion WebUI。"],
            ["ElevenLabs", "https://elevenlabs.io/", "AI 语音生成。"],
            ["Suno", "https://suno.com/", "AI 音乐生成。"],
        ],
        "quick_start": ["商业项目先查授权。", "本地生成优先试 ComfyUI 工作流。", "视频工具先用免费额度做风格验证。"],
        "pitfalls": ["不要上传敏感人脸和未授权素材。", "AI 生成内容用于公开传播时要注意平台规则。"],
    },
    {
        "title": "远程开发、服务器与内网穿透",
        "slug": "remote-dev-server",
        "category": "开发 / 服务器",
        "audience": "学生服务器、实验室 GPU、远程办公和个人服务部署用户",
        "hero_url": "https://tailscale.com/",
        "summary": "整理 SSH、远程编辑、文件同步、隧道、终端复用和跨设备组网工具。",
        "why_hot": "学生党最常见痛点是连不上服务器、传文件慢、端口转发乱，这类工具贴很实用。",
        "entries": [
            ["VS Code Remote SSH", "https://code.visualstudio.com/docs/remote/ssh", "VS Code 远程开发官方文档。"],
            ["Tailscale", "https://tailscale.com/", "基于 WireGuard 的组网工具。"],
            ["Cloudflare Tunnel", "https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/", "无需公网 IP 的隧道方案。"],
            ["ngrok", "https://ngrok.com/", "本地服务公网暴露工具。"],
            ["tmux", "https://github.com/tmux/tmux", "终端会话复用。"],
            ["mosh", "https://mosh.org/", "弱网下更稳的远程 shell。"],
            ["rsync", "https://rsync.samba.org/", "增量文件同步。"],
            ["rclone", "https://rclone.org/", "云盘和远程存储同步工具。"],
        ],
        "quick_start": ["先保证 SSH key 登录稳定。", "长任务必须用 tmux。", "跨网络访问优先考虑 Tailscale 或 Cloudflare Tunnel。"],
        "pitfalls": ["不要把端口裸奔到公网。", "不要把私钥上传到服务器或网盘。"],
    },
    {
        "title": "macOS 效率工具清单",
        "slug": "macos-productivity",
        "category": "macOS / 效率",
        "audience": "Mac 用户、学生、开发者、研究生",
        "hero_url": "https://www.raycast.com/",
        "summary": "整理 Mac 上最常用的启动器、窗口管理、包管理、终端、截图、播放器和虚拟化工具。",
        "why_hot": "macOS 效率工具是 GitHub 和中文社区长期热门题材，适合做成可持续更新榜单。",
        "entries": [
            ["Homebrew", "https://brew.sh/", "macOS 包管理器。"],
            ["Raycast", "https://www.raycast.com/", "启动器、快捷命令和 AI 工作流。"],
            ["Rectangle", "https://rectangleapp.com/", "开源窗口管理。"],
            ["AltTab", "https://alt-tab-macos.netlify.app/", "Windows 风格窗口切换。"],
            ["iTerm2", "https://iterm2.com/", "经典终端模拟器。"],
            ["OrbStack", "https://orbstack.dev/", "轻量 Docker/Linux 虚拟化工具。"],
            ["Shottr", "https://shottr.cc/", "截图和标注工具。"],
            ["IINA", "https://iina.io/", "现代 macOS 视频播放器。"],
        ],
        "quick_start": ["先装 Homebrew，再装窗口管理和终端工具。", "启动器只选一个主力，不要 Raycast/Alfred 混乱使用。", "开发者优先配置终端和容器环境。"],
        "pitfalls": ["不要安装来源不明的破解工具。", "权限类工具要注意辅助功能和屏幕录制权限。"],
    },
    {
        "title": "Windows 效率与开发工具",
        "slug": "windows-productivity",
        "category": "Windows / 效率",
        "audience": "Windows 用户、学生、开发者",
        "hero_url": "https://github.com/microsoft/PowerToys",
        "summary": "整理 Windows 上最值得安装的官方工具、终端、包管理、搜索、截图、剪贴板和磁盘分析工具。",
        "why_hot": "Windows 用户体量巨大，工具清单只要靠谱就很容易被收藏。",
        "entries": [
            ["Microsoft PowerToys", "https://learn.microsoft.com/en-us/windows/powertoys/", "微软官方效率工具合集。"],
            ["Windows Terminal", "https://github.com/microsoft/terminal", "现代 Windows 终端。"],
            ["winget", "https://learn.microsoft.com/en-us/windows/package-manager/winget/", "Windows 官方包管理器。"],
            ["WSL", "https://learn.microsoft.com/en-us/windows/wsl/", "Windows Subsystem for Linux。"],
            ["AutoHotkey", "https://www.autohotkey.com/", "自动化热键脚本。"],
            ["Everything", "https://www.voidtools.com/", "极速文件搜索。"],
            ["ShareX", "https://getsharex.com/", "截图录屏和上传工具。"],
            ["WizTree", "https://diskanalyzer.com/", "磁盘空间分析工具。"],
        ],
        "quick_start": ["先装 PowerToys、Windows Terminal、winget。", "开发者再配置 WSL。", "文件搜索和截图工具能立刻提升效率。"],
        "pitfalls": ["不要随便运行网上下载的 AHK 脚本。", "清理磁盘前先确认不是项目数据或缓存索引。"],
    },
    {
        "title": "知识管理与 Obsidian 工作流",
        "slug": "knowledge-management",
        "category": "知识管理",
        "audience": "写论文、记笔记、做项目复盘的人",
        "hero_url": "https://obsidian.md/",
        "summary": "整理 Markdown 笔记、双链、文献管理、稍后读、白板、图表和自动化工具。",
        "why_hot": "Obsidian/Notion/Logseq 用户都有强烈迁移、插件、模板需求，中文资料天然有流量。",
        "entries": [
            ["Obsidian", "https://obsidian.md/", "本地 Markdown 知识库。"],
            ["Logseq", "https://logseq.com/", "开源大纲式知识管理。"],
            ["Notion", "https://www.notion.so/", "在线协作文档和数据库。"],
            ["Anytype", "https://anytype.io/", "本地优先对象式知识管理。"],
            ["Readwise Reader", "https://readwise.io/read", "稍后读和高亮管理。"],
            ["Zotero", "https://www.zotero.org/", "文献管理。"],
            ["Mermaid", "https://mermaid.js.org/", "文本生成流程图。"],
            ["Excalidraw", "https://excalidraw.com/", "手绘风白板。"],
        ],
        "quick_start": ["先确定信息入口：网页、论文、日记、项目。", "使用统一目录和模板，不要一开始沉迷插件。", "每周做一次整理和归档。"],
        "pitfalls": ["知识库最大敌人是过度设计。", "云同步前要想清楚隐私和备份。"],
    },
    {
        "title": "PDF、OCR 与文档处理工具",
        "slug": "pdf-ocr-docs",
        "category": "文档 / OCR",
        "audience": "处理论文、扫描件、合同、电子书和课件的人",
        "hero_url": "https://github.com/Stirling-Tools/Stirling-PDF",
        "summary": "整理 PDF 合并拆分、OCR、格式转换、电子书管理、扫描件归档和数学公式识别工具。",
        "why_hot": "PDF 是学生和办公人群最高频痛点之一，好用工具贴长期有收藏价值。",
        "entries": [
            ["Stirling PDF", "https://github.com/Stirling-Tools/Stirling-PDF", "可自托管的 PDF 工具箱。"],
            ["PDF24", "https://www.pdf24.org/en/", "在线/桌面 PDF 工具。"],
            ["OCRmyPDF", "https://ocrmypdf.readthedocs.io/", "给扫描 PDF 加 OCR 文本层。"],
            ["Tesseract OCR", "https://github.com/tesseract-ocr/tesseract", "开源 OCR 引擎。"],
            ["Paperless-ngx", "https://github.com/paperless-ngx/paperless-ngx", "文档归档和 OCR 管理。"],
            ["Pandoc", "https://pandoc.org/", "文档格式转换瑞士军刀。"],
            ["Calibre", "https://calibre-ebook.com/", "电子书管理和转换。"],
            ["Mathpix", "https://mathpix.com/", "公式和文档 OCR。"],
        ],
        "quick_start": ["扫描件先 OCR，再归档。", "论文 PDF 用 Zotero 管理，办公 PDF 用 Stirling/PDF24。", "大批量转换优先 Pandoc 或脚本。"],
        "pitfalls": ["敏感文件不要上传到未知在线工具。", "OCR 结果必须人工核对。"],
    },
    {
        "title": "自托管服务与 NAS 工具",
        "slug": "selfhosted-nas",
        "category": "自托管 / NAS",
        "audience": "想搭家庭服务器、NAS、个人云和内网服务的人",
        "hero_url": "https://github.com/awesome-selfhosted/awesome-selfhosted",
        "summary": "整理自托管入口、Docker 管理、相册、影音、网盘、密码库、Git 服务和监控工具。",
        "why_hot": "自托管和 NAS 是高收藏属性主题，适合从入门到项目清单持续更新。",
        "entries": [
            ["awesome-selfhosted", "https://github.com/awesome-selfhosted/awesome-selfhosted", "自托管项目大列表。"],
            ["Docker", "https://www.docker.com/", "容器基础设施。"],
            ["CasaOS", "https://casaos.io/", "家庭云系统。"],
            ["Immich", "https://github.com/immich-app/immich", "自托管相册。"],
            ["Jellyfin", "https://jellyfin.org/", "自托管媒体服务器。"],
            ["Nextcloud", "https://nextcloud.com/", "个人云盘和协作平台。"],
            ["Vaultwarden", "https://github.com/dani-garcia/vaultwarden", "轻量 Bitwarden 兼容服务。"],
            ["Uptime Kuma", "https://github.com/louislam/uptime-kuma", "自托管监控面板。"],
        ],
        "quick_start": ["先用 Docker Compose 管理服务。", "所有外网暴露服务都要有 HTTPS 和强密码。", "先搭备份，再搭相册和网盘。"],
        "pitfalls": ["不要把管理面板直接暴露公网。", "家庭 NAS 最大风险不是部署失败，而是硬盘坏了没备份。"],
    },
    {
        "title": "开源替代软件清单",
        "slug": "open-source-alternatives",
        "category": "开源 / 替代",
        "audience": "想找免费、开源、跨平台软件的人",
        "hero_url": "https://github.com/obsproject/obs-studio",
        "summary": "整理常见商业软件的开源替代入口，以及图片、视频、音频、办公和直播工具。",
        "why_hot": "开源替代是 GitHub 上非常吃香的主题，搜索意图明确，用户愿意 star 保存。",
        "entries": [
            ["Open Source Alternative To", "https://www.opensourcealternative.to/", "按商业产品找开源替代。"],
            ["AlternativeTo", "https://alternativeto.net/", "软件替代搜索。"],
            ["LibreOffice", "https://www.libreoffice.org/", "开源办公套件。"],
            ["GIMP", "https://www.gimp.org/", "图像编辑。"],
            ["Krita", "https://krita.org/", "绘画和数字艺术。"],
            ["Blender", "https://www.blender.org/", "3D 创作套件。"],
            ["Inkscape", "https://inkscape.org/", "矢量图编辑。"],
            ["OBS Studio", "https://obsproject.com/", "录屏和直播。"],
        ],
        "quick_start": ["先列出你正在用的付费工具。", "逐个找开源替代并试用一周。", "确认文件格式兼容后再迁移。"],
        "pitfalls": ["开源不等于免费商用无条件，仍要看 license。", "不要为了开源而牺牲关键工作流稳定性。"],
    },
    {
        "title": "量化交易、回测与行情数据",
        "slug": "quant-trading-backtest",
        "category": "金融 / 量化",
        "audience": "想做量化机器人、回测、纸交易和数据分析的人",
        "hero_url": "https://github.com/freqtrade/freqtrade",
        "summary": "整理开源交易机器人、回测框架、行情接口和 A 股/加密数据工具，强调风控和纸交易。",
        "why_hot": "量化赚钱叙事很容易吸引关注，但高质量项目必须把风险和回测讲清楚。",
        "entries": [
            ["Freqtrade", "https://www.freqtrade.io/en/stable/", "开源加密货币交易机器人。"],
            ["Backtrader", "https://www.backtrader.com/", "经典 Python 回测框架。"],
            ["vectorbt", "https://vectorbt.dev/", "向量化量化研究工具。"],
            ["backtesting.py", "https://kernc.github.io/backtesting.py/", "轻量 Python 回测库。"],
            ["QuantConnect LEAN", "https://github.com/QuantConnect/Lean", "开源量化交易引擎。"],
            ["vn.py", "https://www.vnpy.com/", "中文量化交易框架。"],
            ["AkShare", "https://akshare.akfamily.xyz/", "中文开源金融数据接口。"],
            ["CCXT", "https://github.com/ccxt/ccxt", "加密交易所 API 统一库。"],
        ],
        "quick_start": ["只做纸交易，先跑 3 个月模拟。", "每个策略必须有最大回撤、手续费和滑点。", "用小资金之前先写风控规则。"],
        "pitfalls": ["不要相信截图收益率。", "回测盈利不等于实盘盈利，本页不构成投资建议。"],
    },
    {
        "title": "数据分析与可视化工具",
        "slug": "data-visualization",
        "category": "数据 / 可视化",
        "audience": "科研、运营、产品、数据分析和 dashboard 用户",
        "hero_url": "https://github.com/apache/echarts",
        "summary": "整理 Python 数据分析、数据库、本地 dashboard、交互图表和 BI 工具。",
        "why_hot": "数据可视化是跨行业刚需，开源工具成熟，适合做长期维护总表。",
        "entries": [
            ["Jupyter", "https://jupyter.org/", "Notebook 数据分析环境。"],
            ["Pandas", "https://pandas.pydata.org/", "Python 数据分析基础库。"],
            ["Polars", "https://pola.rs/", "高性能 DataFrame。"],
            ["DuckDB", "https://duckdb.org/", "嵌入式分析数据库。"],
            ["Plotly", "https://plotly.com/python/", "交互式图表。"],
            ["Apache ECharts", "https://echarts.apache.org/", "强大的开源可视化图表库。"],
            ["Streamlit", "https://streamlit.io/", "快速构建数据 App。"],
            ["Apache Superset", "https://superset.apache.org/", "开源 BI 平台。"],
        ],
        "quick_start": ["小数据先 Pandas，大数据/本地分析试 DuckDB/Polars。", "展示给别人看时用 Streamlit 或 Superset。", "论文图表先保证可复现。"],
        "pitfalls": ["不要把图做得比数据更复杂。", "dashboard 上线前要处理权限和数据脱敏。"],
    },
    {
        "title": "API 调试与后端开发工具",
        "slug": "api-backend-tools",
        "category": "后端 / API",
        "audience": "后端、全栈、AI 应用开发者",
        "hero_url": "https://hoppscotch.io/",
        "summary": "整理 API 调试、接口文档、命令行 HTTP、后端框架、数据库和 BaaS 工具。",
        "why_hot": "API 调试和后端脚手架是项目开发刚需，链接型清单很容易被收藏。",
        "entries": [
            ["Postman", "https://www.postman.com/", "主流 API 开发协作平台。"],
            ["Insomnia", "https://insomnia.rest/", "API 调试客户端。"],
            ["Hoppscotch", "https://hoppscotch.io/", "开源 API 调试工具。"],
            ["Bruno", "https://www.usebruno.com/", "本地优先 API 客户端。"],
            ["HTTPie", "https://httpie.io/", "友好的命令行 HTTP 工具。"],
            ["Swagger / OpenAPI", "https://swagger.io/specification/", "API 描述规范。"],
            ["FastAPI", "https://fastapi.tiangolo.com/", "Python API 框架。"],
            ["Supabase", "https://supabase.com/", "开源 Firebase 替代。"],
        ],
        "quick_start": ["接口先写 OpenAPI，再调试。", "本地项目可用 Bruno 管理接口文件。", "Python 后端快速 demo 选 FastAPI。"],
        "pitfalls": ["不要把生产 token 保存在公开 API collection。", "接口文档如果不跟 CI 走，很快会失真。"],
    },
    {
        "title": "GitHub 开源项目包装与发布",
        "slug": "github-project-packaging",
        "category": "GitHub / 开源",
        "audience": "想让项目更像正式开源产品的人",
        "hero_url": "https://github.com/badges/shields",
        "summary": "整理 README、badge、Pages、release、贡献者、star history、部署和项目展示工具。",
        "why_hot": "很多人代码能写，但项目不会包装；这类清单直接服务 GitHub 涨星和面试展示。",
        "entries": [
            ["GitHub README Docs", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes", "官方 README 说明。"],
            ["Shields.io", "https://shields.io/", "Badge 生成。"],
            ["GitHub Pages", "https://pages.github.com/", "项目页托管。"],
            ["Vercel", "https://vercel.com/", "前端项目部署。"],
            ["Netlify", "https://www.netlify.com/", "静态站点部署。"],
            ["Readme.so", "https://readme.so/", "README 结构辅助。"],
            ["Star History", "https://star-history.com/", "star 增长图。"],
            ["all-contributors", "https://allcontributors.org/", "贡献者展示规范。"],
        ],
        "quick_start": ["README 首屏必须说清楚项目解决什么。", "放截图、安装、Quick Start、FAQ 和 License。", "每次功能更新都发 release。"],
        "pitfalls": ["不要在无关 issue 里硬广。", "截图和 demo 链接比口号重要。"],
    },
    {
        "title": "隐私、安全与密码管理工具",
        "slug": "privacy-security",
        "category": "安全 / 隐私",
        "audience": "学生、开发者、远程办公和注重隐私的人",
        "hero_url": "https://github.com/bitwarden/clients",
        "summary": "整理密码管理、加密通信、隐私邮箱、浏览器、安全检查和数据泄露查询入口。",
        "why_hot": "账号安全和隐私工具是长期刚需，尤其适合中文用户做基础安全教育。",
        "entries": [
            ["Privacy Guides", "https://www.privacyguides.org/", "隐私工具和建议总入口。"],
            ["Bitwarden", "https://bitwarden.com/", "密码管理器。"],
            ["KeePassXC", "https://keepassxc.org/", "本地开源密码库。"],
            ["Proton Mail", "https://proton.me/mail", "注重隐私的邮箱服务。"],
            ["Signal", "https://signal.org/", "端到端加密通讯。"],
            ["Tor Browser", "https://www.torproject.org/", "匿名网络浏览器。"],
            ["Have I Been Pwned", "https://haveibeenpwned.com/", "数据泄露查询。"],
            ["age", "https://github.com/FiloSottile/age", "简单现代的文件加密工具。"],
        ],
        "quick_start": ["先启用密码管理器和两步验证。", "重要账号使用独立邮箱和独立密码。", "定期查泄露并轮换密码。"],
        "pitfalls": ["不要复用密码。", "不要把 2FA 恢复码放在同一个云笔记里。"],
    },
    {
        "title": "中文开源镜像与下载加速",
        "slug": "cn-mirrors-downloads",
        "category": "下载 / 镜像",
        "audience": "国内开发者、学生、服务器用户",
        "hero_url": "https://github.com/tuna/tunasync",
        "summary": "整理国内高校和厂商开源镜像、包管理加速和常见开发依赖下载入口。",
        "why_hot": "下载慢是中文开发者高频痛点，镜像站总表非常实用。",
        "entries": [
            ["清华大学开源软件镜像站", "https://mirrors.tuna.tsinghua.edu.cn/", "国内常用高校镜像站。"],
            ["中国科学技术大学镜像站", "https://mirrors.ustc.edu.cn/", "中科大开源镜像。"],
            ["上海交通大学镜像站", "https://mirror.sjtu.edu.cn/", "上海交大镜像站。"],
            ["北京外国语大学镜像站", "https://mirrors.bfsu.edu.cn/", "BFSU 镜像站。"],
            ["阿里云镜像站", "https://developer.aliyun.com/mirror/", "常用开发镜像配置文档。"],
            ["npmmirror", "https://npmmirror.com/", "npm 包镜像。"],
            ["TUNA Anaconda 帮助", "https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/", "conda/anaconda 镜像配置。"],
            ["TUNA PyPI 帮助", "https://mirrors.tuna.tsinghua.edu.cn/help/pypi/", "pip 镜像配置。"],
        ],
        "quick_start": ["优先使用高校镜像官方帮助页配置。", "项目 README 里写清楚镜像只是加速，不是依赖来源。", "服务器上固定配置 pip/conda/npm 镜像。"],
        "pitfalls": ["不要从来路不明的网盘下载开发工具。", "镜像同步有延迟，版本异常时先回官方源确认。"],
    },
]


def main() -> None:
    ensure_dirs()
    write_json()
    write_readme()
    write_guides()
    write_auxiliary_files()
    print(f"Generated {len(GUIDES)} Chinese practical guides.")


def ensure_dirs() -> None:
    for path in [ROOT / "data", GUIDES_DIR, SCREENSHOTS, ROOT / "docs"]:
        path.mkdir(parents=True, exist_ok=True)


def write_json() -> None:
    payload = {
        "meta": {
            "title": "Awesome Practical CN",
            "description": "20 个中文实用信息汇总贴：AI、学生福利、科研、设计、远程开发、效率工具、量化、镜像等。",
            "language": "zh-CN",
            "last_verified": "2026-06-29",
            "screenshot_policy": "Screenshots are captured from official/public landing pages and include source URLs in each guide.",
        },
        "guides": GUIDES,
    }
    DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_readme() -> None:
    rows = []
    for index, guide in enumerate(GUIDES, start=1):
        rows.append(
            f"| {index:02d} | [{guide['title']}](docs/guides/{guide['slug']}.md) | {guide['category']} | {guide['audience']} | {len(guide['entries'])} |"
        )
    hot_cards = "\n".join(
        f'<a href="docs/guides/{guide["slug"]}.md"><img src="assets/screenshots/{guide["slug"]}.png" width="260" alt="{guide["title"]}"></a>'
        for guide in GUIDES[:8]
    )
    readme = f"""# Awesome Practical CN

> 20 个中文实用信息汇总贴：AI 工具、学生福利、科研论文、免费课程、设计素材、远程开发、效率工具、PDF/OCR、自托管、量化、镜像站等。

<p align="center">
  <img src="assets/cover.svg" alt="Awesome Practical CN cover" width="920">
</p>

## 为什么做这个

中文互联网上不缺碎片链接，缺的是可以直接收藏、转发、持续维护的高质量总表。本仓库把不同领域的常用入口整理成 20 个独立专题，每个专题都包含：

- 一句话定位
- 官方入口 / 下载入口 / GitHub 链接
- 适合谁
- 快速上手顺序
- 常见坑
- 官方公开页面截图与来源链接

> 截图说明：本仓库优先使用官方公开网页的自动截图，并在每个专题页标注截图来源。若某网站禁止自动截图或页面不可访问，则保留来源链接并等待人工补图。

## 热门专题预览

<p>
{hot_cards}
</p>

## 20 个专题

| # | 专题 | 分类 | 适合人群 | 链接数 |
| ---: | --- | --- | --- | ---: |
{chr(10).join(rows)}

## 维护原则

- 只收官方入口、官方文档、知名开源仓库和相对稳定的资源页。
- 不收盗版资源、破解软件、返利链接、来路不明网盘。
- 每个链接都要说明用途，不做单纯堆链接。
- 截图必须来自公开页面，且在专题页保留来源。
- 面向中文用户写结论，尽量减少英文资料的理解成本。

## 本地生成

```bash
python3 scripts/build_guides.py
python3 scripts/capture_screenshots.py
python3 scripts/validate_links.py
```

## 贡献

欢迎补充新专题、替换失效链接、提交更清晰的官方截图。提交前请先看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

MIT. 第三方网站截图和商标归原权利方所有，本仓库仅做导航、评论和信息整理。
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def write_guides() -> None:
    for guide in GUIDES:
        entries = "\n".join(
            f"| [{name}]({url}) | {desc} |" for name, url, desc in guide["entries"]
        )
        quick = "\n".join(f"{idx}. {item}" for idx, item in enumerate(guide["quick_start"], start=1))
        pitfalls = "\n".join(f"- {item}" for item in guide["pitfalls"])
        md = f"""# {guide['title']}

![{guide['title']}](../../assets/screenshots/{guide['slug']}.png)

> 分类：**{guide['category']}**
>
> 适合：{guide['audience']}
>
> 截图来源：[{guide['hero_url']}]({guide['hero_url']})

## 一句话

{guide['summary']}

## 为什么值得收藏

{guide['why_hot']}

## 精选入口

| 名称 | 用途 |
| --- | --- |
{entries}

## 快速上手

{quick}

## 常见坑

{pitfalls}

## 维护建议

- 如果某个工具出现价格、额度、开源状态或官网迁移，请优先改本页链接和说明。
- 如果补图，请使用官方公开页面截图，并保留来源链接。
- 如果新增入口，请写清楚它解决什么问题，避免变成无差别链接农场。

---

[返回首页](../../README.md)
"""
        (GUIDES_DIR / f"{guide['slug']}.md").write_text(md, encoding="utf-8")


def write_auxiliary_files() -> None:
    (ROOT / ".gitignore").write_text(
        dedent(
            """\
            __pycache__/
            *.pyc
            .DS_Store
            .venv/
            output/
            """
        ),
        encoding="utf-8",
    )
    (ROOT / "LICENSE").write_text(
        dedent(
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
        ),
        encoding="utf-8",
    )
    (ROOT / "CONTRIBUTING.md").write_text(
        dedent(
            """\
            # Contributing

            欢迎补充中文实用信息汇总。

            ## 收录标准

            - 优先官方入口、官方文档、知名开源仓库、稳定资源站。
            - 每个链接必须说明用途。
            - 不收盗版、破解、灰产、返利链接和来路不明网盘。
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
            """
        ),
        encoding="utf-8",
    )
    (ROOT / "CHANGELOG.md").write_text(
        dedent(
            """\
            # Changelog

            ## v0.1.0 - 2026-06-29

            - Initial release with 20 Chinese practical guide pages.
            - Add structured guide data, generated README, topic pages, screenshot pipeline, and link validator.
            """
        ),
        encoding="utf-8",
    )
    (ROOT / "docs" / "MAINTENANCE.md").write_text(
        dedent(
            """\
            # Maintenance

            ## 每周维护

            - 跑 `python3 scripts/validate_links.py` 检查链接。
            - 检查 GitHub 热门项目和产品官网是否迁移。
            - 更新截图时保留来源链接，不使用付费课程、会员内容或私人页面截图。

            ## 内容风格

            - 中文结论前置。
            - 每个链接必须解释用途。
            - 每页既要能收藏，也要能直接发给朋友。
            """
        ),
        encoding="utf-8",
    )
    (ASSETS / "cover.svg").write_text(render_cover_svg(), encoding="utf-8")


def render_cover_svg() -> str:
    cards = [
        ("AI 工具", "#2563eb"),
        ("学生福利", "#16a34a"),
        ("科研论文", "#9333ea"),
        ("效率工具", "#ea580c"),
        ("PDF/OCR", "#0891b2"),
        ("量化回测", "#dc2626"),
        ("开源替代", "#4f46e5"),
        ("镜像下载", "#0f766e"),
    ]
    card_svg = []
    for idx, (label, color) in enumerate(cards):
        x = 80 + (idx % 4) * 290
        y = 245 + (idx // 4) * 120
        card_svg.append(
            f'<rect x="{x}" y="{y}" width="240" height="82" rx="22" fill="#ffffff" filter="url(#shadow)"/>'
            f'<circle cx="{x + 42}" cy="{y + 41}" r="18" fill="{color}" opacity=".92"/>'
            f'<text x="{x + 76}" y="{y + 50}" class="card">{label}</text>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1320" height="610" viewBox="0 0 1320 610" role="img" aria-label="Awesome Practical CN">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#fbfdff"/>
      <stop offset="100%" stop-color="#eef6ff"/>
    </linearGradient>
    <filter id="shadow" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="10" stdDeviation="13" flood-color="#15304f" flood-opacity=".13"/>
    </filter>
    <style>
      .title{{font:800 48px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#0f172a}}
      .sub{{font:500 22px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#52637a}}
      .card{{font:760 24px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#142033}}
      .small{{font:600 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;fill:#64748b}}
    </style>
  </defs>
  <rect width="1320" height="610" rx="34" fill="url(#bg)"/>
  <circle cx="1120" cy="120" r="170" fill="#dbeafe" opacity=".65"/>
  <circle cx="140" cy="510" r="150" fill="#dcfce7" opacity=".55"/>
  <text x="72" y="98" class="title">Awesome Practical CN</text>
  <text x="74" y="142" class="sub">20 个中文实用信息汇总贴：链接、截图、用途、避坑和快速上手</text>
  <text x="74" y="188" class="small">AI · 学生福利 · 科研论文 · 免费课程 · 设计素材 · 远程开发 · 效率工具 · 量化 · 镜像</text>
  {''.join(card_svg)}
</svg>
"""


if __name__ == "__main__":
    main()
