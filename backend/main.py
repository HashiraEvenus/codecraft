from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

from routes import challenges, execution

app = FastAPI(title="CodeCraft API", version="1.0.0")

origins = [
    "http://localhost:5173",
    os.getenv("FRONTEND_URL", ""),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o for o in origins if o],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(challenges.router, prefix="/api/challenges", tags=["challenges"])
app.include_router(execution.router, prefix="/api/execution", tags=["execution"])


@app.get("/")
def health():
    return {"status": "ok", "service": "codecraft-api"}
