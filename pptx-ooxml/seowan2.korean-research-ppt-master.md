<p align="center">
  <img src="assets/readme-hero.png" alt="Korean Research PPT Master workflow: Intake, Story, Visual, PPTX, QA" width="100%">
</p>

<h1 align="center">Korean Research PPT Master</h1>

<p align="center">
  한국어 연구·R&amp;D 발표자료를 기획부터 PPTX 제작·렌더링 검수까지 완주하는 Codex 마스터 스킬
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0.0-2563EB" alt="version 4.0.0">
  <img src="https://img.shields.io/badge/type-Codex%20Skill-111827" alt="Codex Skill">
  <img src="https://img.shields.io/badge/language-ko--KR-0F766E" alt="Korean">
  <img src="https://img.shields.io/badge/output-editable%20PPTX-EF6C00" alt="Editable PPTX">
</p>

## 한 문장으로 설명하면

**한 문장짜리 요청이나 연구 자료를 받아, 발표 목적에 맞는 스토리와 시각 문법을 설계하고 편집 가능한 PPTX와 검수용 montage까지 완성하는 한국어 연구 발표 전용 스킬입니다.**

단순히 텍스트를 슬라이드에 옮기지 않습니다. 발표 대상과 목적을 먼저 파악하고, 근거 자료를 구조화한 뒤, 슬라이드마다 가장 적합한 차트·도식·스크린샷·ImageGen figure를 선택합니다. 제작 후에는 실제 렌더링 결과를 확인하고 문제를 자동 수정합니다.

## 왜 필요한가

연구 발표자료는 내용만 맞는다고 완성되지 않습니다. 다음과 같은 문제는 정보의 신뢰도와 발표 설득력을 함께 떨어뜨립니다.

- 논문이나 보고서의 긴 문장을 그대로 붙여 넣은 슬라이드
- 배경·방법·결과가 평면적으로 나열되어 결론이 보이지 않는 구성
- 모든 내용을 카드 레이아웃에 넣어 관계와 중요도가 사라진 디자인
- `Baseline`을 “기준선”으로 쓰는 식의 어색한 번역체
- 수치를 차트 대신 장식용 큐브나 배지로 표현한 화면
- 화살표가 글자를 통과하거나 작은 글씨로 내용을 우겨 넣은 레이아웃
- 파일은 생성됐지만 실제 렌더링 상태를 확인하지 않은 결과물

Korean Research PPT Master는 이 문제들을 하나의 제작 파이프라인에서 다룹니다.

## 전체 워크플로

```text
요청 접수
  ↓
부족한 정보만 Intake
  ↓
발표 Brief 확정
  ↓
사용자 자료 분석 및 필요 시 외부 조사
  ↓
Story Architecture 설계
  ↓
슬라이드별 Archetype · Visual Grammar 결정
  ↓
한국어 연구 문체 적용 · Design System 확정
  ↓
편집 가능한 PPTX 제작
  ↓
Preflight · 전체 렌더링 · Montage 검수
  ↓
문제 자동 수정 후 최종 전달
```

처음에 필요한 정보를 한 번 확인한 뒤에는 중간 승인 요청을 반복하지 않고 제작과 검수를 자율적으로 진행합니다. 사용자가 이미 제공한 내용은 다시 묻지 않습니다.

## 핵심 기능

### 1. 필요한 것만 묻는 Intake

발표 대상, 목적, 시간 또는 장수, 자료 범위, 필수 내용, 디자인 제약 중 요청에서 알 수 없는 항목만 짧게 확인합니다. 사용자는 모르는 항목을 “알아서”라고 답해도 됩니다.

### 2. 발표를 위한 Story Architecture

문서 목차를 그대로 슬라이드 순서로 사용하지 않습니다. 각 장이 다음 장을 필요하게 만드는 흐름을 설계합니다.

- 연구 발표: `Context → Problem → Evidence → Goal → Approach → Experiment → Result → Interpretation`
- 정부 R&D 보고: `사업 목표 → 진행 현황 → 개발 내용 → 성과 → 이슈 → 대응 → 향후 일정`
- 실패 분석: `분석 대상 → 기준 → 전체 분포 → 주요 원인 → 진단 실험 → 결론`

원칙은 **한 슬라이드, 한 핵심 메시지**입니다.

### 3. 콘텐츠에 맞는 Slide Archetype

레이아웃을 먼저 고르고 내용을 끼워 넣지 않습니다. 슬라이드의 역할을 먼저 정의합니다.

