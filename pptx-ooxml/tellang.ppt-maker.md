# ppt-maker

정부 업무보고 스타일 PPTX 생성기. PptxGenJS + Noto Sans KR 기반.

## 특징

- 다크 헤더 + 탭 네비게이션 + 카드 레이아웃
- SVG 아이콘 (이모지 없음)
- Noto Sans KR 4단계 weight (Black/Medium/Regular/DemiLight)
- 이미지 비율 자동 보정 (fitImg)
- 사진 캡션 오버레이

## 사용법

```bash
npm install
node src/generate.mjs
```

## 디자인 시스템

| 역할 | 색상 |
|------|------|
| Accent | `#16A34A` (초록) 또는 `#2563EB` (블루) |
| Dark BG | `#111111` |
| Content BG | `#F9FAFB` |
| Text | `#1F2937` / `#374151` / `#6B7280` |

## 파일 구조

```
src/
  generate.mjs      # PPTX 생성 메인 스크립트
assets/
  optimized/         # 최적화된 이미지
docs/
  BUILD_PRD.md       # Opus 플러그인용 빌드 PRD
  PHOTO_POLISHING_PRD.md
  THEME_FONT_PRD.md
  POLISHING_PRD.md
  gov-briefing-style.md  # 디자인 시스템 레퍼런스
```

## 참고

- [gov-briefing-pptx-wooseokjin](https://github.com) — 디자인 시스템 원본
- [PptxGenJS](https://github.com/gitbrent/PptxGenJS) — PPTX 생성 라이브러리
