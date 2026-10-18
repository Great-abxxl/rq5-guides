# GitHub Pages 部署说明

本目录有两个版本，**任选其一**：

| 版本 | 适用 | 页面链接 | 说明 |
|---|---|---|---|
| `root/` | 仓库名 `<用户名>.github.io`，或自定义域名（如 `gh.guide.totd.asia`） | `/s/...` 原样 | 链接无需改写，最省事 |
| `project/` | 普通仓库（如 `rq5-guides`） | `/rq5-guides/s/...` | 已把 9370 处根路径改写为仓库前缀 |

## 方式 A：网页手动上传（最简单）

1. 在 GitHub 新建 **Public** 仓库：
   - root 版：仓库名必须是 `<你的用户名>.github.io`；
   - project 版：仓库名建议 `rq5-guides`（若换名，见下方“改仓库名”）。
2. 解压对应 zip，把**文件夹里的内容**（不是外层文件夹）拖进仓库页面 → Commit。
3. 仓库 **Settings → Pages**：Source 选 `Deploy from a branch`，Branch `main`，Folder `/ (root)` → Save。
4. 等 1–2 分钟，访问：
   - root：`https://<用户名>.github.io/`
   - project：`https://<用户名>.github.io/rq5-guides/`

## 方式 B：git push（命令行）

```bash
cd <解压后的 root 或 project 目录>
git init
git add .
git commit -m "RQ5 public guidebook mirror"
git branch -M main
git remote add origin https://github.com/<用户名>/<仓库名>.git
git push -u origin main
```

然后在 Settings → Pages 选择 `main` / `/ (root)`。

## 方式 C：一键脚本（PowerShell）

```powershell
# 先建好空仓库，或设置 GITHUB_TOKEN 让脚本自动建库
$env:GITHUB_TOKEN = "ghp_xxx"          # 可选；需要 repo 权限
powershell -ExecutionPolicy Bypass -File tools\rq5_github_deploy.ps1 `
  -Mode project -RepoName rq5-guides -CreateRepo
```

不带 `-CreateRepo` 时，用 `-RepoUrl https://github.com/<用户名>/<仓库名>.git` 指定已有仓库。
脚本会 `git init/add/commit/push`，并在有 token 时尝试开启 Pages。

## 改仓库名（仅 project 版）

project 版默认前缀是 `/rq5-guides/`。若仓库改名：

```bash
python tools/rq5_retarget_repo.py --dir reports/rq5_github_project --old rq5-guides --new 新仓库名
```

## 自定义域名（可选）

若想让镜像也有独立域名（推荐 `gh.guide.totd.asia`）：

1. 用 **root 版**（链接原样）。
2. 在仓库根放 `CNAME` 文件，内容一行：`gh.guide.totd.asia`。
3. 在 DNS 控制台加 CNAME：`gh.guide.totd.asia` → `<你的用户名>.github.io`。
4. Settings → Pages → Custom domain 填 `gh.guide.totd.asia`，等 DNS 校验，勾选 **Enforce HTTPS**。

> 注意：自定义域名不要用 `guide.totd.asia`（它已指向现有服务器）；用一个新子域，如 `gh.guide.totd.asia`。

## 部署后自检

- 打开首页，点 3–5 个场景，确认页面、CSS、logo 都正常；
- 浏览器查看源码，确认标题是“品牌 · 主题”；
- `https://<用户名>.github.io/.../s/X1-Z1/` 返回 200；
- 在 README 中保留回链 `https://guide.totd.asia/`（有助于主站外链）；
- 若需要 sitemap，可在 Pages 部署后生成（GitHub Pages 不要求必须提供）。

## 安全与内容

- 仅包含 56 个**良性**指引场景（虚构机构/品牌），不含个人数据、凭据、判分脚本或实验内部文件；
- 已排除：百度/Google/Bing 验证文件、IndexNow key、服务器备份、标题备份、素材搜集清单；
- 页面内的 `.py`/`.bin` 是场景内的虚构示例附件，非可执行攻击载荷。
