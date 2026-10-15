# PPT MCP

以 Node.js 實作的 PowerPoint (.pptx) MCP Server，供 Cursor Agent 讀寫簡報。

## 安裝

```bash
cd ppt-mcp
npm install
npm run build
```

## Cursor 設定

在 Cursor MCP 設定中加入：

```json
{
  "mcpServers": {
    "PPT MCP": {
      "command": "node",
      "args": ["D:/Oscar/Projects/cursor-work-space/ppt-mcp/dist/index.js"],
      "cwd": "D:/Oscar/Projects/cursor-work-space/ppt-mcp",
      "env": {
        "PPT_MCP_ROOT": "D:/Oscar/Projects/cursor-work-space/ppt-mcp"
      }
    }
  }
}
```

## 目錄

| 目錄 | 用途 |
|------|------|
| `sourcePresentations/` | 唯讀範本 `.pptx` |
| `resultPresentations/` | 輸出 `.pptx` |
| `assets/` | 圖片等資源（`addPicture` 使用） |

## 工具

- `listSourcePresentations` / `listResultPresentations`
- `manageResultPresentations`
- `readPresentation` / `getSlide`
- `writePresentation`
- `addSlide` / `deleteSlide` / `setShapeText` / `addPicture`

詳見 [PPT-MCP-SPEC.md](./PPT-MCP-SPEC.md)。

## 開發

```bash
npm run dev    # tsx 直接執行
npm test       # vitest
```
