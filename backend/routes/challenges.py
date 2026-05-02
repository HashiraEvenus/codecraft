import random
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from challenges_data import CHALLENGES

router = APIRouter()

TOPICS = [
    {"id": "arrays-strings",  "name": "Arrays & Strings",      "icon": "Brackets",     "description": "Manipulation, searching, and pattern matching"},
    {"id": "algorithms",      "name": "Algorithms",             "icon": "Cpu",          "description": "Sorting, searching, recursion, and complexity"},
    {"id": "data-structures", "name": "Data Structures",        "icon": "Database",     "description": "Linked lists, trees, stacks, queues, and graphs"},
    {"id": "oop",             "name": "OOP & Design Patterns",  "icon": "Layers",       "description": "Classes, inheritance, SOLID principles"},
    {"id": "best-practices",  "name": "Best Practices",         "icon": "CheckCircle2", "description": "Clean code, refactoring, and code review"},
    {"id": "scripting",       "name": "Scripting & Automation", "icon": "Terminal",     "description": "File I/O, CLI tools, and task automation"},
]


class ChallengeRequest(BaseModel):
    topic: str
    difficulty: str
    language: str = "python"
    exclude_ids: list[str] = []


def _pick_hardcoded(topic: str, difficulty: str, language: str, exclude_ids: set[str]):
    """Return a random hardcoded challenge that matches the filters, or None."""
    exact_matches = [
        c for c in CHALLENGES
        if c["topic"] == topic
        and c["difficulty"] == difficulty
        and c["language"] == language
    ]
    if exact_matches:
        matches = [c for c in exact_matches if c["id"] not in exclude_ids]
    else:
        # Relax language filter — most challenges are Python-only for now
        fallback_matches = [
            c for c in CHALLENGES
            if c["topic"] == topic
            and c["difficulty"] == difficulty
        ]
        matches = [c for c in fallback_matches if c["id"] not in exclude_ids]
    return random.choice(matches) if matches else None


def _has_matching_challenge(topic: str, difficulty: str, language: str):
    exact_match = any(
        c for c in CHALLENGES
        if c["topic"] == topic
        and c["difficulty"] == difficulty
        and c["language"] == language
    )
    if exact_match:
        return True
    return any(
        c for c in CHALLENGES
        if c["topic"] == topic
        and c["difficulty"] == difficulty
    )


@router.get("/topics")
def get_topics():
    return TOPICS


@router.get("/library")
def get_library():
    """Return a summary of all hardcoded challenges (no solutions)."""
    return [
        {
            "id": c["id"],
            "title": c["title"],
            "topic": c["topic"],
            "difficulty": c["difficulty"],
            "language": c["language"],
            "concept_count": len(c.get("concepts", [])),
            "test_count": len(c.get("test_cases", [])),
        }
        for c in CHALLENGES
    ]


@router.get("/library/{challenge_id}")
def get_library_challenge(challenge_id: str):
    for challenge in CHALLENGES:
        if challenge["id"] == challenge_id:
            return challenge

    raise HTTPException(status_code=404, detail="Challenge not found")


@router.post("/generate")
async def create_challenge(req: ChallengeRequest):
    topic      = req.topic.lower().strip()
    difficulty = req.difficulty.lower().strip()
    language   = req.language.lower().strip()
    exclude_ids = set(req.exclude_ids)

    valid_difficulties = {"beginner", "intermediate", "advanced"}
    if difficulty not in valid_difficulties:
        raise HTTPException(status_code=400, detail=f"difficulty must be one of {valid_difficulties}")

    valid_languages = {"python", "javascript", "typescript"}
    if language not in valid_languages:
        raise HTTPException(status_code=400, detail=f"language must be one of {valid_languages}")

    challenge = _pick_hardcoded(topic, difficulty, language, exclude_ids)
    if challenge:
        return challenge

    if exclude_ids and _has_matching_challenge(topic, difficulty, language):
        raise HTTPException(
            status_code=409,
            detail="You have completed every matching challenge. Enable completed exercises to practice them again."
        )

    raise HTTPException(
        status_code=404,
        detail=f"No challenge yet for {topic} / {difficulty} / {language}. More coming soon!"
    )
