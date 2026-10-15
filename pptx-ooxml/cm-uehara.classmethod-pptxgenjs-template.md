# classmethod-pptxgenjs-template

クラスメソッドのスライドデザインに沿った PPTX スライドを AI で作成するためのテンプレートです。

## 概要

[classmethod-marp-theme](https://github.com/classmethod/classmethod-marp-theme) のデザイン（カラーパレット、タイポグラフィ、レイアウト構成）を参考に、 [PptxGenJS](https://gitbrent.github.io/PptxGenJS/) 向けに変換したテンプレートを提供します。Anthropic 公式の pptx スキルと組み合わせて使用します。

## セットアップ

### 1. pptx スキルのインストール

Anthropic 公式の pptx スキルを事前にインストールしてください。

https://github.com/anthropics/skills/tree/main/skills/pptx

方法は任意ですが、 [skills.sh](https://skills.sh/) を利用する場合は以下でインストールが可能です。

```bash
npx skills add https://github.com/anthropics/skills --skill pptx
```

### 2. 依存関係のインストール

```bash
npm install
```

### 3. テンプレートの生成（任意）

※生成AIを活用して PptxGenJS でゼロから作成する場合はスキップできます。

```bash
node template/generate-template.js
```

## プロジェクト構成

```
classmethod-pptxgenjs-template/
├── AGENTS.md                          # AI エージェント向けスライド作成ガイド
├── .agents/skills/pptx/               # pptx スキル（セットアップ 1. でインストール）
├── template/
│   ├── theme.js                       # テーマ定数（カラー、フォント、サイズ）
│   ├── generate-template.js           # テンプレート生成スクリプト
│   ├── classmethod-template.pptx      # 生成されたテンプレート（18レイアウト）
│   └── TEMPLATE.md                    # レイアウト仕様ドキュメント
└── package.json
```

## 収録レイアウト

テンプレートには 18 種類のスライドレイアウトが含まれています。

| # | レイアウト | 用途 |
|---|----------|------|
| 1 | タイトル | 表紙（ロゴ + タイトル + サブタイトル） |
| 2 | セクション区切り | 章の導入 |
| 3 | 標準コンテンツ | ヘッダー付き箇条書き |
| 4 | ヘッダーなし | フルコンテンツ |
| 5 | 画像中央 | 図表の表示 |
| 6 | テキスト＋図（右） | 左テキスト・右画像 |
| 7 | テキスト＋図（左） | 左画像・右テキスト |
| 8 | 2カラム | 2列比較 |
| 9 | 3カラム | 3列並列 |
| 10 | 主要指標 | KPI カード |
| 11 | プロセス | タイムライン |
| 12 | 比較 | Before / After |
| 13 | アイコングリッド | 機能・特徴一覧 |
| 14 | 引用 | キーメッセージ |
| 15 | アジェンダ | 目次 |
| 16 | テーブル | データ表 |
| 17 | 青アクセント | 強調セクション |
| 18 | クロージング | 締め |

## 使い方

セットアップ完了後、このプロジェクトをワークスペースとして開き、AI エージェントにスライド作成を依頼します。

### Cursor の場合

Agent モードでプロンプトを入力します。

```
AWSのコスト最適化について、スライドを作って
```

```
以下の内容でプレゼン資料を作成してください。
- タイトル: サーバーレスアーキテクチャ入門
- 対象: エンジニア向け社内勉強会
- ページ数: 8ページ程度
```

### Claude Code の場合

ターミナルから直接依頼できます。

```bash
claude "/your-path/documents の資料を参考に、AWSを利用したインフラ基盤構築の事例について、6ページのスライドを作って"
```

### Tips

- テーマやレイアウトの指定は不要です。`AGENTS.md` を読んだエージェントが自動的にクラスメソッドのブランドテーマを適用します
- ページ数を指定すると意図に近い分量になります
- 画像を含めたい場合は、ファイルパスや URL を伝えてください

### 参考

- `AGENTS.md` — AI エージェント向けのスライド作成ガイド
- `template/TEMPLATE.md` — 全18レイアウトの詳細仕様

---

本リポジトリはクラスメソッド社の内部使用を目的として作成されています。
