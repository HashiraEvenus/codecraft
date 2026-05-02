import google.generativeai as genai
import os
import json
import re

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
_model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-2.0-flash-lite"))
USE_LOCAL_FALLBACK = os.getenv("USE_LOCAL_CHALLENGE_FALLBACK", "true").lower() == "true"

LANGUAGE_STARTERS = {
    "python": "def solution(...):\n    pass",
    "javascript": "function solution(...) {\n  // your code here\n}",
    "typescript": "function solution(...): ReturnType {\n  // your code here\n}",
}


def _local_challenge(topic: str, difficulty: str, language: str) -> dict:
    topic_label = topic.replace("-", " ").replace("&", "and").title()

    if language == "python":
        starter_code = "def solution(text):\n    # Return the reversed text.\n    pass"
        solution = "def solution(text):\n    return text[::-1]"
        test_cases = [
            {"input": 'solution("hello")', "expected_output": "olleh"},
            {"input": 'solution("CodeCraft")', "expected_output": "tfarCedoC"},
            {"input": 'solution("")', "expected_output": ""},
        ]
        examples = ['text[::-1]', 'for char in text:\n    result = char + result']
        docs_url = "https://docs.python.org/3/tutorial/introduction.html#strings"
    elif language == "typescript":
        starter_code = "function solution(text: string): string {\n  // Return the reversed text.\n  return \"\";\n}"
        solution = "function solution(text: string): string {\n  return text.split(\"\").reverse().join(\"\");\n}"
        test_cases = [
            {"input": 'solution("hello")', "expected_output": "olleh"},
            {"input": 'solution("CodeCraft")', "expected_output": "tfarCedoC"},
            {"input": 'solution("")', "expected_output": ""},
        ]
        examples = ['text.split("").reverse().join("")', "const chars: string[] = [...text];"]
        docs_url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse"
    else:
        starter_code = "function solution(text) {\n  // Return the reversed text.\n  return \"\";\n}"
        solution = "function solution(text) {\n  return text.split(\"\").reverse().join(\"\");\n}"
        test_cases = [
            {"input": 'solution("hello")', "expected_output": "olleh"},
            {"input": 'solution("CodeCraft")', "expected_output": "tfarCedoC"},
            {"input": 'solution("")', "expected_output": ""},
        ]
        examples = ['text.split("").reverse().join("")', "for (const char of text) { /* ... */ }"]
        docs_url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split"

    return {
        "title": f"Local Fallback: Reverse a String",
        "description": (
            f"Gemini is unavailable or out of quota, so this local {difficulty} "
            f"{topic_label} challenge was generated for practice. Write a function "
            "named solution that takes a string and returns the characters in reverse order."
        ),
        "starter_code": starter_code,
        "test_cases": test_cases,
        "hint": "Build the result from the end of the string, or use the language's string/list helpers.",
        "solution": solution,
        "concepts": [
            {
                "title": "String indexing",
                "explanation": "Strings are ordered sequences, so you can read characters by position or iterate over them.",
                "examples": examples,
                "watch_out": "Remember that the last character is at the end of the string, not at index 0.",
            },
            {
                "title": "Function return values",
                "explanation": "The test cases call your solution function and compare what it returns.",
                "examples": ["return result", "return text"],
                "watch_out": "Printing is not the same as returning; the tests expect the function to return a value.",
            },
        ],
        "docs_url": docs_url,
    }


async def generate_challenge(topic: str, difficulty: str, language: str) -> dict:
    prompt = f"""You are a coding challenge generator and patient tutor. Return ONLY valid JSON — no markdown, no backticks, no explanation.

Generate a {difficulty} coding challenge on the topic "{topic}" in {language}.

Return this exact JSON structure:
{{
  "title": "Short descriptive title",
  "description": "Clear 2-4 sentence problem statement with 1-2 concrete examples showing input and output",
  "starter_code": "Runnable {language} starter code with the function signature and a placeholder body",
  "test_cases": [
    {{"input": "the exact expression to call the function, e.g. solution(5)", "expected_output": "expected printed result as a string"}},
    {{"input": "...", "expected_output": "..."}},
    {{"input": "...", "expected_output": "..."}}
  ],
  "hint": "A helpful nudge that guides thinking without giving away the solution",
  "solution": "A complete, clean, working solution in {language}",
  "concepts": [
    {{
      "title": "Concept name (e.g. List Slicing)",
      "explanation": "1-2 sentence plain-English explanation of the concept, written for someone returning to coding after a break",
      "examples": ["short runnable code snippet", "another variant"],
      "watch_out": "One common mistake or gotcha beginners make with this concept"
    }}
  ],
  "docs_url": "Official docs URL most relevant to this challenge (e.g. Python docs, MDN)"
}}

Rules:
- test_cases.input must be a valid {language} expression that calls the function
- test_cases.expected_output must exactly match what print(input) would output
- starter_code must be syntactically valid (no errors, just incomplete logic)
- difficulty {difficulty}: beginner=simple loops/conditions, intermediate=algorithms/data structures, advanced=optimization/complex logic
- concepts: include 2-4 concepts the solver NEEDS to know to complete this challenge — not general theory, only directly relevant syntax and built-ins
- explanations should be friendly and clear, like a senior dev explaining to a friend returning to coding after months away
- watch_out should highlight subtle traps (e.g. .sort() returns None, 0-based indexing, etc.)"""

    try:
        response = _model.generate_content(prompt)
        raw = response.text.strip()

        # Strip markdown code fences if Gemini wraps the response
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        return json.loads(raw.strip())
    except Exception:
        if USE_LOCAL_FALLBACK:
            return _local_challenge(topic, difficulty, language)
        raise
