# PPT Studio

**跟 AI 说一句话，它把整套 PPT 画出来。图片型 PPT 还能反过来重建成可编辑的 pptx。**

不是往模板里填字——每一页都由图像模型整体设计生成，然后打包成可以放映的 `.pptx`；
拿到一套只有图片的 PPT，也能拆出文字、图标、背景，重建成真正能改字的版本。

![生成结果](frontend/public/help/img07.jpg)

MIT 许可 · 自己部署 · 数据全在自己机器上 · Windows 双击即用 / Linux · macOS 一条命令 / Docker 一键

在线版：[zuoppt.top](https://zuoppt.top)（同一份代码）。

<details>
<summary><b>English</b></summary>

**PPT Studio** is a self-hosted web app that turns one sentence (plus any material you drop in — Word, PDF, Excel, images, decks) into a complete slide deck. An agent first agrees the visual style and the per-page outline with you, then an image model paints every slide as a whole composition, and the result is exported as a `.pptx`. It also runs the other way: give it an image-only deck and the **image-to-editable** pipeline segments text, icons and backgrounds, solves fonts and sizes, and rebuilds a genuinely editable pptx.

Quick start — Windows: double-click `start.bat`. Linux / macOS: `./start.sh`. Docker: `docker compose up -d`. Then open http://127.0.0.1:8000, register (the first account becomes admin, no invite code needed), and enter your OpenAI-compatible endpoints in the admin panel (`#/admin`). Set `FAKE_IMAGE=1` to walk through the whole flow without spending a cent. Bring your own API: any OpenAI-compatible chat model with tool calling (vision recommended) and an image model such as `gpt-image-2`.

Both PPT processing paths are supported: on **Windows** the editable rebuild renders through PowerPoint (COM) and fits Microsoft YaHei / DengXian / SimHei / SimSun; on **Linux / macOS** it uses LibreOffice headless and Noto CJK fonts (`apt install libreoffice-impress fonts-noto-cjk fonts-arphic-ukai`). The landing page, UI and prompts are Chinese-first; the landing page has an English switch.

</details>

---

## 目录

- [先说清楚：它是什么，不是什么](#先说清楚它是什么不是什么)
- [功能一览](#功能一览)
- [安装](#安装)
- [第一次使用（图文七步）](#第一次使用图文七步)
- [图转可编辑](#图转可编辑)
- [多人使用：注册门禁与积分](#多人使用注册门禁与积分)
- [常见问题](#常见问题)
- [部署到服务器](#部署到服务器)
- [给开发者](#给开发者)
- [仓库来历](#仓库来历)

---

## 先说清楚：它是什么，不是什么

**它是**一个跑在你自己电脑上的网页应用。你打开浏览器，用中文描述需求（可以顺便上传 Word、PDF、
Excel、图片、已有的 PPT），AI 先跟你确认设计风格和大纲，你点头之后才逐页作画，最后给你一个 `.pptx`。

**它不是**免费的。程序本身开源免费，但**它要调用你自己的 AI 接口，每生成一页都要花钱**。
成本取决于你用哪家的接口——这笔账是你和接口提供方之间的事，跟本项目无关。

**想先零成本试一遍**：`.env` 里把 `FAKE_IMAGE` 设成 `1`，程序会用本地占位图代替真实的图像生成，
整个流程都能走通，一分钱不花。确认自己喜欢再去买接口。

---

## 功能一览

| | |
|---|---|
| **一句话生成整套 PPT** | 需求 + 资料 → 风格方案（人审）→ 逐页大纲（人审、可逐字段手改）→ 逐页整图渲染 → 自动质检 → 导出 pptx |
| **只改一页** | 「第 3 页标题换成……」只重画那一页；内容没变的页按 hash 跳过，不重复花钱 |
| **图转可编辑** | 图片型 PPT → 去字、分割、抠图、字体求解、重建、校准 → 真正可编辑的 pptx（[详情](#图转可编辑)） |
| **风格库 / 模板库** | 官方 6 套风格；上传 pptx 或整套图片做模板，AI 自动按页型分类；会话里确认过的风格一键存入 |
| **两种会话模式** | 普通：资料全文进上下文，一轮出结果；⚡高级：agent 在一次性 Docker 沙盒里读资料、跑 Python 画图表、自己看图检查 |
| **模型注册表** | 多个 OpenAI 兼容端点并存；思维链模型（DeepSeek-R1 / GLM 等）实时显示推理；不识图的模型自动降级 |
| **图像多通道** | 主/备通道按优先级排，失败自动切换，连续失败进入冷却；每通道可选质量档位 |
| **管理面板** | 总览、用户、兑换码、模型与 API、调用健康、成本核算（token × 官方价 × 中转倍率 vs 积分收入）、全站流水、站内信 |
| **完成提醒** | 渲染完 / 转换完有提示音、标签页闪烁、可选桌面通知——切去别的标签页也不会错过 |
| **展示页** | 中英双语的产品首页（`#/welcome`），自部署时自动隐藏售卖相关内容 |

---

## 安装

### 你需要准备什么

1. **Python 3.11 或更高**。[到官网下载](https://www.python.org/downloads/)，Windows 安装时**务必勾选 `Add Python to PATH`**。
2. **一个 OpenAI 格式的 AI 接口**——给你一个 `base_url` 和一个 `api_key` 的都行（官方 API、各家中转、自建网关）：

   | 用途 | 需要的能力 | 说明 |
   |---|---|---|
   | 对话模型 | 支持工具调用（function calling），最好也支持识图 | 负责聊需求、定风格、写大纲、标注图片 |
   | 图像模型 | 能按指定尺寸出图，如 `gpt-image-2` / `gpt-image-2.5` | 负责把每一页画出来，**这是主要成本** |

   > 这些不用现在填。装好之后在网页的管理面板里配置，不用编辑任何文件。

3. （可选）**LibreOffice**：「上传 pptx 做模板」需要；Linux / macOS 上「图转可编辑」也需要。
4. （可选）**Docker**：只有「⚡高级模式」的沙盒需要。

### Windows：双击 `start.bat`

1. 点这个仓库右上角的绿色 **Code → Download ZIP**，解压到任意文件夹
2. 双击 **`start.bat`**
3. 等它跑完（第一次要装依赖，2–5 分钟），浏览器会自动打开 http://127.0.0.1:8000

它会自动完成：建虚拟环境 → 装依赖 → 生成 `.env`（随机登录密钥、开放注册）→ 启动 → 开浏览器。
关掉那个黑色窗口就是停止；下次再双击，秒开。

### Linux / macOS：`./start.sh`

```bash
git clone https://github.com/sakurahello1/ppt-studio.git && cd ppt-studio
./start.sh
```

做的事和 `start.bat` 一样。想让局域网访问：`HOST=0.0.0.0 ./start.sh`。

系统依赖（可选功能用）：

```bash
# Debian / Ubuntu
sudo apt install libreoffice-impress fonts-noto-cjk fonts-noto-cjk-extra fonts-arphic-ukai
# macOS
brew install --cask libreoffice     # 字体：把 Noto Sans CJK / Noto Serif CJK 的 .ttc 放进 ~/Library/Fonts
```

### Docker

```bash
git clone https://github.com/sakurahello1/ppt-studio.git && cd ppt-studio
AUTH_SECRET=$(python3 -c 'import secrets;print(secrets.token_hex(32))') docker compose up -d
```

镜像里带了 LibreOffice 和中文字体，模板导入与图转可编辑都能用。`data/` 与 `workspaces/` 挂在当前目录。

### 手动

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env                 # 至少改掉 AUTH_SECRET
# 前端产物 web/ 随仓库自带；改了前端才需要：cd frontend && npm install && npm run build
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000
```

---

## 第一次使用（图文七步）

> 截图来自作者的在线版，地址栏是 `zuoppt.top`；你自己部署的话地址是 **http://127.0.0.1:8000**，界面一样。
> 站内也有一份图文教程：登录页的「新手使用教程」（`/help/`）。

### 第 1 步：打开网址

![打开网址](frontend/public/help/img01.jpg)

### 第 2 步：注册账号

点「注册」，用户名密码自己定。

![注册](frontend/public/help/img02.jpg)

- **第一个注册的账号自动成为管理员**，管理员生成永远不扣积分——个人自用全程不用管积分系统。
- 截图里的「邀请码」框**你不会看到**。自己部署默认开放注册（`OPEN_SIGNUP=1`），
  邀请码是你把实例开放给别人时**自己设**的门禁，不用向任何人索取。

### 第 3 步：配置模型（只需做一次）

登录后进「管理面板」（地址栏加 `#/admin`）→「模型与 API」，填你的接口。

- **对话模型**和**图像通道**分开配，每一条都能独立填 `base_url` / `api_key`，`＋ 添加`、行尾 `×` 删。
- **识图**：这个模型能看图。上传 PPT 模板、自动质检、图转可编辑的标注都需要识图能力。
- **思维链**：DeepSeek-R1、GLM 这类会输出推理过程的模型勾上，思考过程会实时显示。普通模型不要勾。
- **api_key 保存后显示成掩码**（`sk-…a1b2`）是正常的。想改就填新的；**留空 = 保留原值**。
- **图像通道可以配多条**，按优先级排，主通道挂了自动切备用；每条可选质量档位。
- **成本核算**（可选）：给每个模型填官方美元单价和中转倍率、给图像通道填每张人民币，
  「成本」页就能按 token 和张数把上游花费算出来，和积分收入对比。

### 第 4 步：回首页，说需求

用中文描述你要什么，可以顺便拖入资料（Word / PDF / Excel / 图片 / PPT）。下方还能选风格和模板。

![输入需求](frontend/public/help/img03.jpg)

### 第 5 步：确认设计风格

AI 会先给一份风格方案，行就点确认，不行就直接说要改什么。**这一步不花钱**，可以反复改到满意。

![确认风格](frontend/public/help/img05.jpg)

### 第 6 步：确认大纲

逐页大纲。可以直接在编辑器里改，也可以让 AI 改「第 3 页标题换成……」。**这一步也不花钱。**

![确认大纲](frontend/public/help/img06.jpg)

> 前两道确认是刻意设计的：作画才是花钱的环节，所以让你在花钱之前先把方向定死。

### 第 7 步：出图、下载

确认之后开始逐页作画，缩略图一张张点亮；完成后 AI 会自己看一遍成品做质检，明显问题会自主修正（不另扣积分）。
然后点「下载 PPTX」。

![生成结果](frontend/public/help/img07.jpg)

对哪页不满意，直接说「第 3 页……」——**只有那一页会重画**。成品下方还有「✎ 转成可编辑版」，见下一节。

---

## 图转可编辑

输入一套图片型 PPT（刚生成的、或者上传的 pptx / 一组图片），输出一份**真正可编辑**的 pptx：
文字是文本框、图标是独立图片、背景是干净的底图。

```
① 去字      gpt-image-2 擦掉整页文字，得到干净背景
② 标注      对话模型三次结构化识图（文字行 / 图标编号 / 容器面板），并发发出
③ 裁切      按标注从原图与去字图里裁出图标、编号、面板，GrabCut 抠边
④ 求解      字形缓存 + 质心对齐 IoU，反解每个文字框的字体、字号、字距
⑤ 重建      组装 pptx → 渲染成图 → 逐框与原图对位闭环 → 再渲染
⑥ 校准      同组文本的字体 / 字号 / 字距归一（视觉一致性优先于像素还原）
⑦ 交付      合册 + 逐页残差报告（人工复核的优先级）
```

两种模式：**完整**（文字 + 图标 + 面板全部拆开）和**只做文字**（图标面板保留在背景里，便宜更快）。
标注结果可以在工作台里人工修订后一键重建；每一步的产物都在工作区里，任务可以断点续跑、
只重跑某一页的某一阶段。求解在独立子进程里跑，内存吃紧时先被系统回收，不影响主服务。

### 两个平台，两条 PPT 处理路径

重建后的 pptx 要渲染成图片做闭环对位，字体求解也要读本机字体——这一段 Windows 和 Linux 走的路完全不同，
两条都在这个仓库里：

| | Windows | Linux / macOS |
|---|---|---|
| pptx → 图片 | **PowerPoint COM**（常驻单实例；这是原版实测的路线） | **LibreOffice headless**（`soffice`，独立 profile，串行） |
| 候选字体 | 微软雅黑 / 等线 / 黑体 / 宋体 /（可选）思源黑 VF，都在 `C:\Windows\Fonts` | Noto Sans CJK / Noto Serif CJK / AR PL UKai，`fonts-noto-cjk` `fonts-arphic-ukai` |
| 依赖 | 已安装的 PowerPoint；`pywin32`（`pip install -e .` 会自动装） | `libreoffice-impress` + 上述字体包（macOS：`brew install --cask libreoffice` + 手动放字体） |
| 强制指定 | `EDITABLE_RENDERER=com` | `EDITABLE_RENDERER=soffice`；`SOFFICE_BIN` 指定可执行文件位置 |

没装对应的字体不会报错，只是候选变少；一个都没有时求解会失败，工作台会把原因写出来。
`workspaces/<会话>/editable/` 里是全部中间产物（`meta.json` 状态机、`strip/` 去字图、`seg/` 标注、
`assets/` 素材、`solved/` 求解、`build/` 单页成品、`deck.pptx` 合册、`report.json` 残差）。

---

## 多人使用：注册门禁与积分

自己一个人用，这一节可以跳过。

**注册门禁**（管理面板「模型与 API」最下方，或首启的 `.env`）：

- **开放注册**（`OPEN_SIGNUP=1`，自部署默认）：任何人可以注册；填了码照样按码走。
- **全局口令**（`ACCESS_PASSWORD`）：一个你手动发给别人的口令，走口令注册不送积分。
- **一次性邀请码**：管理面板批量生成 `INV-XXXX-XXXX-XXXX`，自带积分面额，注册即到账。
  邀请码和兑换码可以互换使用——买错种类的人不会被挡在门外。

**把实例开放到公网前**：关掉开放注册，确认 `AUTH_SECRET` 是随机值。

**积分**：按实际渲染页数扣，默认 1 积分 / 页，2K 与 4K 同价（倍率在管理面板可改）；
图转可编辑同样 1 积分 / 页；内容没变被跳过的页不收费；失败或中途停止的页自动退款；自动质检的重画不另扣；
管理员始终免费。对话、大纲、模板解析都不计费。

**兑换码**：管理面板批量生成 `PPT-XXXX-XXXX-XXXX`（可导出 CSV），用户在「兑换与购买」页兑换，接口限频防爆破。
「购买链接」留空则站内不显示任何购买入口。

**站内信**：用户可以给管理员留言，登录页有「忘记密码」公开通道（提交联系方式，管理员在面板里处理）。

---

## 常见问题

<details>
<summary><b>双击 start.bat 后闪一下就没了</b></summary>

八成是 Python 没装，或者装的时候没勾 `Add Python to PATH`。按 `Win + R`，输入 `cmd` 回车，
在黑窗口里输入 `python --version`。提示「不是内部或外部命令」就是 PATH 没配好——重新运行 Python 安装包，
选 `Modify`，勾上 `Add Python to environment variables`。
</details>

<details>
<summary><b>打开网页显示「前端尚未构建，请运行 vite build」</b></summary>

说明 `web/` 文件夹缺失。它随仓库一起发布，不需要你构建；最常见的原因是下载 ZIP 时没解压完整。
开发者自己构建：`cd frontend && npm install && npm run build`。
</details>

<details>
<summary><b>我改了 .env，但设置没生效</b></summary>

**这是最容易踩的坑。** `.env` 里的模型、邀请码、开放注册这些配置**只在第一次启动时**被读进数据库，
之后以数据库里的值为准。**改配置请到网页的管理面板里改**，立刻生效，不用重启。
`AUTH_SECRET`、`FAKE_IMAGE`、目录位置这些启动常量除外——它们每次启动都从 `.env` 读。
</details>

<details>
<summary><b>注册时提示要邀请码</b></summary>

说明这个实例关了开放注册。自己部署的默认配置是开着的，正常情况下不会遇到。
会遇到的情况：你照着旧版 `.env.example` 写了 `ACCESS_PASSWORD=change_me`——那注册时就填 `change_me`；
或者你已经启动过一次、之后才改 `.env`——改了没用，见上一条，请到管理面板「模型与 API」里勾上「开放注册」。

> **删 `data/` 前请先停止服务。** 服务运行中删库会让配置重新播种成一个半吊子状态。
</details>

<details>
<summary><b>生成时提示积分不足</b></summary>

**个人自己用不会遇到。** 第一个注册的账号是管理员，管理员免计费。如果遇到了，说明你当前登录的不是第一个账号；
用管理员账号到管理面板「用户」里给它加积分即可。
</details>

<details>
<summary><b>图像生成报错 / 一直失败</b></summary>

1. 管理面板里 `base_url` 是不是漏了结尾的 `/v1`
2. 你的 key 有没有开通图像模型的权限（很多中转站对话和图像是分开授权的）
3. 账户余额
4. 先把 `FAKE_IMAGE=1` 打开跑一遍——占位图能正常出，问题就一定在接口那端

管理面板「调用健康」页能看到每个通道最近的成功率、耗时和错误原文。
</details>

<details>
<summary><b>上传 pptx 当模板 / 图转可编辑失败，提示 soffice</b></summary>

这两条路在 Linux / macOS 上都要 LibreOffice。Debian/Ubuntu：`sudo apt install libreoffice-impress fonts-noto-cjk fonts-arphic-ukai`；
macOS：`brew install --cask libreoffice`。装在非常规位置就设 `SOFFICE_BIN=/path/to/soffice`。
Windows 上图转可编辑走 PowerPoint，不需要 LibreOffice；上传 pptx 做模板仍需要它（装好即可，程序会去默认安装目录找）。
</details>

<details>
<summary><b>能不能不联网、完全本地跑？</b></summary>

程序本身可以，但它依赖的图像模型和对话模型需要联网调用。如果你有本地部署的、提供 OpenAI 兼容接口的模型，
把 `base_url` 指向它就行。
</details>

---

## 部署到服务器

<details>
<summary>systemd + nginx 参考配置</summary>

```bash
cp deploy/ppt-generator.service /etc/systemd/system/     # 改 WorkingDirectory / ExecStart 里的路径
systemctl daemon-reload && systemctl enable --now ppt-generator
```

**nginx 反代必须关掉缓冲**，否则生成进度推送不出来（本项目用 SSE 推送实时进度）：

```nginx
location /api/ {
    proxy_pass http://127.0.0.1:8000;
    proxy_buffering off;
    proxy_read_timeout 3600s;
}
```

`deploy/nginx-zuoppt.conf` 是一份完整的线上参考配置（含 HTTPS、上传大小、静态资源缓存）。

**放到公网前请务必**：关掉开放注册（`OPEN_SIGNUP=0` 或面板里取消勾选），设置邀请码或改用一次性邀请码，
并确认 `AUTH_SECRET` 是随机值。`PPT_DATA_DIR` / `PPT_WORKSPACES_DIR` 可以把会长大的两个目录挪到别的盘。
`scripts/backup_db.py` 备份 SQLite。
</details>

---

## 给开发者

### 后端分层

```
api  →  services  →  { agent | render | library | editable }  →  { domain | infra }
```

同层之间可以互相 import，但整张图必须是 DAG。这条规则由 `scripts/check_layers.py` 检查（也跟着 pytest 一起跑）：
逆向依赖、循环依赖，以及「写在函数体里但其实不需要延迟的 import」都会被点名。

```
backend/app/
├── main.py            装配：create_app() 注册路由 + 启动钩子，不含业务
├── config.py          启动时从 .env 读死的常量（路径、密钥、开关）
│
├── api/               接口层：auth · session · library · account · admin · notice · editable · static
├── services/          编排层：SessionService（一次用户动作的完整链条：回合跑完要不要重渲、
│                      渲染完要不要质检）· EditableService（子进程里跑转换管线，计费与退款）
│
├── agent/             回合层：AgentTurn（跑一次回合）· ToolRegistry（@register 扩展工具）· prompts / vision
├── render/            渲染层：plan（估价与执行唯一口径）→ slide_renderer → job；
│                      image_router（通道优先级 / 熔断 / 失败切换）+ image_backend（图像 API 客户端）
├── library/           资产层：TemplateLibrary（摄取管线 + manifest 缓存）· StyleLibrary
├── editable/          图转可编辑：pipeline（stage 状态机）· segmenter · cutters · solver · renderer
│                      · stages · worker（独立子进程入口）
│
├── domain/            领域层：Session 状态机 · billing · costs · outline / style / prompt
│                      · generation_state（增量渲染）· exporter（图片 → pptx）· rasterize（pptx / pdf → 图片）
└── infra/             基础设施：db（core + repositories）· store · events（SSE）· runtime（可热改的配置）
                       · auth · ingest · alarm（上游计费 / 鉴权错误 → 管理员站内信）· sandbox
```

约定：**有状态的模块 = 类 + 模块底部装配一个单例**（`db.users.create(...)`、`store.sessions.save(...)`、
`bus.publish(...)`、`billing.service.estimate(...)`）；构造器一律零副作用，资源惰性初始化，
所以测试里换掉单例的落盘路径就能整套跑在 tmp 目录上（见 `tests/conftest.py`）。
**worker 不互相调用**：`AgentTurn` 与 `RenderJob` 都只跑完自己那一段并返回结果，「接下来干什么」由 `SessionService` 决定。

### 前端

React 18 + Vite，hash 路由，`api.js` 是唯一的后端调用面。

```
frontend/src/
├── main.jsx / App.jsx      入口、路由、未登录 → 展示页
├── pages/                  Home · Login · Settings · Billing · Inbox · StyleLibrary · TemplateLibrary
│   ├── Chat/               会话页：FeedItem · Cards · Deck · Composer
│   ├── Editable/           图转可编辑工作台（Workbench + parts/）
│   ├── Admin/              Overview · Users · Codes · Models · Health · Costs · Ledger · Notices
│   └── Landing/            中英双语展示页（framer-motion）
├── components/             Sidebar · Editor · DetailViewer · PickPanel · TermsModal · NoticePopup …
├── notify.js               提示音 / 标签页闪烁 / 桌面通知
└── styles/                 按区域切开的样式，index.css 的 @import 顺序即层叠顺序
```

**`web/` 是构建产物但随仓库发布**，这样普通用户不必安装 Node。改了前端记得 `npm run build` 后把 `web/` 一起提交。
`vite.config.js` 里的插件只保留 woff2 字体（中日韩字体按 unicode-range 拆成几百个子集，去掉 woff 回退后产物约 25MB）。

### 开发与测试

```bash
uvicorn backend.app.main:app --reload        # 后端热载
cd frontend && npm run dev                   # 前端热载（vite 把 /api 代理到 8000）
pytest -q                                    # 约 200 条，不联网、不花钱、不碰 data/
pytest --e2e                                 # 起两个真进程（应用 + 假 OpenAI 流式服务），多约 20 秒
python scripts/check_layers.py               # 依赖方向
```

冒烟测试用脚本化 LLM + `FAKE_IMAGE=1` 在进程内跑通 intake → style → outline → render → export，
断言状态迁移与积分增减；`test_auth_surface.py` 遍历真实路由表，公开接口必须显式登记理由。
CI（`.github/workflows/ci.yml`）在每次 push / PR 上跑后端测试与前端构建。

### 其它目录

- `promo/` — 宣传片（Remotion 工程、合成音效、字幕、封面、Logo）与成片 `promo_1080p.mp4`
- `docs/` — 产品介绍、新手教程源文件（线上版在 `frontend/public/help/`）
- `deploy/` — systemd 单元、nginx 参考配置、高级模式沙盒镜像 `runner.Dockerfile`
- `scripts/` — 官方素材生成入库、数据库备份、分层检查

---

## 仓库来历

这个仓库合并了之前的几个：`ppt_generator`（主应用，线上运行的版本）和 `ppt-editable`
（图转可编辑，在 Windows + PowerPoint 上实测的版本）。两条历史都保留在 git log 里；以线上版为准，
Windows 路线作为平台分支保留在同一份代码中。旧仓库已归档，只读。

## License

[MIT](LICENSE)
