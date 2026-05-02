# CodeCraft

CodeCraft is a local coding-practice app for keeping library knowledge, syntax, and problem-solving skills fresh. It serves an AI-assisted, curated exercise library from `backend/challenges_data.py` and runs submitted code on your own machine.

It is meant to be free to use locally: no account creation, subscriptions, paywalls, or external challenge-generation credentials are required.

## What it looks like 
## Screenshots
![Dashboard](https://github.com/HashiraEvenus/codecraft/blob/main/docs/Dashboard.png?raw=true)
![Challenge Editor](https://github.com/HashiraEvenus/codecraft/blob/main/docs/code-editor.png?raw=true)
![Exercise Library](https://github.com/HashiraEvenus/codecraft/blob/main/docs/Library.png?raw=true)



## What It Does

- Pick a topic, difficulty, and language from the dashboard.
- Generate a matching challenge from the bundled exercise library.
- Solve it in the Monaco-based editor.
- Run and test Python, JavaScript, or TypeScript locally.
- Track completed exercises in the library view.
- Skip completed exercises by default, with an option to include them again for review.
- Review hints, solutions, concepts, and reference docs included with each challenge.
- Grow the library over time by adding more exercises to `backend/challenges_data.py`.

## Tech Stack

- Frontend: React, TypeScript, Vite, Tailwind CSS
- Backend: FastAPI
- Editor: Monaco Editor
- Challenge data: AI-assisted curated exercises in `backend/challenges_data.py`
- Execution: local subprocess runner

## Local Setup

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

The backend runs on `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
copy .env.example .env
npm run dev
```

The frontend runs on `http://localhost:5173`.

## Configuration

The backend `.env` only controls local runtime behavior, such as command names and timeouts:

```env
LOCAL_RUN_TIMEOUT_SECONDS=5
LOCAL_MAX_CODE_BYTES=200000
PYTHON_COMMAND=python
NODE_COMMAND=node
TSX_COMMAND=npx
TSX_ARGS=tsx
FRONTEND_URL=http://localhost:5173
```

The frontend `.env` points to the local backend:

```env
VITE_API_URL=http://localhost:8000
```

## Safety Note

Submitted code runs locally on your machine. Only run code you trust.
