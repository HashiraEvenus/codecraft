# CodeCraft — Local Architecture

## Stack Overview

| Layer | Choice | Why |
|---|---|---|
| Frontend framework | React + TypeScript + Vite | Fast DX, strong ecosystem, Vite build is fast |
| Styling | Tailwind CSS v3 | Utility-first, no context switching, consistent dark theme |
| Code editor | Monaco Editor (`@monaco-editor/react`) | Same engine as VS Code — syntax highlighting, IntelliSense, multi-language, theming out of the box. CodeMirror is lighter but Monaco wins on features for a coding platform |
| AI generation | Google Gemini | Uses the user's own local API key for challenge generation |
| Code execution | Local subprocess runner | No hosted execution API, no per-run cost, useful for personal practice |
| Backend | FastAPI (Python) | Simple local API for generation and execution |
| Routing | React Router v6 | Standard, lightweight |
| HTTP client (FE) | Axios | Clean interceptors, consistent error handling |
| Icons | Lucide React | Consistent, lightweight, tree-shakeable |

## Product Direction

CodeCraft is a local-first personal practice tool, not a hosted SaaS. There is no pricing layer, Pro mode, hosted code execution, or license-key flow.

## Code Execution Flow

```
User writes code → POST /api/execution/run → local Python/Node/tsx command → stdout/stderr returned
User submits → POST /api/execution/test → backend runs each test case locally → pass/fail per case
```

Test validation: the backend appends `print(test_case_input)` to the user's code and compares stdout to expected output.

Execution happens on the same machine running the backend. This is convenient for personal use, but it is not safe for public untrusted users.

## AI Challenge Generation

```
User picks topic + difficulty + language → POST /api/challenges/generate
→ Gemini prompt → JSON response with title, description, starter_code, test_cases, hint, solution
```

The prompt instructs Gemini to return strict JSON only. Response is parsed and forwarded to the frontend.

## Local Runtime Configuration

Backend execution commands are configured through `.env`:

```env
PYTHON_COMMAND=python
NODE_COMMAND=node
TSX_COMMAND=npx
TSX_ARGS=tsx
LOCAL_RUN_TIMEOUT_SECONDS=5
```

## What You Need To Fill In

1. **`backend/.env`** — `GEMINI_API_KEY`
2. **`frontend/.env`** — `VITE_API_URL=http://localhost:8000`
