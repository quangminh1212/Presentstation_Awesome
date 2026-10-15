# MCP Presentation

Proyecto público de presentación con Playwright MCP para pruebas automatizadas.

## Requisitos

- Node.js (v18 o superior recomendado)
- npm (v9 o superior)
- Git
- Visual Studio Code

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/matnoon/MCP-Presentation.git
   cd MCP-Presentation
   ```
2. Instala las dependencias:
   ```sh
   npm install
   ```
3. Instala Playwright y navegadores:
   ```sh
   npx playwright install
   ```
4. Instala y configura MCP siguiendo la documentación oficial:
   [Visual Studio Code MCP](https://code.visualstudio.com/mcp)

## Estructura del proyecto

- `pages/` - Page Object Models
- `tests/` - Pruebas automatizadas
- `mcp.config.json` - Configuración MCP
- `playwright.config.ts` - Configuración Playwright
- `MCP Test/` - Carpeta pública para recursos compartidos
- `MCP-Explanation.md` - Explicación en inglés sobre MCP y ventajas

## Uso

- Ejecuta el servidor MCP:
  ```sh
  npx playwright-mcp server
  ```
- Corre los tests:
  ```sh
  npx playwright test
  ```

## Referencias
- [Visual Studio Code MCP](https://code.visualstudio.com/mcp)
