# CodeCraft — Local Setup Guide

CodeCraft is a local AI coding-practice app. It uses your Gemini API key to generate challenges and runs code on your own machine.

## Requirements

- Python 3.10+
- Node.js 18+
- A Gemini API key from https://aistudio.google.com/app/apikey
- Optional for TypeScript execution: `npx tsx` support

### Backend

```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
uvicorn main:app --reload
# Runs on http://localhost:8000
```

Local execution uses the commands in `backend/.env`:

```env
PYTHON_COMMAND=python
NODE_COMMAND=node
TSX_COMMAND=npx
TSX_ARGS=tsx
```

If a command is not on your PATH, replace it with the full path to the executable.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
# .env points to http://localhost:8000
npm run dev
# Runs on http://localhost:5173
```

---

## How To Use

1. Start the backend.
2. Start the frontend.
3. Open http://localhost:5173.
4. Generate a challenge.
5. Solve it in the built-in editor.
6. Run or test the solution locally.

---

## Safety Note

Code execution is local. Only run code you trust, because submitted code executes on your machine.

---

## Open Source Usage

Do not commit your `.env` files. Other users should add their own Gemini API key and run the app locally.
