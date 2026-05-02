import asyncio
import os
import subprocess
import sys
import tempfile
from pathlib import Path


RUN_TIMEOUT_SECONDS = float(os.getenv("LOCAL_RUN_TIMEOUT_SECONDS", "5"))
MAX_CODE_BYTES = int(os.getenv("LOCAL_MAX_CODE_BYTES", "200000"))

RUNTIMES = {
    "python": {
        "command": os.getenv("PYTHON_COMMAND", sys.executable),
        "args": [],
        "suffix": ".py",
        "test_wrapper": lambda code, expr: f"{code}\n\nprint({expr})",
    },
    "javascript": {
        "command": os.getenv("NODE_COMMAND", "node"),
        "args": [],
        "suffix": ".js",
        "test_wrapper": lambda code, expr: f"{code}\n\nconsole.log({expr});",
    },
    "typescript": {
        "command": os.getenv("TSX_COMMAND", "npx"),
        "args": os.getenv("TSX_ARGS", "tsx").split(),
        "suffix": ".ts",
        "test_wrapper": lambda code, expr: f"{code}\n\nconsole.log({expr});",
    },
}


def _runtime_for(language: str) -> dict:
    runtime = RUNTIMES.get(language.lower())
    if not runtime:
        supported = ", ".join(sorted(RUNTIMES))
        raise ValueError(f"Unsupported language '{language}'. Supported languages: {supported}.")
    return runtime


async def execute_code(language: str, code: str) -> dict:
    if len(code.encode("utf-8")) > MAX_CODE_BYTES:
        raise ValueError(f"Code is too large. Limit is {MAX_CODE_BYTES} bytes.")

    runtime = _runtime_for(language)

    with tempfile.TemporaryDirectory(prefix="codecraft-") as temp_dir:
        file_path = Path(temp_dir) / f"main{runtime['suffix']}"
        file_path.write_text(code, encoding="utf-8")

        try:
            completed = await asyncio.to_thread(
                subprocess.run,
                [runtime["command"], *runtime["args"], str(file_path)],
                cwd=temp_dir,
                capture_output=True,
                text=True,
                timeout=RUN_TIMEOUT_SECONDS,
            )
        except subprocess.TimeoutExpired:
            return {
                "stdout": "",
                "stderr": f"Execution timed out after {RUN_TIMEOUT_SECONDS:g} seconds.",
                "exit_code": 124,
                "signal": "timeout",
            }
        except FileNotFoundError as exc:
            raise RuntimeError(
                f"Runtime command '{runtime['command']}' was not found. "
                "Install it or update the command in backend/.env."
            ) from exc

    return {
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "exit_code": completed.returncode,
        "signal": None,
    }


async def run_tests(language: str, code: str, test_cases: list[dict]) -> dict:
    runtime = _runtime_for(language)
    results = []

    for tc in test_cases:
        test_code = runtime["test_wrapper"](code, tc["input"])
        result = await execute_code(language, test_code)
        actual = result["stdout"].strip()
        expected = str(tc["expected_output"]).strip()

        results.append({
            "input": tc["input"],
            "expected": expected,
            "actual": actual,
            "passed": actual == expected,
            "stderr": result["stderr"],
        })

    return {
        "results": results,
        "all_passed": all(r["passed"] for r in results),
        "passed_count": sum(1 for r in results if r["passed"]),
        "total": len(results),
    }
