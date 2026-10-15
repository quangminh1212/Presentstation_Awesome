# Discover

A growing catalog of **AI Factory skills** for Claude Code, organized by organization/domain.

각 폴더는 특정 기관·도메인을 위한 Claude Code skill 모음입니다. 각 skill은 자체 `SKILL.md` (또는 `skill.md`)와 frontmatter를 가지며, `~/.claude/skills/`에 복사·심볼릭링크하여 즉시 사용할 수 있습니다.

## Catalog

| 폴더 | 도메인 | 스킬 |
|------|-------|------|
| [`kist/`](./kist) | KIST (한국과학기술연구원) | `kist-brand-guidelines`, `kist-finder`, `kist-ppt` |

## Install skills

전체 폴더를 글로벌 스킬 디렉터리에 심볼릭링크하는 방법:

```bash
# clone
git clone https://github.com/aifactory-team/discover.git
cd discover

# install all KIST skills (symlink — 업데이트가 자동 반영)
for d in kist/*/; do
  name=$(basename "$d")
  ln -sfn "$(pwd)/$d" "$HOME/.claude/skills/$name"
done
```

또는 단일 스킬만 복사:

```bash
cp -r kist/kist-brand-guidelines ~/.claude/skills/
```

설치 후 Claude Code를 재시작하면 새 스킬이 인식됩니다.

## Contributing a new domain

1. 도메인 폴더 생성: `<organization-or-domain>/`
2. 그 안에 스킬 디렉터리들 추가 — 각각 `SKILL.md`/`skill.md`를 frontmatter 형식으로 작성
3. 도메인 폴더에 `README.md` — 스킬 목록 + 출처 + 라이선스 고지
4. PR

## Skill format

각 스킬 디렉터리는 다음 구조를 가집니다:

```
<skill-name>/
├── SKILL.md          # or skill.md (case insensitive)
│   ├── frontmatter: name, description (pushy 트리거 키워드 포함)
│   └── markdown body
├── assets/           # (선택) 이미지·로고·아이콘 등 정적 자산
├── reference/        # (선택) 토큰·참조 파일
├── examples/         # (선택) 사용 예시
└── scripts/          # (선택) 실행 스크립트
```

자세한 작성 가이드는 [Claude Code Skills 공식 문서](https://docs.anthropic.com/en/docs/claude-code/skills)를 참조.

## License & notices

- 코드와 스킬 정의는 [MIT License](./LICENSE)
- **개별 스킬에 포함된 제3자 자산(로고·이미지·데이터)은 해당 권리자 소유**입니다. 각 스킬 디렉터리 안의 `LICENSE_NOTICE.md`를 반드시 확인하세요.
- 본 저장소의 스킬은 **참조용**이며, 해당 기관 명의의 공식 산출물 제작에 사용하려면 해당 기관의 별도 허가가 필요합니다.

---

Maintained by [AI Factory](https://github.com/aifactory-team).
