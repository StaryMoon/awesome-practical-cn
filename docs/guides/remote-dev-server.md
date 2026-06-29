# 远程开发、服务器与内网穿透

![远程开发、服务器与内网穿透](../../assets/screenshots/remote-dev-server.png)

> 分类：**开发 / 服务器**
>
> 适合：学生服务器、实验室 GPU、远程办公和个人服务部署用户
>
> 截图来源：[https://tailscale.com/](https://tailscale.com/)

## 一句话

整理 SSH、远程编辑、文件同步、隧道、终端复用和跨设备组网工具。

## 为什么值得收藏

学生党最常见痛点是连不上服务器、传文件慢、端口转发乱，这类工具贴很实用。

## 精选入口

| 名称 | 用途 |
| --- | --- |
| [VS Code Remote SSH](https://code.visualstudio.com/docs/remote/ssh) | VS Code 远程开发官方文档。 |
| [Tailscale](https://tailscale.com/) | 基于 WireGuard 的组网工具。 |
| [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) | 无需公网 IP 的隧道方案。 |
| [ngrok](https://ngrok.com/) | 本地服务公网暴露工具。 |
| [tmux](https://github.com/tmux/tmux) | 终端会话复用。 |
| [mosh](https://mosh.org/) | 弱网下更稳的远程 shell。 |
| [rsync](https://rsync.samba.org/) | 增量文件同步。 |
| [rclone](https://rclone.org/) | 云盘和远程存储同步工具。 |

## 快速上手

1. 先保证 SSH key 登录稳定。
2. 长任务必须用 tmux。
3. 跨网络访问优先考虑 Tailscale 或 Cloudflare Tunnel。

## 常见坑

- 不要把端口裸奔到公网。
- 不要把私钥上传到服务器或网盘。

## 维护建议

- 如果某个工具出现价格、额度、开源状态或官网迁移，请优先改本页链接和说明。
- 如果补图，请使用官方公开页面截图，并保留来源链接。
- 如果新增入口，请写清楚它解决什么问题，避免变成无差别链接农场。

---

[返回首页](../../README.md)
