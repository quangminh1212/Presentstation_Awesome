# ai-agent-zhihu-skill

知乎开放平台官方 API 的 AI Agent Skill——不依赖浏览器 cookie、不搞逆向、不爬虫（Hermes skill 名：`zhihu-open-platform`）。

**覆盖官方全部 18 个 API 端点**（2026-09-29 文档快照）：知乎搜索、热榜、全网搜索、知乎直答、每日额度、问题推荐、问题回答列表、我的创作/全文/评论、创作数据统计、我的关注、近期收藏、收藏夹、收藏夹内容、PDF 解析、PPT 生成。附带 Python 脚本，设置一个环境变量即可用。

## 快速使用

```bash
# 1. 设置 Access Secret（从 https://developer.zhihu.com/profile 获取）
export ZHIHU_ACCESS_SECRET=your_...

# 2. 直接跑脚本
python3 scripts/zhihu-search.py '{"query":"RAG 评测","count":5}'
python3 scripts/hot-list.py '{"limit":10}'
python3 scripts/quota.py '{}'                       # 每日额度（免费）
python3 scripts/user-favlists.py '{"limit":20}'     # 我的收藏夹
python3 scripts/favlist-contents.py '{"favlist_url_token":36433780,"limit":10}'
python3 scripts/ppt-generation.py '{"command":"run","resource_url":"https://www.zhihu.com/question/1/answer/2","num_pages":12}'
```

所有脚本 Python stdlib-only，零依赖，输出归一化 JSON（键转 snake_case），错误统一 `{"error":"...","exit_code":1}`。脚本会自动加载 skill 目录下的 `.env`。

## 覆盖的端点

| 端点 | 脚本 | 用途 |
| --- | --- | --- |
| `zhihu_search` | `scripts/zhihu-search.py` | 搜索知乎问题、回答、文章 |
| `hot_list` | `scripts/hot-list.py` | 知乎实时热榜 |
| `global_search` | `scripts/global-search.py` | 全网搜索（非知乎专用） |
| `zhida` | `scripts/zhida.py` | 知乎直答（LLM 驱动） |
| `quota` | `scripts/quota.py` | 每日额度查询（免费） |
| `question_recommendations` | `scripts/question-recommendations.py` | 适合回答的问题推荐 |
| `question_answers` | `scripts/question-answers.py` | 问题下的回答列表（分页） |
| `user_contents` | `scripts/user-contents.py` | 我的创作列表 |
| `user_content_detail` | `scripts/user-content-detail.py` | 我的创作全文 |
| `user_content_comments` | `scripts/user-content-comments.py` | 我的创作评论 |
| `creator_account_stats` | `scripts/creator-account-stats.py` | 账号维度创作数据 |
| `creator_content_stats` | `scripts/creator-content-stats.py` | 单篇创作数据 |
| `user_followees` | `scripts/user-followees.py` | 我的关注列表 |
| `user_collections` | `scripts/user-collections.py` | 我的近期收藏 |
| `user_favlists` | `scripts/user-favlists.py` | 我的收藏夹列表 |
| `favlist_contents` | `scripts/favlist-contents.py` | 收藏夹内容（分页） |
| `pdf_parse` | `scripts/pdf-parse.py` | PDF 异步解析（上传→任务→轮询） |
| `ppt_generation` | `scripts/ppt-generation.py` | 回答/文章 → PPTX 异步生成 |

每个端点的 API 规格、参数表、curl 示例见 `references/`；统一 MCP 端点见 `references/mcp.md`。

## 安装

Hermes Agent：

```bash
git clone https://github.com/kids0cn/ai-agent-zhihu-skill.git
cp -r zhihu-open-platform ~/.hermes/skills/
# 或软链接：
ln -s $(pwd)/zhihu-open-platform ~/.hermes/skills/
```

多 Agent 共享：

```bash
cp -r zhihu-open-platform ~/.agents/skills/
```

## 配置

### 必需

| 变量 | 说明 |
| --- | --- |
| `ZHIHU_ACCESS_SECRET` | Bearer auth token，从 https://developer.zhihu.com/profile 获取 |

### 可选

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `ZHIHU_OPENAPI_BASE_URL` | `https://developer.zhihu.com` | 所有端点的基础 URL |
| `ZHIHU_<ENDPOINT>_URL` | — | 单端点覆盖（如 `ZHIHU_HOT_LIST_URL`） |
| `ZHIHU_PDF_PARSE_URL` / `ZHIHU_PPT_GENERATION_URL` | — | 覆盖 pdf/ppt 任务 API base |

也可以在 skill 目录创建本地 `.env`（`.gitignore` 已排除，`chmod 600`）：

```bash
echo 'ZHIHU_ACCESS_SECRET=your_...' > <skill-dir>/.env
chmod 600 <skill-dir>/.env
```

## 文件结构

```
zhihu-open-platform/
├── SKILL.md                    # Skill 正文（决策逻辑、鉴权、错误处理）
├── scripts/                    # 18 个端点脚本（stdlib-only）
│   ├── zhihu-search.py         # 知乎搜索
│   ├── hot-list.py             # 热榜
│   ├── global-search.py        # 全网搜索
│   ├── zhida.py                # 直答
│   ├── quota.py                # 额度查询
│   ├── question-recommendations.py / question-answers.py
│   ├── user-contents.py / user-content-detail.py / user-content-comments.py
│   ├── creator-account-stats.py / creator-content-stats.py
│   ├── user-followees.py / user-collections.py / user-favlists.py / favlist-contents.py
│   ├── pdf-parse.py            # 异步：upload → create → poll
│   └── ppt-generation.py       # 异步：create → poll
├── references/                 # 20 篇（全端点 API 规格 + 脚本用法 + curl）
│   ├── official-api.md         # 全端点索引、认证、额度表、错误码
│   └── mcp.md                  # 统一 MCP 端点
└── agents/
    └── openai.yaml             # OpenAI Agents SDK 接口配置
```

## 额度（免费档，以 `quota.py` 实时返回为准）

搜索类 5000/日、热榜/问题发现/直答/创作能力 100/日、知乎用户数据 10000/日、PDF+PPT 小工具 10/日（任务成功才计数）。

## 依赖

- [知乎开放平台](https://developer.zhihu.com) 账号及 Access Secret
- Python 3（脚本 stdlib-only，无 pip 依赖）
- 支持 skill 文件的 AI Agent 平台（Hermes、OpenAI Agents SDK 等）

## License

MIT
