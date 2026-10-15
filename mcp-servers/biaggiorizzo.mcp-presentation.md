# Exemplos práticos de MCP (Model Context Protocol) em Python

O **MCP** é um protocolo aberto que padroniza como aplicações de IA (LLMs) se conectam a dados e ferramentas externas. Este repositório reúne servidores MCP completos, escritos em Python com o SDK oficial (`FastMCP`), que demonstram na prática as três primitivas do lado do servidor — **Resources**, **Tools** e **Prompts**.

## Exemplos

| Exemplo | O que demonstra |
|---|---|
| [`01_pizzaria_mcp`](./01_pizzaria_mcp) | Um atendente de pizzaria com **estado em memória**: a IA lê cardápio e estoque (Resources), faz pedidos que debitam ingredientes de verdade (Tools) e segue um roteiro de atendimento (Prompt). |
| [`02_docker_controller`](./02_docker_controller) | A IA conectada a uma **ferramenta real da sua máquina**: lista containers, lê logs, reinicia serviços via CLI do Docker — e mostra como validar argumentos antes de executar ações sensíveis. |

## Pré-requisitos

- **Python 3.10+**
- **Docker** (apenas para o exemplo 02)
- Um cliente MCP (Claude Desktop, Cline/RooCode, etc.) — ou nenhum: cada exemplo pode ser testado direto no navegador com o **MCP Inspector** (`mcp dev server.py`)

## Como começar

```bash
cd 01_pizzaria_mcp        # ou 02_docker_controller
pip install -r requirements.txt
mcp dev server.py         # abre o MCP Inspector no navegador
```

Cada pasta tem um README com o passo a passo de configuração nos clientes MCP e um roteiro de prompts prontos para testar.

## Segurança

Os exemplos são didáticos. Antes de conectar um LLM a sistemas reais, valide argumentos de tools, limite as permissões de cada servidor e leia o [OWASP Top 10 para LLMs](https://genai.owasp.org/llm-top-10/).

## Autor

**Biaggio Rizzo** — Desenvolvedor Backend

- 🌐 [biaggiorizzo.dev](https://biaggiorizzo.dev/)
- 💼 [LinkedIn](https://www.linkedin.com/in/biaggio-rizzo)