- `COVER`: 제목과 최소 메타데이터만 사용하는 표지
- `SINGLE MESSAGE`: 하나의 주장과 dominant visual
- `RESULT CHART`: 정량 결과가 중심인 차트
- `ANNOTATED EVIDENCE`: 실제 화면·실험 증거와 주석
- `PROCESS / CAUSAL FLOW`: 단계 또는 인과관계
- `EXPERIMENT MATRIX`: 변수 조합과 Ablation
- `DECISION TREE`: 판정 규칙과 분기
- `SUMMARY`: 결론과 다음 행동

### 4. 정보 유형별 Visual Grammar

| 전달하려는 정보 | 우선 표현 |
|---|---|
| 비율·분포·순위 | bar, stacked bar, dot plot |
| 시간 변화 | line, area chart |
| 원인과 결과 | causal flow |
| 시스템 구성 | architecture diagram |
| 기존 방식과 제안 방식 | comparison |
| 변수 조합 | experiment matrix |
| GUI 오류와 실제 증거 | annotated screenshot |
| 핵심 수치 하나 | hero metric |
| 정확한 다차원 값 | table |
| 개념·구조·메커니즘 | ImageGen conceptual figure |

정확한 수치 비교에는 차트, 실제 증거에는 스크린샷, 개념과 흐름 설명에는 ImageGen을 사용합니다.

### 5. 자연스러운 한국어 연구 문체

영어 문장을 직역하지 않고 한국의 대학 연구실·기업 R&D·정부과제 발표에서 실제로 사용하는 표현으로 재구성합니다.

| 지양 | 권장 |
|---|---|
| 기준선 모델 | 베이스라인 모델 |
| 실제 세계에서의 성능 | 실환경 성능 |
| 물리적으로 근거된 데이터 | 물리 기반 데이터 |
| 요구된 업무를 수행하는 능력 | 실제 태스크 수행 성능 |
| 기존 방식에는 여러 한계가 존재한다 | 기존 방식의 한계 |

슬라이드 제목은 문장형 설명보다 짧고 명확한 **명사구형 정보 라벨**을 우선합니다.

### 6. 의미 전달형 ImageGen figure

v4부터 개념·구조·흐름·메커니즘 설명에 ImageGen을 활용할 수 있습니다. 생성 전 `Visual Brief`를 작성하고 다음 기준을 적용합니다.

- 입력·처리·출력 또는 비교 관계가 3초 안에 읽힐 것
- flat 또는 light semi-flat 기반의 학술적 벡터 스타일
- 짧은 라벨과 일관된 화살표로 읽는 방향을 명확히 할 것
- 의미 없는 3D, neon glow, 미래도시, 장식용 AI 이미지를 피할 것
- 실제 증거가 필요한 장에서는 생성 이미지가 스크린샷을 대체하지 않을 것

### 7. 편집 가능한 PPTX

가능한 한 텍스트는 native text, 표는 native table, 도식은 native shape, 차트는 편집 가능한 구조로 제작합니다. 중요한 정보를 한 장의 이미지로 평면화하지 않습니다.

### 8. 렌더링 기반 QA와 자동 수정

완성 선언 전에 최소 한 번은 `제작 → 렌더링 → 검수` 사이클을 수행합니다.

- 내용과 수치의 출처 일치
- 스토리 흐름과 결론의 근거
- 제목·본문의 시각 계층
- overflow, clipping, overlap, 이미지 왜곡
- connector와 텍스트 충돌
- 작은 글씨와 과도한 정보 밀도
- 동일 레이아웃 반복 여부와 전체 deck rhythm
- 번역체·AI식 추상 표현·보고서형 장문

## 설치

### 방법 1 — Git으로 설치

```bash
git clone https://github.com/seowan2/korean-research-ppt-master.git ~/.codex/skills/korean-research-ppt-master
```

Windows PowerShell:

```powershell
git clone https://github.com/seowan2/korean-research-ppt-master.git "$env:USERPROFILE\.codex\skills\korean-research-ppt-master"
```

### 방법 2 — ZIP으로 설치

1. GitHub의 **Code → Download ZIP**을 선택합니다.
2. 압축을 풉니다.
3. 폴더 이름을 `korean-research-ppt-master`로 맞춥니다.
4. 폴더 전체를 `~/.codex/skills/` 아래에 둡니다.
5. 다음 Codex 요청부터 스킬을 사용할 수 있습니다.

## 사용 방법

자연어로 연구 발표자료 제작을 요청하면 자동으로 선택될 수 있습니다. 명시적으로 호출하려면 `$korean-research-ppt-master`를 사용합니다.

