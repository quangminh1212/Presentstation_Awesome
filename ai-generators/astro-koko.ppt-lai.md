<p align="center">
  <img src="assets/hero/hero-main.png" alt="ppt-lai：一个非常不艺术的 PPT skill" width="50%" />
</p>


# ppt-lai

> 大喊一声「PPT，来！」，一份历经岁月沉淀、史书认证的专业 PPT 闪亮登场！！！

这是一个充满艺术细菌的ppt制作 skill, 你给它一个主题、几页旧稿，或者一堆还没整理好的材料；它交付一份 4:3、原生可编辑、的 `.pptx`

<p>
  <img src="https://img.shields.io/github/v/release/astro-koko/ppt-lai" alt="latest release" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT license" />
  <img src="https://img.shields.io/badge/output-editable%20.pptx-red" alt="editable pptx" />
</p>

## 先睹为快

目前项目内置三档口味，任君挑选

<img src="assets/patina/l1-l2-l3.png" alt="L1、L2、L3 三档千禧年风格 PPT 对比" width="100%" />

| 档位 | 时间感 | 看起来像 |
| --- | --- | --- |
| **L1** | 2007–2010 | 还没完全离开 Office 模板的旧课件 |
| **L2**（默认） | 2003–2006 | 充满主讲人小巧思的祖传课件 |
| **L3** | 2000–2002 | 从“清朝”挖掘出土，人走PPT还在 |

## 交付物

最后落地的是一个真的 `.pptx` 文件。打开后，字还能选，颜色能换，形状能拖，标题上的描边和阴影也不是一张图片

你可以从一句话开始，也可以把定稿旧稿交过来。新稿会按主题组织页面；旧稿只换视觉，源文件里的文字、数字、年份和人名逐字保留。

## 使用案例

##### 做一份新稿

适合只有一个想法、一个提纲，或者一批资料的时候。

```text
用 ppt-lai 做一份「区块链在文化遗产保护中的应用」PPT。
面向学院分享，8 页，默认 L2；事实以我提供的材料为准，输出原生可编辑 .pptx。
```

主题 / 材料 → 整理内容和页序 → 事实审校 → 生成可编辑 `.pptx`

##### 翻新一份旧稿

适合内容已经定稿，只想让它看起来像一份真正流通过的老课件。

```text
用 ppt-lai 把这份年终总结.pptx 翻新成 L3 千禧年风格。
正文、数字、年份和人名逐字保留，只改视觉。
```

旧 `.pptx` → 提取原文 → 只换视觉 → 内容冻结复检 → 可编辑 `.pptx`

这条路只动字体、配色、标题特效、背景、对齐和使用痕迹。它不会替你润色、总结或“优化表达”。

## 安装

##### Claude Code / CodeBuddy

```text
/plugin marketplace add astro-koko/ppt-lai
/plugin install ppt-lai@ppt-lai
```

##### Codex

```text
使用 $skill-installer 安装 astro-koko/ppt-lai 仓库中的 skills/ppt-lai
```

##### WorkBuddy

从 [Releases](https://github.com/astro-koko/ppt-lai/releases) 下载 `ppt-lai-<version>.skill`，然后在 Skills 页面导入。

安装完成后，把主题、材料或 `.pptx` 交给 AI。真正生成或解析前，它会检查 Python 3.10+ 和所需依赖；条件不满足时会停下来说明原因。

## 项目背景

现在的AI 把 PPT 做得越来越漂亮了，可漂亮得都没了味道 ,经过我的不“屑”努力,把濒临失传的”清朝ppt”接回来了，发扬传统ppt制作工艺吾辈有责！

## 项目里较真的地方

- 这里的“丑”有出处。视觉可以穿越，事实不用穿越；现代主题按今天的事实来写
- 构建前后做事实检查；`density_guard()` 和 `diversity_guard()` 会拦住过度堆叠和整套页面复制同一套参数。
- 已经17个主题做回归测试，覆盖历史、文化、技术和现代主题。
- 运行时只维护一份：[`skills/ppt-lai`](skills/ppt-lai/)。交付物始终是原生对象，不是整页截图



## License

MIT
