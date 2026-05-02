from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.local_runner import execute_code, run_tests

router = APIRouter()


class RunRequest(BaseModel):
    language: str
    code: str


class TestRequest(BaseModel):
    language: str
    code: str
    test_cases: list[dict]


@router.post("/run")
async def run_code(req: RunRequest):
    try:
        return await execute_code(req.language, req.code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/test")
async def test_code(req: TestRequest):
    try:
        return await run_tests(req.language, req.code, req.test_cases)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