```text
$korean-research-ppt-master
첨부한 논문을 바탕으로 교수님께 보고할 10분짜리 한국어 발표자료를 만들어줘.
결과와 Ablation을 강조하고, 디자인은 알아서 정해줘.
```

```text
$korean-research-ppt-master
정부과제 중간보고 PPT 15장으로 만들어줘.
내가 제공한 자료만 사용하고, 개발 진척도와 정량 성과를 중심으로 구성해줘.
```

```text
$korean-research-ppt-master
GUI Agent 실패 분석 결과를 학회 발표 스타일로 정리해줘.
실제 오류 화면은 스크린샷으로, 실패 메커니즘은 개념 도식으로 보여줘.
```

정보가 부족하면 스킬이 다음 중 필요한 항목만 묻습니다.

- 발표 대상과 목적
- 발표 시간 또는 목표 장수
- 사용할 자료의 범위
- 반드시 포함하거나 제외할 내용
- 디자인 방향
- 기존 템플릿·로고·폰트·비율 제약

## 기본 산출물

- 편집 가능한 `.pptx`
- 전체 슬라이드 montage `.png`

요청에 따라 PDF, 개별 슬라이드 미리보기, 발표자 노트, source manifest, brief를 추가할 수 있습니다.

## PPTX Preflight

`scripts/pptx_preflight.py`는 완성된 PPTX에서 표지 과밀, 텍스트 블록 과다, 작은 글씨, 텍스트·connector 충돌 가능성을 빠르게 검사합니다.

```bash
pip install python-pptx
python scripts/pptx_preflight.py path/to/output.pptx
```

```text
PREFLIGHT PASS
```

또는 문제가 있는 슬라이드와 이유를 경고로 출력합니다. **Preflight 통과는 시각 검수를 대체하지 않습니다.** 실제 렌더링 이미지와 전체 montage를 함께 확인해야 합니다.

## 기본 디자인 방향

reference deck이 없으면 `Editorial Research Minimal`을 기본값으로 사용합니다.

- 강한 타이포그래피 계층
- 충분한 여백과 명확한 그리드
- neutral background와 제한된 accent color
- 장식보다 데이터·근거·도식 우선
- 슬라이드마다 하나의 dominant visual
- 같은 레이아웃을 반복하지 않는 deck-level rhythm

## 파일 구조

```text
korean-research-ppt-master/
├── SKILL.md
├── README.md
├── assets/
│   └── readme-hero.png
├── references/
│   ├── design-system.md
│   ├── geometry-rules.md
│   ├── imagegen-visualization.md
│   ├── intake.md
│   ├── korean-language.md
│   ├── quality-gates.md
│   ├── slide-archetypes.md
│   ├── story-architecture.md
│   └── visual-grammar.md
└── scripts/
    └── pptx_preflight.py
```

`SKILL.md`는 단일 진입점입니다. 세부 규칙은 필요한 제작 단계에서만 `references/`의 문서를 읽도록 구성되어 있습니다.

## 요구 환경

- Agent Skills 형식을 지원하는 OpenAI Codex
- PPTX 생성 및 렌더링이 가능한 환경 권장
- 개념 figure 생성 시 내장 ImageGen 사용 가능 환경 권장
- Preflight 실행 시 Python 3와 `python-pptx`

## 설계 원칙

1. 콘텐츠가 레이아웃을 결정합니다.
2. 한 슬라이드에는 하나의 핵심 메시지를 둡니다.
3. 정량 비교는 차트, 실제 증거는 스크린샷, 개념·구조는 도식으로 표현합니다.
4. 한국 연구 현장에서 통용되는 용어를 억지로 번역하지 않습니다.
5. 장식보다 근거와 정보의 위계를 우선합니다.
6. 작은 글씨로 해결하지 않고 내용을 압축하거나 슬라이드를 분할합니다.
7. 렌더링 결과를 확인하기 전에는 완성으로 간주하지 않습니다.

## 버전

현재 버전은 **4.0.0**입니다.

- v4: ImageGen 기반 학술용 개념 figure와 semantic clarity 검수 추가
- v3: Slide Archetype, geometry hard rules, PPTX preflight 추가
- v2: Intake부터 제작·렌더링 QA까지 단일 마스터 워크플로 통합

## 기여

개선 제안과 실제 사용 중 발견한 실패 사례는 Issue로 남겨주세요. 문체 규칙, 시각 문법, QA 기준을 변경하는 Pull Request에는 어떤 유형의 발표자료에서 문제가 발생했는지와 기대 동작을 함께 적어주면 검토에 도움이 됩니다.
