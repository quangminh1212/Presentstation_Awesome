<div align="center">

# OfficeAI.Chat

### 原 PptGPT — 一站式 AI 智能幻灯片生成插件，可结合个人知识库生成精准匹配答辩、演讲、汇报场景的 PPT 幻灯片内容及原创配图

[English](./README_En.md) | 简体中文

[![Platform](https://img.shields.io/badge/平台-Windows%20%7C%20macOS%20%7C%20信创%20%7C%20Linux-blue?style=flat-square)](https://github.com/OfficeAIWork/PptGPT)
[![Office](https://img.shields.io/badge/适配-Office%20%7C%20WPS-orange?style=flat-square)](https://github.com/OfficeAIWork/PptGPT)
[![License](https://img.shields.io/badge/许可-Proprietary-red?style=flat-square)](https://github.com/OfficeAIWork/PptGPT)

[下载软件](#-软件下载) · [功能介绍](#-软件使用) · [安装教程](#-软件安装) · [联系我们](#-联系我们)

---

</div>

## 软件简介

OfficeAI.Chat（原 PptGPT）是一款智能幻灯片生成插件，可结合个人知识库生成精准匹配答辩、演讲、汇报场景的 PPT 幻灯片内容及原创配图，也支持通过润色及翻译功能优化 PPT 内容。

| 核心能力                    | 说明                                                               |
| :-------------------------- | :----------------------------------------------------------------- |
| **智能幻灯片生成**    | 输入主题自动生成演示方案与提纲，一键生成带排版内容的 PPT 演讲稿    |
| **润色与改写**        | 疏通润色、扩写、缩写，自动优化 PPT 文案表达                        |
| **思维导图与配图**    | 根据关键词生成思维导图，根据描述生成原创幻灯片配图                 |
| **OfficeAI智能体**        | 多模态智能助手，支持总结PPT、生成图表/思维导图/图片、辅助编辑PPT格式 |

> **适配环境：** Windows 系统（推荐 Win10+）· 苹果 macOS · 国产信创系统 · Linux 系统 · Office 2012+ · WPS 最新版

---

## 软件安装

### 软件下载

| 下载渠道 | 链接                                                                |
| :------- | :------------------------------------------------------------------ |
| 官方网站 | [https://officeai.chat](https://officeai.chat)                       |

#### 各平台安装包下载

| 安装包 | 平台 | 大小 | 下载链接 |
| :--- | :--- | :--- | :--- |
| OfficeAI.Chat-Windows.rar | Windows 10/11 (x64) | ~74 MB | [下载](https://github.com/OfficeAIWork/PptGPT/releases/download/v1.0.0/OfficeAI.Chat-Windows.rar) |
| OfficeAI.Chat-macOS.rar | macOS 10.15+ (Intel/Apple Silicon) | ~182 MB | [下载](https://github.com/OfficeAIWork/PptGPT/releases/download/v1.0.0/OfficeAI.Chat-macOS.rar) |
| OfficeAI.Chat-Linux.rar | Linux (Ubuntu/CentOS 等) | ~113 MB | [下载](https://github.com/OfficeAIWork/PptGPT/releases/download/v1.0.0/OfficeAI.Chat-Linux.rar) |
| OfficeAI.Chat-DomesticOS.rar | 信创系统 (UOS/Kylin) | ~161 MB | [下载](https://github.com/OfficeAIWork/PptGPT/releases/download/v1.0.0/OfficeAI.Chat-DomesticOS.rar) |

> [!IMPORTANT]
> 安装前请关闭 Office、WPS 等相关软件；部分无管理员权限的电脑建议先关闭杀毒软件，安装完成后再开启。

### 安装步骤

**第一步：安装插件**

双击或以管理员身份运行 `setup.exe`，按向导依次点击【下一步】完成安装。

![安装界面](./Images/01-setup.png)

![安装步骤](./Images/02-installation-steps.png)

**第二步：确认安装**

进入 Office（PowerPoint / WPS 演示）后点击确认安装。

![Office 确认安装](./Images/03-office-confirm.png)

### 软件升级

点击【升级软件】按钮即可自动检查并更新到最新版本。如有新版本，等待下载完成后按向导步骤执行更新安装，完成后重新打开 PowerPoint 或 WPS 即可。

|              升级菜单              |              升级界面              |
| :--------------------------------: | :--------------------------------: |
| ![升级菜单](./Images/08-update-menu.png) | ![升级界面](./Images/09-update-screen.png) |

### 登录与模型配置

#### 方式一：用户登录（目前免费）

![登录界面](./Images/04-login.png)

- 勾选「OfficeAI.Chat 模型服务」，输入用户名和密码点击【确定】
- 新用户点击【免费注册】注册账号后登录
- 忘记密码可通过手机号重置

#### 方式二：自定义模型 API（永久免费）

![自定义 API](./Images/05-custom-api.png)

勾选「自定义模型服务」，按以下步骤配置：

| 配置项            | 说明                                                                                        |
| :---------------- | :------------------------------------------------------------------------------------------ |
| **模型 ID** | 推荐：深度求索 DeepSeek-V4-Flash、智谱 GLM5.1、阿里 Qwen3.7-Max、OpenAI GPT-5.5（境外用户） |
| **API Key** | 进入大模型管理后台复制 API Key 并粘贴                                                       |
| **API Url** | 进入大模型管理后台复制 API Url 并粘贴（注意末尾需带 `/v1` 版本号）                        |

> [!TIP]
> 软件已预置 DeepSeek、智谱、阿里百炼等主流平台的标准地址，选择后自动填入。内网可通过 Ollama 完全离线使用，地址格式：`http://[服务器IP]:11434/v1`

---

## 软件使用

### 功能菜单

![](./Images/10-feature-menu.png)


### OfficeAI 智能体

![智能体界面](./Images/07-officeai-agent.png)

OfficeAI 智能体是具备自主任务拆解与执行能力的办公智能助手。仅需下达自然语言目标，智能体自动规划流程、落地执行，代替枯燥繁琐的手工操作。

#### 内容编辑与处理

| 功能     | 说明                               |
| :------- | :--------------------------------- |
| 润色改写 | 优化文字表达，让语句更流畅、专业   |
| 扩写丰富 | 在原文基础上扩展内容，增加细节描述 |
| 缩写精简 | 在不改变原意的情况下精简文字       |
| 翻译     | 中英文互译，自动识别源语言         |

#### 智能生成

| 功能     | 说明                                     |
| :------- | :--------------------------------------- |
| 思维导图 | 根据关键词生成总结型或头脑风暴型思维导图 |
| 智能配图 | 根据描述生成原创幻灯片配图               |
| 知识图谱 | 可视化展示概念之间的关系                 |

> [!TIP]
> 可以这样跟智能体交流：
>
> - 「总结这份PPT的摘要」
> - 「把这段文字润色得更专业一些」
> - 「根据人工智能这个关键词生成思维导图」
> - 「帮我生成一张科技风格的配图」
> - 「把选中文本翻译成英文」

---

### 生成幻灯片

点击【幻灯片生成】按钮进入设置界面：

**第一步：设置生成参数**

下拉框中没有的选项可以在文本框中手动输入。

![设置参数](./Images/12-set-parameters.gif)

**第二步：生成方案**

输入幻灯片主题，点击【生成方案】自动生成演示方案，生成后可自定义编辑调整，不满意可重新生成。

![生成方案](./Images/13-generate-plan.gif)

**第三步：应用提纲**

将提纲插入当前模板，或基于提纲自动生成带主题及内容的演讲稿。

![生成 PPT](./Images/14-generate-ppt.gif)

### 润色

选择需要改写的文本内容，按默认选择不同模式（精确、平衡、创新）的【疏通润色】功能，自动优化润色当前选中文本。

> [!NOTE]
> 从精确方案到创新方案，内容呈现逐步丰富。精确模式聚焦原文改写，创新模式发散扩展，可根据创作需求选择。

### 改写（扩写 / 缩写）

- **扩写**：选中短语点击【扩写】，在原文基础上丰富内容
- **缩写**：选中段落点击【缩写】，在不改变原意的情况下精简文字

### 中英互译

将选中文本的内容进行中英文转换。

### 思维导图

选中关键词，点击【思维导图】，自动生成总结型或头脑风暴预测型思维导图。

![生成思维导图](./Images/15-generate-mind-map.gif)

### 智能配图

选中关键字或短语，点击【智能配图】，自动生成原创幻灯片配图。

![智能配图](./Images/16-smart-illustration.gif)

## 软件卸载

在 Windows 控制面板 → 程序和功能 中找到「OfficeAI.Chat 办公智能体套包」，右键选择【卸载】即可。

![卸载](./Images/22-uninstall.png)

---

## 联系我们

微信联系我们，微信号：**WordGPT_KF**

<div align="center">

![客服微信](./Images/21-wechat-support.png)

---

*如果这个项目对你有帮助，请给我们一个 Star 支持！*

</div>
