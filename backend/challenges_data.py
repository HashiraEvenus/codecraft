"""
Hand-crafted challenges. Each test case's expected_output must match
exactly what Python's print() produces for that input.
"""

CHALLENGES = [

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "reverse-a-string",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Reverse a String",
        "description": (
            "Write a function called `solution` that takes a string and returns it reversed.\n\n"
            "Example:\n  solution('hello') → 'olleh'\n  solution('Python') → 'nohtyP'"
        ),
        "starter_code": "def solution(text: str) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("hello")',   "expected_output": "olleh"},
            {"input": 'solution("Python")',  "expected_output": "nohtyP"},
            {"input": 'solution("")',        "expected_output": ""},
            {"input": 'solution("a")',       "expected_output": "a"},
        ],
        "hint": "Python strings support slice notation — try using a step of -1.",
        "solution": "def solution(text: str) -> str:\n    return text[::-1]",
        "concepts": [
            {
                "title": "String Slicing  [ start : stop : step ]",
                "explanation": (
                    "Slicing lets you extract a portion of a string. "
                    "The third value is the step — how many characters to skip (and in which direction). "
                    "A step of -1 means 'go backwards through every character'."
                ),
                "examples": [
                    's = "hello"',
                    's[0:3]     # "hel"   — characters 0, 1, 2',
                    's[::2]     # "hlo"   — every other character',
                    's[::-1]    # "olleh" — all characters, reversed',
                ],
                "watch_out": (
                    "s.reverse() does not exist for strings (only for lists). "
                    "reversed(s) returns an iterator, so you need ''.join(reversed(s)) — "
                    "the slice s[::-1] is cleaner and more Pythonic."
                ),
            },
            {
                "title": "Strings Are Immutable",
                "explanation": (
                    "You cannot change individual characters in a string. "
                    "Every operation that looks like it modifies a string actually creates a new one."
                ),
                "examples": [
                    's = "hello"',
                    '# s[0] = "H"  ← TypeError! strings are read-only',
                    's = "H" + s[1:]  # correct: build a new string',
                ],
                "watch_out": (
                    "If you try to build the result by doing result[i] = char you will get a TypeError. "
                    "Use concatenation or a list of characters and join at the end."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/introduction.html#strings",
    },

    {
        "id": "count-vowels",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Count Vowels",
        "description": (
            "Write a function called `solution` that takes a string and returns "
            "the number of vowels (a, e, i, o, u) it contains. Ignore case.\n\n"
            "Example:\n  solution('hello') → 2\n  solution('Python') → 1"
        ),
        "starter_code": "def solution(text: str) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("hello")',   "expected_output": "2"},
            {"input": 'solution("Python")',  "expected_output": "1"},
            {"input": 'solution("rhythm")',  "expected_output": "0"},
            {"input": 'solution("AEIOU")',   "expected_output": "5"},
        ],
        "hint": "Loop through each character and check if it belongs to a known set of vowels. Convert to lowercase first.",
        "solution": (
            "def solution(text: str) -> int:\n"
            "    vowels = 'aeiou'\n"
            "    return sum(1 for ch in text if ch.lower() in vowels)"
        ),
        "concepts": [
            {
                "title": "Iterating Over a String",
                "explanation": (
                    "A string is a sequence of characters, so you can loop over it "
                    "the same way you loop over a list."
                ),
                "examples": [
                    'for ch in "hello":',
                    '    print(ch)   # h, e, l, l, o (one per line)',
                ],
                "watch_out": (
                    "for i in range(len(text)) works but is less Pythonic. "
                    "Prefer 'for ch in text' when you only need the characters, "
                    "not their positions."
                ),
            },
            {
                "title": "in Operator for Membership",
                "explanation": (
                    "'in' checks whether a value exists inside a sequence or string. "
                    "It works on strings, lists, tuples, sets, and dicts."
                ),
                "examples": [
                    '"e" in "hello"   # True',
                    '"z" in "hello"   # False',
                    '"e" in ["a","e"] # True',
                    '"e" in {"a","e"} # True (set — fastest for large lookups)',
                ],
                "watch_out": (
                    "'e' in 'hello' is True, but 'el' in 'hello' is also True — "
                    "'in' checks for substrings, not just single characters."
                ),
            },
            {
                "title": "str.lower() and str.upper()",
                "explanation": (
                    "These return a new string with all characters converted. "
                    "They do not change the original string."
                ),
                "examples": [
                    '"Hello".lower()  # "hello"',
                    '"hello".upper()  # "HELLO"',
                    '"AEIOU".lower()  # "aeiou"',
                ],
                "watch_out": (
                    "text.lower() returns a new string — it does NOT modify text in place. "
                    "You must use the return value: text = text.lower()."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#string-methods",
    },

    {
        "id": "find-max-in-list",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Find the Maximum",
        "description": (
            "Write a function called `solution` that takes a list of integers "
            "and returns the largest value. Do not use the built-in max().\n\n"
            "Example:\n  solution([3, 1, 4, 1, 5, 9]) → 9"
        ),
        "starter_code": "def solution(nums: list) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([3, 1, 4, 1, 5, 9])", "expected_output": "9"},
            {"input": "solution([1])",                 "expected_output": "1"},
            {"input": "solution([-5, -1, -3])",        "expected_output": "-1"},
            {"input": "solution([0, 0, 0])",           "expected_output": "0"},
        ],
        "hint": "Start by assuming the first element is the largest. Then compare it against every other element.",
        "solution": (
            "def solution(nums: list) -> int:\n"
            "    largest = nums[0]\n"
            "    for n in nums:\n"
            "        if n > largest:\n"
            "            largest = n\n"
            "    return largest"
        ),
        "concepts": [
            {
                "title": "Tracking a Running Value in a Loop",
                "explanation": (
                    "A common pattern: initialise a variable before the loop, "
                    "update it inside the loop, return it after."
                ),
                "examples": [
                    "largest = nums[0]      # seed with the first element",
                    "for n in nums:",
                    "    if n > largest:",
                    "        largest = n    # update whenever we find a better value",
                    "return largest",
                ],
                "watch_out": (
                    "Do not seed with 0 — if all numbers are negative, 0 will never be replaced "
                    "and you will return the wrong answer. Always seed with nums[0]."
                ),
            },
            {
                "title": "Indexing Into a List",
                "explanation": (
                    "Lists are zero-indexed: the first element is at index 0, "
                    "the last is at index -1."
                ),
                "examples": [
                    'nums = [10, 20, 30]',
                    'nums[0]   # 10',
                    'nums[-1]  # 30 (last element)',
                    'nums[1]   # 20',
                ],
                "watch_out": (
                    "Accessing nums[len(nums)] raises an IndexError. "
                    "The last valid index is len(nums) - 1, or just use nums[-1]."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html",
    },

    {
        "id": "remove-duplicates",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Remove Duplicates",
        "description": (
            "Write a function called `solution` that takes a list of integers "
            "and returns a new list with duplicates removed. "
            "Preserve the original order of first appearances.\n\n"
            "Example:\n  solution([1, 2, 2, 3, 1]) → [1, 2, 3]"
        ),
        "starter_code": "def solution(nums: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 2, 3, 1])",   "expected_output": "[1, 2, 3]"},
            {"input": "solution([1, 1, 1])",           "expected_output": "[1]"},
            {"input": "solution([1, 2, 3])",           "expected_output": "[1, 2, 3]"},
            {"input": "solution([])",                  "expected_output": "[]"},
        ],
        "hint": "Use a set to keep track of which values you have already seen.",
        "solution": (
            "def solution(nums: list) -> list:\n"
            "    seen = set()\n"
            "    result = []\n"
            "    for n in nums:\n"
            "        if n not in seen:\n"
            "            result.append(n)\n"
            "            seen.add(n)\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "Sets — Fast Membership Checks",
                "explanation": (
                    "A set stores unique values and checks membership in O(1) time "
                    "(vs O(n) for a list). Perfect when you need to track 'have I seen this?'."
                ),
                "examples": [
                    "seen = set()       # empty set",
                    "seen.add(5)        # add a value",
                    "5 in seen          # True",
                    "seen = {1, 2, 3}   # set literal",
                    "# note: {} creates an empty DICT, not a set — use set()",
                ],
                "watch_out": (
                    "list(set(nums)) removes duplicates but destroys the order. "
                    "If order matters (as here), you must use the seen-set + result-list pattern."
                ),
            },
            {
                "title": "list.append()",
                "explanation": (
                    "append() adds one item to the end of a list. "
                    "It modifies the list in place and returns None."
                ),
                "examples": [
                    "result = []",
                    "result.append(1)   # [1]",
                    "result.append(2)   # [1, 2]",
                    "# result = result.append(3)  ← BUG: returns None!",
                ],
                "watch_out": (
                    "result = result.append(x) sets result to None because append returns None. "
                    "Just call result.append(x) on its own line."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — INTERMEDIATE
    # ──────────────────────────────────────────────

    {
        "id": "two-sum",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Two Sum",
        "description": (
            "Write a function called `solution` that takes a list of integers and a target integer. "
            "Return the indices of the two numbers that add up to the target as a list [i, j] "
            "where i < j. You may assume exactly one solution exists.\n\n"
            "Example:\n  solution([2, 7, 11, 15], 9) → [0, 1]  (2 + 7 = 9)"
        ),
        "starter_code": "def solution(nums: list, target: int) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([2, 7, 11, 15], 9)",  "expected_output": "[0, 1]"},
            {"input": "solution([3, 2, 4], 6)",        "expected_output": "[1, 2]"},
            {"input": "solution([1, 5, 3, 7], 8)",     "expected_output": "[1, 3]"},
        ],
        "hint": "For each number, check whether (target - number) has already been seen. A dictionary mapping value→index makes this O(n).",
        "solution": (
            "def solution(nums: list, target: int) -> list:\n"
            "    seen = {}\n"
            "    for i, n in enumerate(nums):\n"
            "        complement = target - n\n"
            "        if complement in seen:\n"
            "            return [seen[complement], i]\n"
            "        seen[n] = i\n"
            "    return []"
        ),
        "concepts": [
            {
                "title": "Dictionaries as Index Maps",
                "explanation": (
                    "A dict lets you store and look up values in O(1) time. "
                    "A classic trick is to map value→index as you loop, "
                    "so you can instantly check whether a needed complement exists."
                ),
                "examples": [
                    "seen = {}          # empty dict",
                    "seen[5] = 0       # key=5, value=0 (the index)",
                    "5 in seen          # True — checks keys",
                    "seen[5]            # 0   — retrieves the index",
                ],
                "watch_out": (
                    "in on a dict checks keys, not values. "
                    "'5 in seen' is True if 5 is a KEY — even if the stored value is 0."
                ),
            },
            {
                "title": "enumerate() — Index + Value Together",
                "explanation": (
                    "enumerate() wraps an iterable and gives you both the index and the value "
                    "on each iteration. Much cleaner than maintaining a counter variable."
                ),
                "examples": [
                    "for i, val in enumerate([10, 20, 30]):",
                    "    print(i, val)   # 0 10 / 1 20 / 2 30",
                    "",
                    "# instead of:",
                    "i = 0",
                    "for val in nums:",
                    "    ...",
                    "    i += 1",
                ],
                "watch_out": (
                    "enumerate starts at 0 by default. "
                    "You can change the start: enumerate(nums, start=1) — but index 0 is almost always what you want."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#enumerate",
    },

    {
        "id": "is-palindrome",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Is It a Palindrome?",
        "description": (
            "Write a function called `solution` that takes a string and returns True "
            "if it reads the same forwards and backwards, ignoring spaces and case. "
            "Return False otherwise.\n\n"
            "Example:\n  solution('racecar') → True\n  solution('A man a plan a canal Panama') → True"
        ),
        "starter_code": "def solution(text: str) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("racecar")',                        "expected_output": "True"},
            {"input": 'solution("A man a plan a canal Panama")',    "expected_output": "True"},
            {"input": 'solution("hello")',                          "expected_output": "False"},
            {"input": 'solution("")',                               "expected_output": "True"},
        ],
        "hint": "Strip spaces and lowercase the string first, then compare it to its reverse.",
        "solution": (
            "def solution(text: str) -> bool:\n"
            "    cleaned = text.replace(' ', '').lower()\n"
            "    return cleaned == cleaned[::-1]"
        ),
        "concepts": [
            {
                "title": "str.replace(old, new)",
                "explanation": (
                    "replace() returns a new string with all occurrences of old swapped for new. "
                    "Passing an empty string as new effectively deletes the characters."
                ),
                "examples": [
                    '"hello world".replace(" ", "")   # "helloworld"',
                    '"aabbcc".replace("b", "x")       # "aaxxcc"',
                    '"hello".replace("z", "!")        # "hello" — no change if not found',
                ],
                "watch_out": (
                    "replace() does not modify the string in place. "
                    "You must capture the return value: text = text.replace(' ', '')."
                ),
            },
            {
                "title": "Chaining String Methods",
                "explanation": (
                    "Because string methods always return a new string, "
                    "you can chain them in one expression."
                ),
                "examples": [
                    'text.replace(" ", "").lower()',
                    'text.strip().upper().replace("-", "")',
                ],
                "watch_out": (
                    "Each method call returns a new string. "
                    "If one step returns None (e.g. if you accidentally called a list method), "
                    "the chain will raise an AttributeError."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.replace",
    },

    {
        "id": "flatten-list",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Flatten a Nested List",
        "description": (
            "Write a function called `solution` that takes a list which may contain "
            "integers or other lists of integers (one level deep) and returns a single flat list.\n\n"
            "Example:\n  solution([1, [2, 3], 4, [5]]) → [1, 2, 3, 4, 5]"
        ),
        "starter_code": "def solution(nested: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, [2, 3], 4, [5]])",  "expected_output": "[1, 2, 3, 4, 5]"},
            {"input": "solution([[1, 2], [3, 4]])",      "expected_output": "[1, 2, 3, 4]"},
            {"input": "solution([1, 2, 3])",             "expected_output": "[1, 2, 3]"},
            {"input": "solution([])",                    "expected_output": "[]"},
        ],
        "hint": "Check whether each item is a list using isinstance(). If it is, extend your result with it; otherwise append the item directly.",
        "solution": (
            "def solution(nested: list) -> list:\n"
            "    result = []\n"
            "    for item in nested:\n"
            "        if isinstance(item, list):\n"
            "            result.extend(item)\n"
            "        else:\n"
            "            result.append(item)\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "isinstance() — Type Checking",
                "explanation": (
                    "isinstance(value, type) returns True if value is of that type. "
                    "Use it when your function can receive different kinds of input."
                ),
                "examples": [
                    "isinstance(3, int)       # True",
                    "isinstance([1,2], list)  # True",
                    "isinstance('hi', str)    # True",
                    "isinstance(3.0, int)     # False (it's a float)",
                ],
                "watch_out": (
                    "type(x) == list is less flexible than isinstance(x, list) — "
                    "isinstance also returns True for subclasses. Prefer isinstance."
                ),
            },
            {
                "title": "list.extend() vs list.append()",
                "explanation": (
                    "append() adds one item. extend() adds all items from an iterable. "
                    "Use extend() when you want to merge a list into another list."
                ),
                "examples": [
                    "result = [1, 2]",
                    "result.append([3, 4])   # [1, 2, [3, 4]]  — adds the list as one element",
                    "result.extend([3, 4])   # [1, 2, 3, 4]    — merges the items in",
                    "result += [3, 4]        # same as extend",
                ],
                "watch_out": (
                    "result.append([3, 4]) adds [3, 4] as a single nested element, not the numbers 3 and 4. "
                    "This is a very common mistake when flattening lists."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#isinstance",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "fizzbuzz",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "FizzBuzz",
        "description": (
            "Write a function called `solution` that takes an integer n and returns a string:\n"
            "  'Fizz' if n is divisible by 3\n"
            "  'Buzz' if n is divisible by 5\n"
            "  'FizzBuzz' if divisible by both\n"
            "  The number as a string otherwise\n\n"
            "Example:\n  solution(15) → 'FizzBuzz'\n  solution(7) → '7'"
        ),
        "starter_code": "def solution(n: int) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(15)", "expected_output": "FizzBuzz"},
            {"input": "solution(3)",  "expected_output": "Fizz"},
            {"input": "solution(5)",  "expected_output": "Buzz"},
            {"input": "solution(7)",  "expected_output": "7"},
        ],
        "hint": "Check divisibility by both 3 and 5 first, before checking each individually. Order of conditions matters.",
        "solution": (
            "def solution(n: int) -> str:\n"
            "    if n % 3 == 0 and n % 5 == 0:\n"
            "        return 'FizzBuzz'\n"
            "    elif n % 3 == 0:\n"
            "        return 'Fizz'\n"
            "    elif n % 5 == 0:\n"
            "        return 'Buzz'\n"
            "    return str(n)"
        ),
        "concepts": [
            {
                "title": "The Modulo Operator  %",
                "explanation": (
                    "n % m gives the remainder after dividing n by m. "
                    "If the remainder is 0, n is perfectly divisible by m."
                ),
                "examples": [
                    "10 % 3   # 1   (10 = 3×3 + 1)",
                    "15 % 5   # 0   (15 = 5×3 + 0, so divisible)",
                    "7  % 2   # 1   (odd number)",
                    "8  % 2   # 0   (even number)",
                ],
                "watch_out": (
                    "Check the combined case (divisible by both) BEFORE the individual cases. "
                    "If you check n % 3 first and return, you will never reach the FizzBuzz branch for multiples of 15."
                ),
            },
            {
                "title": "Converting Integers to Strings",
                "explanation": (
                    "str() converts any value to its string representation. "
                    "You need this when your function must return a string but the value is a number."
                ),
                "examples": [
                    "str(7)      # '7'",
                    "str(3.14)   # '3.14'",
                    "str(True)   # 'True'",
                    'f"{7}"      # "7"  — f-string also works',
                ],
                "watch_out": (
                    "Returning the integer 7 instead of the string '7' will fail the test. "
                    "Make sure you wrap with str() or use an f-string."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations",
    },

    {
        "id": "fibonacci",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Fibonacci Sequence",
        "description": (
            "Write a function called `solution` that takes an integer n and returns "
            "the first n numbers of the Fibonacci sequence as a list. "
            "The sequence starts: 0, 1, 1, 2, 3, 5, 8 …\n\n"
            "Example:\n  solution(6) → [0, 1, 1, 2, 3, 5]"
        ),
        "starter_code": "def solution(n: int) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(6)",  "expected_output": "[0, 1, 1, 2, 3, 5]"},
            {"input": "solution(1)",  "expected_output": "[0]"},
            {"input": "solution(2)",  "expected_output": "[0, 1]"},
            {"input": "solution(8)",  "expected_output": "[0, 1, 1, 2, 3, 5, 8, 13]"},
        ],
        "hint": "Start with [0, 1] and keep appending the sum of the last two numbers until you have n numbers.",
        "solution": (
            "def solution(n: int) -> list:\n"
            "    if n == 0: return []\n"
            "    if n == 1: return [0]\n"
            "    seq = [0, 1]\n"
            "    while len(seq) < n:\n"
            "        seq.append(seq[-1] + seq[-2])\n"
            "    return seq"
        ),
        "concepts": [
            {
                "title": "while Loops",
                "explanation": (
                    "A while loop repeats as long as its condition is True. "
                    "Use it when you do not know in advance how many iterations you need."
                ),
                "examples": [
                    "seq = [0, 1]",
                    "while len(seq) < 6:",
                    "    seq.append(seq[-1] + seq[-2])",
                    "# seq → [0, 1, 1, 2, 3, 5]",
                ],
                "watch_out": (
                    "If the condition never becomes False, you have an infinite loop. "
                    "Always make sure the loop body moves you closer to termination."
                ),
            },
            {
                "title": "Negative Indexing  list[-1], list[-2]",
                "explanation": (
                    "Index -1 refers to the last element, -2 to the second-last, and so on. "
                    "This lets you read from the end of a list without knowing its length."
                ),
                "examples": [
                    "nums = [0, 1, 1, 2]",
                    "nums[-1]   # 2  (last)",
                    "nums[-2]   # 1  (second-last)",
                    "nums[-1] + nums[-2]  # 3 — next Fibonacci number",
                ],
                "watch_out": (
                    "Negative indexing on an empty list raises an IndexError. "
                    "Make sure you have at least 2 elements before using [-1] and [-2]."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/controlflow.html",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — INTERMEDIATE
    # ──────────────────────────────────────────────

    {
        "id": "binary-search",
        "topic": "algorithms",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Binary Search",
        "description": (
            "Write a function called `solution` that takes a sorted list of integers and a target. "
            "Return the index of the target, or -1 if it is not in the list. "
            "Do not use the 'in' operator or list.index().\n\n"
            "Example:\n  solution([1, 3, 5, 7, 9], 5) → 2"
        ),
        "starter_code": "def solution(nums: list, target: int) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 3, 5, 7, 9], 5)",  "expected_output": "2"},
            {"input": "solution([1, 3, 5, 7, 9], 1)",  "expected_output": "0"},
            {"input": "solution([1, 3, 5, 7, 9], 9)",  "expected_output": "4"},
            {"input": "solution([1, 3, 5, 7, 9], 4)",  "expected_output": "-1"},
        ],
        "hint": "Keep two pointers — left and right — that define the search window. Each iteration, check the middle element and halve the window.",
        "solution": (
            "def solution(nums: list, target: int) -> int:\n"
            "    left, right = 0, len(nums) - 1\n"
            "    while left <= right:\n"
            "        mid = (left + right) // 2\n"
            "        if nums[mid] == target:\n"
            "            return mid\n"
            "        elif nums[mid] < target:\n"
            "            left = mid + 1\n"
            "        else:\n"
            "            right = mid - 1\n"
            "    return -1"
        ),
        "concepts": [
            {
                "title": "Two-Pointer / Shrinking Window",
                "explanation": (
                    "Binary search works by maintaining a left and right boundary. "
                    "Each step you look at the midpoint and throw away the half that cannot contain the answer."
                ),
                "examples": [
                    "left, right = 0, len(nums) - 1",
                    "mid = (left + right) // 2",
                    "# if target is bigger, discard the left half:",
                    "left = mid + 1",
                    "# if target is smaller, discard the right half:",
                    "right = mid - 1",
                ],
                "watch_out": (
                    "The loop condition is left <= right (with equals). "
                    "If you use left < right you will miss the case where left == right "
                    "and the target is exactly at that position."
                ),
            },
            {
                "title": "Integer Division  //",
                "explanation": (
                    "// divides and rounds down to the nearest integer. "
                    "Use it whenever you need a whole-number result."
                ),
                "examples": [
                    "7 // 2    # 3",
                    "8 // 2    # 4",
                    "(0 + 4) // 2   # 2  — midpoint of indices 0..4",
                ],
                "watch_out": (
                    "5 / 2 gives 2.5 (a float), which cannot be used as a list index. "
                    "Always use // when computing indices."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/bisect.html",
    },

    {
        "id": "bubble-sort",
        "topic": "algorithms",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Bubble Sort",
        "description": (
            "Write a function called `solution` that sorts a list of integers "
            "in ascending order using bubble sort. Return the sorted list. "
            "Do not use list.sort() or sorted().\n\n"
            "Example:\n  solution([5, 3, 8, 1]) → [1, 3, 5, 8]"
        ),
        "starter_code": "def solution(nums: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([5, 3, 8, 1])",    "expected_output": "[1, 3, 5, 8]"},
            {"input": "solution([1, 2, 3])",        "expected_output": "[1, 2, 3]"},
            {"input": "solution([3, 1])",            "expected_output": "[1, 3]"},
            {"input": "solution([4, 4, 1])",        "expected_output": "[1, 4, 4]"},
        ],
        "hint": "Use nested loops. The outer loop runs n times. The inner loop compares adjacent pairs and swaps them if they are in the wrong order.",
        "solution": (
            "def solution(nums: list) -> list:\n"
            "    nums = nums[:]\n"
            "    n = len(nums)\n"
            "    for i in range(n):\n"
            "        for j in range(n - i - 1):\n"
            "            if nums[j] > nums[j + 1]:\n"
            "                nums[j], nums[j + 1] = nums[j + 1], nums[j]\n"
            "    return nums"
        ),
        "concepts": [
            {
                "title": "Swapping Two Values in Python",
                "explanation": (
                    "Python lets you swap two variables in a single line using tuple unpacking. "
                    "No temporary variable needed."
                ),
                "examples": [
                    "a, b = 1, 2",
                    "a, b = b, a   # a=2, b=1 — swapped",
                    "",
                    "# same for list positions:",
                    "nums[0], nums[1] = nums[1], nums[0]",
                ],
                "watch_out": (
                    "In many other languages you need a temp variable: tmp=a; a=b; b=tmp. "
                    "In Python, a, b = b, a evaluates the right side first, then assigns — so no temp needed."
                ),
            },
            {
                "title": "range() for Indexed Loops",
                "explanation": (
                    "range(n) generates integers 0, 1, … n-1. "
                    "range(a, b) generates a, a+1, … b-1."
                ),
                "examples": [
                    "for i in range(5):      # 0 1 2 3 4",
                    "for i in range(2, 5):   # 2 3 4",
                    "for i in range(n - 1):  # 0 … n-2",
                ],
                "watch_out": (
                    "range(n) stops at n-1, not n. "
                    "Accessing index n would be out of bounds."
                ),
            },
            {
                "title": "Copying a List Before Mutating It",
                "explanation": (
                    "If you sort in place the caller's list is modified too (lists are passed by reference). "
                    "Take a copy first with nums = nums[:] or nums = list(nums)."
                ),
                "examples": [
                    "original = [3, 1, 2]",
                    "copy = original[:]      # independent copy",
                    "copy.sort()",
                    "print(original)         # [3, 1, 2] — unchanged",
                ],
                "watch_out": (
                    "copy = original just creates another name pointing to the same list. "
                    "Modifying copy also modifies original. Use [:] for a true copy."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/howto/sorting.html",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — ADVANCED
    # ──────────────────────────────────────────────

    {
        "id": "merge-sorted-lists",
        "topic": "algorithms",
        "difficulty": "advanced",
        "language": "python",
        "title": "Merge Two Sorted Lists",
        "description": (
            "Write a function called `solution` that takes two sorted lists of integers "
            "and returns a single sorted merged list. Do not use sort() or sorted().\n\n"
            "Example:\n  solution([1, 3, 5], [2, 4, 6]) → [1, 2, 3, 4, 5, 6]"
        ),
        "starter_code": "def solution(a: list, b: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 3, 5], [2, 4, 6])",  "expected_output": "[1, 2, 3, 4, 5, 6]"},
            {"input": "solution([1, 2], [3, 4])",         "expected_output": "[1, 2, 3, 4]"},
            {"input": "solution([], [1, 2])",              "expected_output": "[1, 2]"},
            {"input": "solution([5], [1, 3, 4])",         "expected_output": "[1, 3, 4, 5]"},
        ],
        "hint": "Use two pointers — one for each list. Always pick the smaller current element and advance that pointer.",
        "solution": (
            "def solution(a: list, b: list) -> list:\n"
            "    result = []\n"
            "    i = j = 0\n"
            "    while i < len(a) and j < len(b):\n"
            "        if a[i] <= b[j]:\n"
            "            result.append(a[i])\n"
            "            i += 1\n"
            "        else:\n"
            "            result.append(b[j])\n"
            "            j += 1\n"
            "    result.extend(a[i:])\n"
            "    result.extend(b[j:])\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "Two-Pointer Merge Pattern",
                "explanation": (
                    "When both lists are already sorted you only need one pass. "
                    "Keep a pointer in each list, compare the current values, "
                    "pick the smaller one, advance that pointer."
                ),
                "examples": [
                    "i, j = 0, 0",
                    "while i < len(a) and j < len(b):",
                    "    if a[i] <= b[j]:",
                    "        result.append(a[i]); i += 1",
                    "    else:",
                    "        result.append(b[j]); j += 1",
                ],
                "watch_out": (
                    "When one list is exhausted the other may still have elements. "
                    "After the while loop, extend the result with a[i:] and b[j:] to capture the remainder."
                ),
            },
            {
                "title": "Slicing to Get the Remainder  list[i:]",
                "explanation": (
                    "list[i:] returns all elements from index i to the end. "
                    "If i >= len(list) it returns an empty list — safe to extend with."
                ),
                "examples": [
                    "[1,2,3,4][2:]   # [3, 4]",
                    "[1,2,3,4][4:]   # []  — index past end returns empty",
                ],
                "watch_out": (
                    "a[i:] and b[j:] after the merge loop will each be either empty or the remaining tail. "
                    "It is safe to extend with both without checking — if one is empty, extend does nothing."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html",
    },

    # ──────────────────────────────────────────────
    # DATA STRUCTURES — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "stack-push-pop",
        "topic": "data-structures",
        "difficulty": "beginner",
        "language": "python",
        "title": "Stack: Push and Pop",
        "description": (
            "A stack is Last-In First-Out (LIFO). Write a function called `solution` "
            "that takes a list of string operations and returns the top element after all operations.\n"
            "Operations:\n  'push:X' — push integer X onto the stack\n  'pop' — remove the top element\n\n"
            "Example:\n  solution(['push:1','push:2','pop','push:3']) → 3"
        ),
        "starter_code": "def solution(ops: list) -> int:\n    stack = []\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(['push:1','push:2','pop','push:3'])", "expected_output": "3"},
            {"input": "solution(['push:5'])",                          "expected_output": "5"},
            {"input": "solution(['push:1','push:2'])",                 "expected_output": "2"},
        ],
        "hint": "A Python list is a perfect stack: append() to push, pop() to remove the last element.",
        "solution": (
            "def solution(ops: list) -> int:\n"
            "    stack = []\n"
            "    for op in ops:\n"
            "        if op.startswith('push:'):\n"
            "            stack.append(int(op.split(':')[1]))\n"
            "        elif op == 'pop':\n"
            "            stack.pop()\n"
            "    return stack[-1]"
        ),
        "concepts": [
            {
                "title": "Python List as a Stack",
                "explanation": (
                    "A list naturally behaves as a stack: append() pushes to the top (end), "
                    "pop() removes and returns the top element."
                ),
                "examples": [
                    "stack = []",
                    "stack.append(1)   # push",
                    "stack.append(2)   # push",
                    "stack.pop()       # returns 2, stack is now [1]",
                    "stack[-1]         # peek — see top without removing",
                ],
                "watch_out": (
                    "stack.pop() on an empty list raises an IndexError. "
                    "Always check 'if stack:' before popping if there is any chance the stack is empty."
                ),
            },
            {
                "title": "str.split(separator)",
                "explanation": (
                    "split() breaks a string into a list of substrings at each occurrence of separator."
                ),
                "examples": [
                    '"push:5".split(":")   # ["push", "5"]',
                    '"a,b,c".split(",")    # ["a", "b", "c"]',
                    '"hello".split()       # ["hello"] — split on whitespace',
                ],
                "watch_out": (
                    "split() returns strings, not integers. "
                    "You must convert: int(op.split(':')[1])"
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks",
    },

    {
        "id": "valid-parentheses",
        "topic": "data-structures",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Valid Parentheses",
        "description": (
            "Write a function called `solution` that takes a string of brackets "
            "and returns True if every opening bracket is closed in the correct order, "
            "False otherwise. Brackets: () [] {}\n\n"
            "Example:\n  solution('()[]{}') → True\n  solution('([)]') → False"
        ),
        "starter_code": "def solution(s: str) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("()[]{}")',  "expected_output": "True"},
            {"input": 'solution("([])")',    "expected_output": "True"},
            {"input": 'solution("([)]")',    "expected_output": "False"},
            {"input": 'solution("{")',       "expected_output": "False"},
            {"input": 'solution("")',        "expected_output": "True"},
        ],
        "hint": "Use a stack. Push opening brackets. When you see a closing bracket, check whether the top of the stack is the matching opener.",
        "solution": (
            "def solution(s: str) -> bool:\n"
            "    pairs = {')': '(', ']': '[', '}': '{'}\n"
            "    stack = []\n"
            "    for ch in s:\n"
            "        if ch in pairs:\n"
            "            if not stack or stack[-1] != pairs[ch]:\n"
            "                return False\n"
            "            stack.pop()\n"
            "        else:\n"
            "            stack.append(ch)\n"
            "    return len(stack) == 0"
        ),
        "concepts": [
            {
                "title": "Dict as a Lookup Table",
                "explanation": (
                    "Instead of a chain of if/elif, store mappings in a dict "
                    "and look them up in O(1)."
                ),
                "examples": [
                    "pairs = {')': '(', ']': '[', '}': '{'}",
                    "pairs[')']   # '('  — the matching opener",
                    "')' in pairs # True — it is a closer",
                ],
                "watch_out": (
                    "Checking 'ch in pairs' only tells you it is a closing bracket. "
                    "Opening brackets are NOT in pairs as keys — they fall into the else branch."
                ),
            },
            {
                "title": "Stack-Based Matching",
                "explanation": (
                    "Push every opener. When you see a closer, the stack's top must be its matching opener. "
                    "If not — or the stack is empty — the string is invalid."
                ),
                "examples": [
                    "# For '([])' the stack evolves:",
                    "# '(' → stack: ['(']",
                    "# '[' → stack: ['(', '[']",
                    "# ']' → pop '[', matches → stack: ['(']",
                    "# ')' → pop '(', matches → stack: []",
                    "# empty stack at end → True",
                ],
                "watch_out": (
                    "At the end, the stack must be empty. "
                    "If it still has elements, some openers were never closed — return False."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks",
    },

    # ──────────────────────────────────────────────
    # OOP — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "bank-account",
        "topic": "oop",
        "difficulty": "beginner",
        "language": "python",
        "title": "Bank Account Class",
        "description": (
            "Write a class called `BankAccount` with:\n"
            "  - An __init__ that takes an owner name and sets balance to 0\n"
            "  - deposit(amount) — adds amount to balance\n"
            "  - withdraw(amount) — subtracts amount (do nothing if insufficient funds)\n"
            "  - get_balance() — returns the current balance\n\n"
            "Then write `solution(owner, ops)` that creates a BankAccount, applies a list of "
            "('deposit', n) or ('withdraw', n) tuples, and returns the final balance."
        ),
        "starter_code": (
            "class BankAccount:\n"
            "    def __init__(self, owner: str):\n"
            "        pass\n\n"
            "    def deposit(self, amount: float):\n"
            "        pass\n\n"
            "    def withdraw(self, amount: float):\n"
            "        pass\n\n"
            "    def get_balance(self) -> float:\n"
            "        pass\n\n\n"
            "def solution(owner: str, ops: list) -> float:\n"
            "    # Create an account and apply ops\n"
            "    pass"
        ),
        "test_cases": [
            {"input": "solution('Alice', [('deposit', 100), ('withdraw', 30)])",  "expected_output": "70"},
            {"input": "solution('Bob', [('deposit', 50), ('withdraw', 100)])",     "expected_output": "50"},
            {"input": "solution('Eve', [])",                                        "expected_output": "0"},
        ],
        "hint": "Store the balance as self.balance. In withdraw, check if amount <= self.balance before subtracting.",
        "solution": (
            "class BankAccount:\n"
            "    def __init__(self, owner: str):\n"
            "        self.owner = owner\n"
            "        self.balance = 0\n\n"
            "    def deposit(self, amount: float):\n"
            "        self.balance += amount\n\n"
            "    def withdraw(self, amount: float):\n"
            "        if amount <= self.balance:\n"
            "            self.balance -= amount\n\n"
            "    def get_balance(self) -> float:\n"
            "        return self.balance\n\n\n"
            "def solution(owner: str, ops: list) -> float:\n"
            "    account = BankAccount(owner)\n"
            "    for op, amount in ops:\n"
            "        if op == 'deposit':\n"
            "            account.deposit(amount)\n"
            "        elif op == 'withdraw':\n"
            "            account.withdraw(amount)\n"
            "    return account.get_balance()"
        ),
        "concepts": [
            {
                "title": "Classes and __init__",
                "explanation": (
                    "__init__ is called automatically when you create an instance. "
                    "Use it to set up the object's initial state using self."
                ),
                "examples": [
                    "class Dog:",
                    "    def __init__(self, name):",
                    "        self.name = name   # instance attribute",
                    "        self.tricks = []",
                    "",
                    "d = Dog('Rex')  # __init__ called automatically",
                    "d.name          # 'Rex'",
                ],
                "watch_out": (
                    "Forgetting self as the first parameter of every method will raise a TypeError. "
                    "self refers to the specific instance the method was called on."
                ),
            },
            {
                "title": "Instance Attributes  (self.x)",
                "explanation": (
                    "Attributes attached to self exist on each individual object. "
                    "Every BankAccount has its own balance — changing one does not affect another."
                ),
                "examples": [
                    "self.balance = 0       # set in __init__",
                    "self.balance += 100    # update in deposit",
                    "return self.balance    # read in get_balance",
                ],
                "watch_out": (
                    "If you write balance = 0 inside __init__ without self., "
                    "it creates a local variable that disappears when __init__ returns. "
                    "Always use self.balance."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/classes.html",
    },

    # ──────────────────────────────────────────────
    # OOP — INTERMEDIATE
    # ──────────────────────────────────────────────

    {
        "id": "shape-area",
        "topic": "oop",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Shape Hierarchy",
        "description": (
            "Create a base class `Shape` with an `area()` method that returns 0. "
            "Then create `Circle(radius)` and `Rectangle(width, height)` that override area().\n"
            "Use 3.14159 for pi.\n\n"
            "Write `solution(shape_type, *args)` that creates the right shape and returns its area "
            "rounded to 2 decimal places.\n\n"
            "Example:\n  solution('circle', 5) → 78.54\n  solution('rectangle', 4, 6) → 24.0"
        ),
        "starter_code": (
            "class Shape:\n"
            "    def area(self) -> float:\n"
            "        return 0\n\n\n"
            "class Circle(Shape):\n"
            "    def __init__(self, radius):\n"
            "        pass\n\n"
            "    def area(self) -> float:\n"
            "        pass\n\n\n"
            "class Rectangle(Shape):\n"
            "    def __init__(self, width, height):\n"
            "        pass\n\n"
            "    def area(self) -> float:\n"
            "        pass\n\n\n"
            "def solution(shape_type: str, *args) -> float:\n"
            "    pass"
        ),
        "test_cases": [
            {"input": "solution('circle', 5)",       "expected_output": "78.54"},
            {"input": "solution('rectangle', 4, 6)", "expected_output": "24.0"},
            {"input": "solution('circle', 1)",        "expected_output": "3.14"},
        ],
        "hint": "Subclasses call the parent via class MyClass(ParentClass). Override area() by defining a method with the same name.",
        "solution": (
            "class Shape:\n"
            "    def area(self) -> float:\n"
            "        return 0\n\n\n"
            "class Circle(Shape):\n"
            "    def __init__(self, radius):\n"
            "        self.radius = radius\n\n"
            "    def area(self) -> float:\n"
            "        return 3.14159 * self.radius ** 2\n\n\n"
            "class Rectangle(Shape):\n"
            "    def __init__(self, width, height):\n"
            "        self.width = width\n"
            "        self.height = height\n\n"
            "    def area(self) -> float:\n"
            "        return self.width * self.height\n\n\n"
            "def solution(shape_type: str, *args) -> float:\n"
            "    if shape_type == 'circle':\n"
            "        return round(Circle(args[0]).area(), 2)\n"
            "    elif shape_type == 'rectangle':\n"
            "        return round(Rectangle(args[0], args[1]).area(), 2)"
        ),
        "concepts": [
            {
                "title": "Inheritance",
                "explanation": (
                    "A subclass inherits all methods from its parent. "
                    "You can override a method by redefining it in the subclass."
                ),
                "examples": [
                    "class Animal:",
                    "    def speak(self): return 'generic sound'",
                    "",
                    "class Dog(Animal):",
                    "    def speak(self): return 'Woof'  # overrides parent",
                    "",
                    "Dog().speak()   # 'Woof'",
                ],
                "watch_out": (
                    "If you forget to override area() in a subclass, calling .area() will use "
                    "the parent's version (which returns 0). Python will not warn you."
                ),
            },
            {
                "title": "*args — Variable Positional Arguments",
                "explanation": (
                    "*args lets a function accept any number of positional arguments. "
                    "Inside the function, args is a tuple."
                ),
                "examples": [
                    "def solution(shape, *args):",
                    "    print(args)       # tuple of extra arguments",
                    "",
                    "solution('circle', 5)          # args = (5,)",
                    "solution('rectangle', 4, 6)    # args = (4, 6)",
                    "args[0]  # first extra arg",
                ],
                "watch_out": (
                    "args is a tuple, not a list. args[0] works fine for reading, "
                    "but you cannot append to it."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/classes.html#inheritance",
    },

    # ──────────────────────────────────────────────
    # BEST PRACTICES — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "list-comprehension",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "python",
        "title": "List Comprehension",
        "description": (
            "Write a function called `solution` that takes a list of integers and returns "
            "a new list containing only the even numbers, each multiplied by 2. "
            "Use a list comprehension — no explicit for loop.\n\n"
            "Example:\n  solution([1, 2, 3, 4, 5]) → [4, 8]"
        ),
        "starter_code": "def solution(nums: list) -> list:\n    # Use a list comprehension\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 3, 4, 5])",   "expected_output": "[4, 8]"},
            {"input": "solution([2, 4, 6])",           "expected_output": "[4, 8, 12]"},
            {"input": "solution([1, 3, 5])",           "expected_output": "[]"},
            {"input": "solution([])",                  "expected_output": "[]"},
        ],
        "hint": "List comprehension syntax: [expression for item in iterable if condition]",
        "solution": (
            "def solution(nums: list) -> list:\n"
            "    return [n * 2 for n in nums if n % 2 == 0]"
        ),
        "concepts": [
            {
                "title": "List Comprehensions",
                "explanation": (
                    "A list comprehension is a compact way to build a list. "
                    "It reads almost like English: "
                    "'give me [expression] for each [item] in [iterable] if [condition]'."
                ),
                "examples": [
                    "# Basic: square every number",
                    "[x**2 for x in range(5)]          # [0, 1, 4, 9, 16]",
                    "",
                    "# With filter: only evens",
                    "[x for x in nums if x % 2 == 0]",
                    "",
                    "# Transform + filter:",
                    "[x * 2 for x in nums if x % 2 == 0]",
                ],
                "watch_out": (
                    "The if clause filters which items are included — it does NOT replace an if/else. "
                    "For if/else inside the expression use: [a if cond else b for x in nums]."
                ),
            },
            {
                "title": "Readability First",
                "explanation": (
                    "List comprehensions are Pythonic when the logic is simple. "
                    "If the expression becomes hard to read, a regular loop is better."
                ),
                "examples": [
                    "# Clear — good comprehension:",
                    "[x * 2 for x in nums if x % 2 == 0]",
                    "",
                    "# Too complex — use a loop instead:",
                    "[f(g(x)) for x in items if h(x) and not j(x)]",
                ],
                "watch_out": (
                    "A comprehension inside a comprehension (nested) is usually a sign to refactor. "
                    "One level deep is the sweet spot."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
    },

    {
        "id": "guard-clauses",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "python",
        "title": "Guard Clauses",
        "description": (
            "The function below has deeply nested ifs. Rewrite it using guard clauses "
            "(early returns) so the happy path is at the bottom with no nesting.\n\n"
            "The function `solution(age, has_id, is_member)` should return:\n"
            "  'too young' if age < 18\n"
            "  'no ID' if not has_id\n"
            "  'not a member' if not is_member\n"
            "  'welcome' otherwise"
        ),
        "starter_code": (
            "def solution(age: int, has_id: bool, is_member: bool) -> str:\n"
            "    # Rewrite using guard clauses (early returns)\n"
            "    if age >= 18:\n"
            "        if has_id:\n"
            "            if is_member:\n"
            "                return 'welcome'\n"
            "            else:\n"
            "                return 'not a member'\n"
            "        else:\n"
            "            return 'no ID'\n"
            "    else:\n"
            "        return 'too young'"
        ),
        "test_cases": [
            {"input": "solution(20, True, True)",   "expected_output": "welcome"},
            {"input": "solution(16, True, True)",   "expected_output": "too young"},
            {"input": "solution(20, False, True)",  "expected_output": "no ID"},
            {"input": "solution(20, True, False)",  "expected_output": "not a member"},
        ],
        "hint": "Flip each condition and return early. The function's last line should be the happy path.",
        "solution": (
            "def solution(age: int, has_id: bool, is_member: bool) -> str:\n"
            "    if age < 18:\n"
            "        return 'too young'\n"
            "    if not has_id:\n"
            "        return 'no ID'\n"
            "    if not is_member:\n"
            "        return 'not a member'\n"
            "    return 'welcome'"
        ),
        "concepts": [
            {
                "title": "Guard Clauses (Early Returns)",
                "explanation": (
                    "A guard clause checks a failure condition and returns immediately. "
                    "This avoids deep nesting and makes the happy path obvious at the end."
                ),
                "examples": [
                    "# Nested — hard to read:",
                    "if condition_a:",
                    "    if condition_b:",
                    "        return 'ok'",
                    "",
                    "# Guard clauses — easy to read:",
                    "if not condition_a: return 'fail a'",
                    "if not condition_b: return 'fail b'",
                    "return 'ok'",
                ],
                "watch_out": (
                    "Guard clauses work best for validation and error cases. "
                    "Do not use early returns in the middle of complex logic — "
                    "that makes code harder to follow, not easier."
                ),
            },
            {
                "title": "not Operator",
                "explanation": (
                    "'not' flips a boolean. 'not True' is False, 'not False' is True. "
                    "It also works on truthy/falsy values."
                ),
                "examples": [
                    "not True     # False",
                    "not False    # True",
                    "not []       # True  (empty list is falsy)",
                    "not [1,2]    # False (non-empty list is truthy)",
                ],
                "watch_out": (
                    "if not has_id is cleaner than if has_id == False. "
                    "Avoid comparing booleans with ==."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/reference/simple_stmts.html#the-return-statement",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "word-frequency",
        "topic": "scripting",
        "difficulty": "beginner",
        "language": "python",
        "title": "Word Frequency Counter",
        "description": (
            "Write a function called `solution` that takes a sentence string and returns "
            "a dictionary with each word as a key and its count as the value. "
            "Ignore case and punctuation (.,!?).\n\n"
            "Example:\n  solution('Hello world hello') → {'hello': 2, 'world': 1}"
        ),
        "starter_code": "def solution(text: str) -> dict:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("Hello world hello")',       "expected_output": "{'hello': 2, 'world': 1}"},
            {"input": 'solution("one")',                     "expected_output": "{'one': 1}"},
            {"input": 'solution("hi hi hi")',               "expected_output": "{'hi': 3}"},
        ],
        "hint": "Use a dict to count. For each word, increment its count by 1 (or start at 0 with dict.get).",
        "solution": (
            "def solution(text: str) -> dict:\n"
            "    counts = {}\n"
            "    for ch in '.,!?':\n"
            "        text = text.replace(ch, '')\n"
            "    for word in text.lower().split():\n"
            "        counts[word] = counts.get(word, 0) + 1\n"
            "    return counts"
        ),
        "concepts": [
            {
                "title": "dict.get(key, default)",
                "explanation": (
                    "get() returns the value for a key, or a default if the key does not exist. "
                    "Essential for counting patterns: get the current count (default 0) and add 1."
                ),
                "examples": [
                    "counts = {}",
                    "counts.get('hello', 0)       # 0 — key not yet in dict",
                    "counts['hello'] = counts.get('hello', 0) + 1",
                    "counts.get('hello', 0)       # 1",
                ],
                "watch_out": (
                    "counts['hello'] raises a KeyError if 'hello' is not in the dict. "
                    "counts.get('hello', 0) is safe — returns 0 instead of crashing."
                ),
            },
            {
                "title": "str.split() — Splitting on Whitespace",
                "explanation": (
                    "split() with no argument splits on any whitespace and discards empty strings. "
                    "It handles multiple spaces, tabs, and newlines automatically."
                ),
                "examples": [
                    '"hello world".split()        # ["hello", "world"]',
                    '"  lots   of spaces  ".split() # ["lots", "of", "spaces"]',
                    '"a,b,c".split(",")           # ["a", "b", "c"]',
                ],
                "watch_out": (
                    '"hello world".split(" ") splits on exactly one space — '
                    'multiple spaces produce empty strings in the result. '
                    'Prefer split() with no argument for general text.'
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#dict.get",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "check-anagram",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Check Anagram",
        "description": (
            "Write a function called `solution` that takes two strings and returns True if "
            "they are anagrams of each other (same letters, different order), False otherwise. "
            "Ignore case.\n\n"
            "Example:\n  solution('listen', 'silent') → True\n  solution('hello', 'world') → False"
        ),
        "starter_code": "def solution(a: str, b: str) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("listen", "silent")', "expected_output": "True"},
            {"input": 'solution("hello", "world")',   "expected_output": "False"},
            {"input": 'solution("Abc", "cab")',        "expected_output": "True"},
            {"input": 'solution("abc", "ab")',         "expected_output": "False"},
        ],
        "hint": "Sort both strings and compare — anagrams produce identical sorted results.",
        "solution": (
            "def solution(a: str, b: str) -> bool:\n"
            "    return sorted(a.lower()) == sorted(b.lower())"
        ),
        "concepts": [
            {
                "title": "sorted() on a String",
                "explanation": (
                    "sorted() works on any iterable, including strings. "
                    "It returns a sorted list of characters. "
                    "Two strings with the same characters will produce identical sorted lists."
                ),
                "examples": [
                    'sorted("listen")   # [\'e\', \'i\', \'l\', \'n\', \'s\', \'t\']',
                    'sorted("silent")   # [\'e\', \'i\', \'l\', \'n\', \'s\', \'t\']',
                    'sorted("listen") == sorted("silent")  # True',
                ],
                "watch_out": (
                    "sorted() returns a list, not a string. "
                    "Comparing sorted('abc') to sorted('cab') works because list equality compares element-by-element. "
                    "No need to join back into a string."
                ),
            },
            {
                "title": "str.lower() for Case-Insensitive Comparison",
                "explanation": (
                    "lower() returns a new string with all letters converted to lowercase. "
                    "Call it on both strings before comparing so 'A' and 'a' are treated the same."
                ),
                "examples": [
                    '"Hello".lower()    # "hello"',
                    '"ABC".lower()      # "abc"',
                    '"already".lower()  # "already" — no change',
                ],
                "watch_out": (
                    "lower() does not modify the original string — strings are immutable in Python. "
                    "It returns a new string, so you must use the return value."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#sorted",
    },

    {
        "id": "capitalize-words",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Capitalize Each Word",
        "description": (
            "Write a function called `solution` that takes a sentence and returns it "
            "with the first letter of every word capitalised and the rest lowercase.\n\n"
            "Example:\n  solution('hello world') → 'Hello World'\n  solution('the QUICK brown FOX') → 'The Quick Brown Fox'"
        ),
        "starter_code": "def solution(sentence: str) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("hello world")',        "expected_output": "Hello World"},
            {"input": 'solution("the QUICK brown FOX")', "expected_output": "The Quick Brown Fox"},
            {"input": 'solution("python")',             "expected_output": "Python"},
            {"input": 'solution("a b c")',              "expected_output": "A B C"},
        ],
        "hint": "Split into words, apply str.capitalize() to each, then join with spaces.",
        "solution": (
            "def solution(sentence: str) -> str:\n"
            "    return ' '.join(word.capitalize() for word in sentence.split())"
        ),
        "concepts": [
            {
                "title": "str.capitalize() vs str.upper() vs str.title()",
                "explanation": (
                    "capitalize() makes the first character uppercase and the rest lowercase. "
                    "upper() makes ALL characters uppercase. "
                    "title() is a one-liner for this exercise but has edge cases (it capitalises after any non-letter)."
                ),
                "examples": [
                    '"hello".capitalize()  # "Hello"',
                    '"hELLO".capitalize()  # "Hello"  — rest forced lowercase',
                    '"hello world".title() # "Hello World"',
                    '"it\'s".title()       # "It\'S"  — the s after \' is also capitalised!',
                ],
                "watch_out": (
                    "str.title() is tempting but has a known bug: it capitalises any letter after a non-letter, "
                    "so \"it's\" becomes \"It'S\". Using split + capitalize + join is safer."
                ),
            },
            {
                "title": "str.join() — Assembling a String from Parts",
                "explanation": (
                    "separator.join(iterable) concatenates all strings in the iterable, "
                    "placing separator between each pair."
                ),
                "examples": [
                    '" ".join(["Hello", "World"])  # "Hello World"',
                    '"-".join(["a", "b", "c"])     # "a-b-c"',
                    '"".join(["h","i"])             # "hi"',
                ],
                "watch_out": (
                    "join() is the fast way to concatenate many strings. "
                    "Using result += word in a loop is slow because strings are immutable — "
                    "each += creates a brand-new string object."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.capitalize",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "rotate-list",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Rotate a List",
        "description": (
            "Write a function called `solution` that takes a list and an integer k, "
            "and returns the list rotated to the right by k positions.\n\n"
            "Example:\n  solution([1, 2, 3, 4, 5], 2) → [4, 5, 1, 2, 3]\n"
            "  solution([1, 2, 3], 1) → [3, 1, 2]"
        ),
        "starter_code": "def solution(nums: list, k: int) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 3, 4, 5], 2)", "expected_output": "[4, 5, 1, 2, 3]"},
            {"input": "solution([1, 2, 3], 1)",        "expected_output": "[3, 1, 2]"},
            {"input": "solution([1, 2, 3], 0)",        "expected_output": "[1, 2, 3]"},
            {"input": "solution([1, 2, 3], 3)",        "expected_output": "[1, 2, 3]"},
        ],
        "hint": "Use the modulo operator to handle k larger than the list length. Then slice: the last k elements come first.",
        "solution": (
            "def solution(nums: list, k: int) -> list:\n"
            "    if not nums:\n"
            "        return nums\n"
            "    k = k % len(nums)\n"
            "    return nums[-k:] + nums[:-k] if k else nums[:]"
        ),
        "concepts": [
            {
                "title": "Modulo for Wrap-Around  %",
                "explanation": (
                    "k % n keeps k within the range 0..n-1. "
                    "Rotating by the list's length is the same as not rotating at all — "
                    "modulo handles any k automatically."
                ),
                "examples": [
                    "# List of length 3:",
                    "k=4 → 4 % 3 = 1   # same as rotating by 1",
                    "k=3 → 3 % 3 = 0   # no rotation needed",
                    "k=0 → 0 % 3 = 0   # no rotation",
                ],
                "watch_out": (
                    "Always apply modulo before slicing. "
                    "nums[-0:] is the same as nums[0:] (the whole list), not an empty slice — "
                    "the k=0 edge case needs a separate check or the ternary `if k else nums[:]`."
                ),
            },
            {
                "title": "Combining Slices with +",
                "explanation": (
                    "You can concatenate two list slices with +. "
                    "For a right rotation by k: take the last k elements, then the rest."
                ),
                "examples": [
                    "nums = [1, 2, 3, 4, 5]",
                    "k = 2",
                    "nums[-2:]      # [4, 5]  — last 2",
                    "nums[:-2]      # [1, 2, 3]  — everything before",
                    "nums[-2:] + nums[:-2]  # [4, 5, 1, 2, 3]",
                ],
                "watch_out": (
                    "nums[-0:] is nums[0:] — the whole list — so k=0 must be handled before slicing. "
                    "The ternary `... if k else nums[:]` is the cleanest fix."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/introduction.html#lists",
    },

    {
        "id": "string-compression",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "String Compression",
        "description": (
            "Write a function called `solution` that compresses a string using run-length encoding. "
            "Replace consecutive repeated characters with the character followed by its count.\n\n"
            "Example:\n  solution('aabccc') → 'a2b1c3'\n  solution('aaaa') → 'a4'"
        ),
        "starter_code": "def solution(s: str) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("aabccc")', "expected_output": "a2b1c3"},
            {"input": 'solution("aaaa")',   "expected_output": "a4"},
            {"input": 'solution("abc")',    "expected_output": "a1b1c1"},
            {"input": 'solution("a")',      "expected_output": "a1"},
        ],
        "hint": "Walk through the string keeping track of the current character and how many times you have seen it in a row.",
        "solution": (
            "def solution(s: str) -> str:\n"
            "    if not s:\n"
            "        return ''\n"
            "    result = []\n"
            "    count = 1\n"
            "    for i in range(1, len(s)):\n"
            "        if s[i] == s[i - 1]:\n"
            "            count += 1\n"
            "        else:\n"
            "            result.append(s[i - 1] + str(count))\n"
            "            count = 1\n"
            "    result.append(s[-1] + str(count))\n"
            "    return ''.join(result)"
        ),
        "concepts": [
            {
                "title": "Iterating with an Index  range(1, len(s))",
                "explanation": (
                    "When you need to compare adjacent characters, iterate by index so you can "
                    "look at both s[i] and s[i-1] at the same time."
                ),
                "examples": [
                    's = "aab"',
                    "for i in range(1, len(s)):",
                    "    print(s[i-1], s[i])  # ('a','a'), ('a','b')",
                ],
                "watch_out": (
                    "Start the range at 1 (not 0) so s[i-1] is always valid. "
                    "After the loop, don't forget to flush the last character and count."
                ),
            },
            {
                "title": "Building Strings Efficiently with a List",
                "explanation": (
                    "Appending to a list and joining at the end is faster than "
                    "result += char in a loop, because strings are immutable — "
                    "each += allocates a new string."
                ),
                "examples": [
                    "parts = []",
                    "parts.append('a' + str(3))  # 'a3'",
                    "parts.append('b' + str(1))  # 'b1'",
                    "''.join(parts)               # 'a3b1'",
                ],
                "watch_out": (
                    "str(count) converts the integer to a string. "
                    "'a' + 3 raises a TypeError — you cannot concatenate str and int directly."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.join",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "sum-of-digits",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Sum of Digits",
        "description": (
            "Write a function called `solution` that takes a non-negative integer and "
            "returns the sum of its digits.\n\n"
            "Example:\n  solution(123) → 6\n  solution(9999) → 36"
        ),
        "starter_code": "def solution(n: int) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(123)",  "expected_output": "6"},
            {"input": "solution(0)",    "expected_output": "0"},
            {"input": "solution(9999)", "expected_output": "36"},
            {"input": "solution(100)",  "expected_output": "1"},
        ],
        "hint": "Convert the number to a string, iterate over each character, convert back to int, and sum them up.",
        "solution": (
            "def solution(n: int) -> int:\n"
            "    return sum(int(d) for d in str(n))"
        ),
        "concepts": [
            {
                "title": "str() and int() — Converting Between Types",
                "explanation": (
                    "str(n) converts an integer to a string so you can iterate over its digits. "
                    "int(d) converts each character digit back to an integer for arithmetic."
                ),
                "examples": [
                    'str(123)       # "123"',
                    'for d in str(123): print(d)   # "1", "2", "3"',
                    'int("7")       # 7',
                    'sum(int(d) for d in str(123))  # 6',
                ],
                "watch_out": (
                    'int("7") works because "7" is a valid integer string. '
                    'int("a") raises a ValueError. '
                    "Always make sure the string contains only digit characters before converting."
                ),
            },
            {
                "title": "Generator Expressions inside sum()",
                "explanation": (
                    "sum() accepts any iterable, including a generator expression. "
                    "You can compute and sum in one line without building an intermediate list."
                ),
                "examples": [
                    "sum(int(d) for d in '123')   # 6",
                    "sum(x**2 for x in range(4))  # 0+1+4+9 = 14",
                ],
                "watch_out": (
                    "A generator expression (round brackets) is lazy — values are produced one at a time. "
                    "A list comprehension (square brackets) builds the whole list first. "
                    "For sum(), the generator is more memory-efficient."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#sum",
    },

    {
        "id": "count-occurrences",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Count Occurrences",
        "description": (
            "Write a function called `solution` that takes a list and a target value, "
            "and returns how many times the target appears in the list. "
            "Do not use list.count().\n\n"
            "Example:\n  solution([1, 2, 2, 3, 2], 2) → 3"
        ),
        "starter_code": "def solution(items: list, target) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 2, 3, 2], 2)", "expected_output": "3"},
            {"input": "solution([1, 2, 3], 4)",        "expected_output": "0"},
            {"input": "solution([], 1)",               "expected_output": "0"},
            {"input": "solution([5, 5, 5], 5)",        "expected_output": "3"},
        ],
        "hint": "Use a for loop and a counter variable. Increment the counter each time you find the target.",
        "solution": (
            "def solution(items: list, target) -> int:\n"
            "    count = 0\n"
            "    for item in items:\n"
            "        if item == target:\n"
            "            count += 1\n"
            "    return count"
        ),
        "concepts": [
            {
                "title": "Accumulator Pattern",
                "explanation": (
                    "Start a variable at 0 (or an empty collection), then update it each loop iteration. "
                    "This is one of the most fundamental patterns in programming."
                ),
                "examples": [
                    "count = 0",
                    "for item in items:",
                    "    if item == target:",
                    "        count += 1   # accumulate",
                    "return count",
                ],
                "watch_out": (
                    "Make sure to initialise the accumulator BEFORE the loop, not inside it. "
                    "Initialising inside would reset it to 0 every iteration."
                ),
            },
            {
                "title": "== vs is",
                "explanation": (
                    "== checks value equality (do they contain the same data?). "
                    "is checks identity (are they the exact same object in memory?). "
                    "Always use == for comparisons unless you specifically need identity."
                ),
                "examples": [
                    "a = [1, 2]",
                    "b = [1, 2]",
                    "a == b   # True  — same values",
                    "a is b   # False — different objects",
                    "",
                    "# Use is only for None checks:",
                    "if x is None: ...",
                ],
                "watch_out": (
                    "Using is to compare integers or strings can sometimes work by accident "
                    "(Python caches small integers). Never rely on this — always use ==."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/controlflow.html#for-statements",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "selection-sort",
        "topic": "algorithms",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Selection Sort",
        "description": (
            "Write a function called `solution` that sorts a list of integers in ascending order "
            "using selection sort. Return the sorted list. Do not use sort() or sorted().\n\n"
            "Selection sort: find the minimum of the unsorted portion, swap it into place, repeat.\n\n"
            "Example:\n  solution([64, 25, 12, 22, 11]) → [11, 12, 22, 25, 64]"
        ),
        "starter_code": "def solution(nums: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([64, 25, 12, 22, 11])", "expected_output": "[11, 12, 22, 25, 64]"},
            {"input": "solution([3, 1, 2])",             "expected_output": "[1, 2, 3]"},
            {"input": "solution([1])",                   "expected_output": "[1]"},
            {"input": "solution([5, 5, 1])",             "expected_output": "[1, 5, 5]"},
        ],
        "hint": "Use an outer loop from 0 to n. Inside, find the index of the minimum in the remaining slice, then swap it with position i.",
        "solution": (
            "def solution(nums: list) -> list:\n"
            "    nums = nums[:]\n"
            "    n = len(nums)\n"
            "    for i in range(n):\n"
            "        min_idx = i\n"
            "        for j in range(i + 1, n):\n"
            "            if nums[j] < nums[min_idx]:\n"
            "                min_idx = j\n"
            "        nums[i], nums[min_idx] = nums[min_idx], nums[i]\n"
            "    return nums"
        ),
        "concepts": [
            {
                "title": "Tracking the Index of a Minimum",
                "explanation": (
                    "Instead of storing the minimum value, store its index. "
                    "That way you know exactly where to swap it to."
                ),
                "examples": [
                    "nums = [3, 1, 4, 1]",
                    "min_idx = 0",
                    "for j in range(1, len(nums)):",
                    "    if nums[j] < nums[min_idx]:",
                    "        min_idx = j",
                    "# min_idx is now 1 (value 1)",
                ],
                "watch_out": (
                    "Initialise min_idx = i (the start of the unsorted portion), not 0. "
                    "Starting at 0 every time would incorrectly search already-sorted elements."
                ),
            },
            {
                "title": "Nested Loops for O(n²) Algorithms",
                "explanation": (
                    "Selection sort has two loops: an outer one that moves the boundary, "
                    "and an inner one that scans the unsorted portion. "
                    "This gives O(n²) time — fine for small lists, slow for large ones."
                ),
                "examples": [
                    "for i in range(n):          # outer: sorted boundary",
                    "    for j in range(i+1, n): # inner: scan unsorted",
                    "        ...",
                ],
                "watch_out": (
                    "Selection sort always does O(n²) comparisons regardless of input order. "
                    "Bubble sort can exit early if the list is already sorted, but selection sort cannot."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/howto/sorting.html",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — ADVANCED (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "climbing-stairs",
        "topic": "algorithms",
        "difficulty": "advanced",
        "language": "python",
        "title": "Climbing Stairs (DP)",
        "description": (
            "You are climbing a staircase with n steps. Each time you can either climb 1 or 2 steps. "
            "Write a function called `solution` that returns the number of distinct ways to reach the top.\n\n"
            "Example:\n  solution(2) → 2  (1+1 or 2)\n  solution(3) → 3  (1+1+1, 1+2, 2+1)\n  solution(5) → 8"
        ),
        "starter_code": "def solution(n: int) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(1)", "expected_output": "1"},
            {"input": "solution(2)", "expected_output": "2"},
            {"input": "solution(3)", "expected_output": "3"},
            {"input": "solution(5)", "expected_output": "8"},
        ],
        "hint": "Notice the pattern: ways(n) = ways(n-1) + ways(n-2). This is Fibonacci! Use two variables to avoid recursion.",
        "solution": (
            "def solution(n: int) -> int:\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    a, b = 1, 1\n"
            "    for _ in range(2, n + 1):\n"
            "        a, b = b, a + b\n"
            "    return b"
        ),
        "concepts": [
            {
                "title": "Dynamic Programming — Bottom-Up",
                "explanation": (
                    "Dynamic programming solves a problem by building up from smaller sub-problems. "
                    "Here, the number of ways to reach step n depends only on steps n-1 and n-2 — "
                    "so you only need to keep two values."
                ),
                "examples": [
                    "# ways(1)=1, ways(2)=2, ways(3)=3, ways(4)=5 ...",
                    "a, b = 1, 1   # ways(0), ways(1)",
                    "# each iteration: new b = a+b, new a = old b",
                    "a, b = b, a + b",
                ],
                "watch_out": (
                    "The naive recursive approach recomputes the same values many times (exponential time). "
                    "The iterative approach is O(n) time and O(1) space — always prefer it."
                ),
            },
            {
                "title": "Simultaneous Assignment  a, b = b, a + b",
                "explanation": (
                    "Python evaluates the right side completely before assigning. "
                    "So a, b = b, a + b correctly uses the OLD values of a and b on the right. "
                    "No temporary variable needed."
                ),
                "examples": [
                    "a, b = 1, 1",
                    "a, b = b, a + b   # a=1, b=2",
                    "a, b = b, a + b   # a=2, b=3",
                    "a, b = b, a + b   # a=3, b=5",
                ],
                "watch_out": (
                    "If you write a = b; b = a + b, the second line uses the NEW value of a (which is b), "
                    "not the old one. The single-line swap avoids this bug entirely."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/controlflow.html",
    },

    # ──────────────────────────────────────────────
    # DATA STRUCTURES — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "queue-using-list",
        "topic": "data-structures",
        "difficulty": "beginner",
        "language": "python",
        "title": "Queue: Enqueue and Dequeue",
        "description": (
            "A queue is First-In First-Out (FIFO). Write a function called `solution` that takes "
            "a list of string operations and returns the front element after all operations.\n"
            "Operations:\n  'enqueue:X' — add integer X to the back\n  'dequeue' — remove the front element\n\n"
            "Example:\n  solution(['enqueue:1','enqueue:2','dequeue','enqueue:3']) → 2"
        ),
        "starter_code": "def solution(ops: list) -> int:\n    queue = []\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(['enqueue:1','enqueue:2','dequeue','enqueue:3'])", "expected_output": "2"},
            {"input": "solution(['enqueue:5'])",                                   "expected_output": "5"},
            {"input": "solution(['enqueue:1','enqueue:2','enqueue:3'])",           "expected_output": "1"},
        ],
        "hint": "Use a Python list. append() adds to the back. pop(0) removes from the front. queue[0] peeks at the front without removing.",
        "solution": (
            "def solution(ops: list) -> int:\n"
            "    queue = []\n"
            "    for op in ops:\n"
            "        if op.startswith('enqueue:'):\n"
            "            queue.append(int(op.split(':')[1]))\n"
            "        elif op == 'dequeue':\n"
            "            queue.pop(0)\n"
            "    return queue[0]"
        ),
        "concepts": [
            {
                "title": "Queue vs Stack",
                "explanation": (
                    "A stack is LIFO (last in, first out) — like a stack of plates. "
                    "A queue is FIFO (first in, first out) — like a line at a shop. "
                    "Both can be simulated with a Python list."
                ),
                "examples": [
                    "# Stack: append to end, pop from end",
                    "stack.append(x)   # push",
                    "stack.pop()       # pop last",
                    "",
                    "# Queue: append to end, pop from front",
                    "queue.append(x)   # enqueue",
                    "queue.pop(0)      # dequeue first",
                ],
                "watch_out": (
                    "list.pop(0) is O(n) because all remaining elements shift left. "
                    "For performance-critical code, use collections.deque which has O(1) popleft(). "
                    "For learning purposes, list.pop(0) is fine."
                ),
            },
            {
                "title": "collections.deque — The Proper Queue",
                "explanation": (
                    "Python's standard library has deque (double-ended queue) in the collections module. "
                    "It has O(1) append and popleft, making it ideal for queues."
                ),
                "examples": [
                    "from collections import deque",
                    "q = deque()",
                    "q.append(1)    # enqueue",
                    "q.append(2)",
                    "q.popleft()    # dequeue → 1",
                    "q[0]           # peek front → 2",
                ],
                "watch_out": (
                    "deque supports indexing (q[0]) but is not a list — "
                    "some list-specific methods like sort() are not available. "
                    "For most queue tasks, append() and popleft() are all you need."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/collections.html#collections.deque",
    },

    # ──────────────────────────────────────────────
    # DATA STRUCTURES — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "min-stack",
        "topic": "data-structures",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Min Stack",
        "description": (
            "Design a stack that supports push, pop, and get_min() in O(1) time. "
            "get_min() returns the smallest element currently in the stack.\n\n"
            "Write `solution(ops)` where ops is a list of strings:\n"
            "  'push:X' — push integer X\n"
            "  'pop' — remove the top element\n"
            "  'min' — record the current minimum\n\n"
            "Return a list of integers from each 'min' operation in order.\n\n"
            "Example:\n  solution(['push:5','push:3','min','push:1','min']) → [3, 1]"
        ),
        "starter_code": "def solution(ops: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(['push:5','push:3','min','push:1','min'])", "expected_output": "[3, 1]"},
            {"input": "solution(['push:2','push:4','min','pop','min'])",    "expected_output": "[2, 2]"},
            {"input": "solution(['push:1','min'])",                         "expected_output": "[1]"},
        ],
        "hint": "Keep a second 'min stack' alongside the main stack. Every push also pushes the new minimum onto the min stack.",
        "solution": (
            "def solution(ops: list) -> list:\n"
            "    stack = []\n"
            "    min_stack = []   # top is always the current minimum\n"
            "    results = []\n"
            "    for op in ops:\n"
            "        if op.startswith('push:'):\n"
            "            val = int(op.split(':')[1])\n"
            "            stack.append(val)\n"
            "            if not min_stack or val <= min_stack[-1]:\n"
            "                min_stack.append(val)\n"
            "            else:\n"
            "                min_stack.append(min_stack[-1])\n"
            "        elif op == 'pop':\n"
            "            stack.pop()\n"
            "            min_stack.pop()\n"
            "        elif op == 'min':\n"
            "            results.append(min_stack[-1])\n"
            "    return results"
        ),
        "concepts": [
            {
                "title": "Auxiliary Stack for O(1) Minimum",
                "explanation": (
                    "The trick is a second stack that mirrors the main stack but stores the running minimum. "
                    "Every push records 'what is the minimum so far?', so get_min() is just a peek at the top."
                ),
                "examples": [
                    "# Push 5, 3, 7:",
                    "main:    [5, 3, 7]",
                    "min_stk: [5, 3, 3]  # 7 > 3, so min is still 3",
                    "",
                    "# Pop 7:",
                    "main:    [5, 3]",
                    "min_stk: [5, 3]     # min is still 3",
                    "",
                    "# get_min → min_stk[-1] = 3",
                ],
                "watch_out": (
                    "You must pop the min_stack in sync with the main stack. "
                    "If they get out of sync, get_min() will return stale values."
                ),
            },
            {
                "title": "Running Minimum Pattern",
                "explanation": (
                    "When processing a sequence, maintain the best (min/max/sum) seen so far. "
                    "Each new element either beats the current best or the best stays the same."
                ),
                "examples": [
                    "current_min = float('inf')",
                    "for x in values:",
                    "    current_min = min(current_min, x)",
                    "",
                    "# Or inline when pushing:",
                    "new_min = min(val, min_stack[-1]) if min_stack else val",
                    "min_stack.append(new_min)",
                ],
                "watch_out": (
                    "float('inf') is a handy sentinel for 'no minimum yet'. "
                    "Any real number is smaller, so the first comparison always wins."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks",
    },

    # ──────────────────────────────────────────────
    # OOP — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "temperature-converter",
        "topic": "oop",
        "difficulty": "beginner",
        "language": "python",
        "title": "Temperature Converter Class",
        "description": (
            "Write a class called `TemperatureConverter` that:\n"
            "  - Takes a temperature in Celsius in __init__\n"
            "  - Has to_fahrenheit() → returns Celsius * 9/5 + 32, rounded to 2 decimal places\n"
            "  - Has to_kelvin() → returns Celsius + 273.15, rounded to 2 decimal places\n\n"
            "Write `solution(celsius, scale)` that creates a converter and returns the result "
            "for 'fahrenheit' or 'kelvin'.\n\n"
            "Example:\n  solution(0, 'fahrenheit') → 32.0\n  solution(0, 'kelvin') → 273.15"
        ),
        "starter_code": (
            "class TemperatureConverter:\n"
            "    def __init__(self, celsius: float):\n"
            "        pass\n\n"
            "    def to_fahrenheit(self) -> float:\n"
            "        pass\n\n"
            "    def to_kelvin(self) -> float:\n"
            "        pass\n\n\n"
            "def solution(celsius: float, scale: str) -> float:\n"
            "    pass"
        ),
        "test_cases": [
            {"input": "solution(0, 'fahrenheit')",    "expected_output": "32.0"},
            {"input": "solution(100, 'fahrenheit')",  "expected_output": "212.0"},
            {"input": "solution(0, 'kelvin')",        "expected_output": "273.15"},
            {"input": "solution(25, 'fahrenheit')",   "expected_output": "77.0"},
        ],
        "hint": "Store celsius as self.celsius in __init__. Use round(value, 2) in each conversion method.",
        "solution": (
            "class TemperatureConverter:\n"
            "    def __init__(self, celsius: float):\n"
            "        self.celsius = celsius\n\n"
            "    def to_fahrenheit(self) -> float:\n"
            "        return round(self.celsius * 9 / 5 + 32, 2)\n\n"
            "    def to_kelvin(self) -> float:\n"
            "        return round(self.celsius + 273.15, 2)\n\n\n"
            "def solution(celsius: float, scale: str) -> float:\n"
            "    t = TemperatureConverter(celsius)\n"
            "    if scale == 'fahrenheit':\n"
            "        return t.to_fahrenheit()\n"
            "    return t.to_kelvin()"
        ),
        "concepts": [
            {
                "title": "Methods as Behaviours",
                "explanation": (
                    "A method is a function that belongs to an object. "
                    "It can read and use the object's data (self.celsius) without needing parameters."
                ),
                "examples": [
                    "class TemperatureConverter:",
                    "    def __init__(self, celsius):",
                    "        self.celsius = celsius",
                    "",
                    "    def to_fahrenheit(self):",
                    "        return self.celsius * 9/5 + 32",
                    "",
                    "t = TemperatureConverter(100)",
                    "t.to_fahrenheit()  # 212.0",
                ],
                "watch_out": (
                    "The conversion formula is (C * 9/5) + 32, not (C * 9) / (5 + 32). "
                    "Python follows standard operator precedence: * and / before +. "
                    "No brackets needed, but add them if it makes the formula clearer."
                ),
            },
            {
                "title": "round(value, ndigits)",
                "explanation": (
                    "round(x, 2) rounds x to 2 decimal places. "
                    "Used here to give clean output instead of floating-point noise like 212.00000000001."
                ),
                "examples": [
                    "round(3.14159, 2)  # 3.14",
                    "round(212.0, 2)    # 212.0",
                    "round(2.675, 2)    # 2.67 — floating-point can surprise you",
                ],
                "watch_out": (
                    "Floating-point arithmetic is not exact. 0.1 + 0.2 is 0.30000000000000004. "
                    "round() hides most of this noise, but for financial calculations use the decimal module."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/classes.html",
    },

    # ──────────────────────────────────────────────
    # OOP — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "todo-list",
        "topic": "oop",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Todo List Class",
        "description": (
            "Build a `TodoList` class with:\n"
            "  - add(task: str) — add a task (default: not done)\n"
            "  - complete(task: str) — mark a task as done\n"
            "  - get_pending() — return a list of tasks that are NOT done (in insertion order)\n\n"
            "Write `solution(ops)` where ops is a list of ('add', task) or ('complete', task) tuples. "
            "Return the result of get_pending() after all operations.\n\n"
            "Example:\n"
            "  solution([('add','write tests'),('add','fix bug'),('complete','fix bug')])\n"
            "  → ['write tests']"
        ),
        "starter_code": (
            "class TodoList:\n"
            "    def __init__(self):\n"
            "        pass\n\n"
            "    def add(self, task: str):\n"
            "        pass\n\n"
            "    def complete(self, task: str):\n"
            "        pass\n\n"
            "    def get_pending(self) -> list:\n"
            "        pass\n\n\n"
            "def solution(ops: list) -> list:\n"
            "    pass"
        ),
        "test_cases": [
            {
                "input": "solution([('add','write tests'),('add','fix bug'),('complete','fix bug')])",
                "expected_output": "['write tests']",
            },
            {
                "input": "solution([('add','task1')])",
                "expected_output": "['task1']",
            },
            {
                "input": "solution([])",
                "expected_output": "[]",
            },
        ],
        "hint": "Use a dict mapping task → bool (False=pending, True=done). get_pending() filters for False values.",
        "solution": (
            "class TodoList:\n"
            "    def __init__(self):\n"
            "        self.tasks = {}   # task → done (bool)\n\n"
            "    def add(self, task: str):\n"
            "        self.tasks[task] = False\n\n"
            "    def complete(self, task: str):\n"
            "        if task in self.tasks:\n"
            "            self.tasks[task] = True\n\n"
            "    def get_pending(self) -> list:\n"
            "        return [t for t, done in self.tasks.items() if not done]\n\n\n"
            "def solution(ops: list) -> list:\n"
            "    todo = TodoList()\n"
            "    for op, *args in ops:\n"
            "        if op == 'add':\n"
            "            todo.add(args[0])\n"
            "        elif op == 'complete':\n"
            "            todo.complete(args[0])\n"
            "    return todo.get_pending()"
        ),
        "concepts": [
            {
                "title": "Dict as a State Store",
                "explanation": (
                    "A dict maps each task to its completion state. "
                    "Lookups and updates are O(1), and insertion order is preserved in Python 3.7+."
                ),
                "examples": [
                    "tasks = {}",
                    "tasks['write tests'] = False   # add",
                    "tasks['fix bug']     = False",
                    "tasks['fix bug']     = True    # complete",
                    "{t: v for t, v in tasks.items() if not v}",
                    "# → {'write tests': False}",
                ],
                "watch_out": (
                    "Calling complete() on a task that was never added should do nothing. "
                    "Always guard with 'if task in self.tasks:' before updating."
                ),
            },
            {
                "title": "Iterating a Dict with .items()",
                "explanation": (
                    "dict.items() returns (key, value) pairs. "
                    "Combine with a list comprehension to filter by value."
                ),
                "examples": [
                    "tasks = {'a': False, 'b': True, 'c': False}",
                    "[t for t, done in tasks.items() if not done]",
                    "# ['a', 'c']  — only pending tasks",
                ],
                "watch_out": (
                    "Modifying a dict while iterating over it raises a RuntimeError. "
                    "If you need to remove items during iteration, iterate over list(tasks.items()) instead."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#dictionaries",
    },

    # ──────────────────────────────────────────────
    # BEST PRACTICES — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "dict-comprehension",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "python",
        "title": "Dictionary Comprehension",
        "description": (
            "Write a function called `solution` that takes a list of words and returns "
            "a dictionary mapping each word to its length. Use a dict comprehension.\n\n"
            "Example:\n  solution(['cat', 'elephant', 'hi']) → {'cat': 3, 'elephant': 8, 'hi': 2}"
        ),
        "starter_code": "def solution(words: list) -> dict:\n    # Use a dict comprehension\n    pass",
        "test_cases": [
            {"input": "solution(['cat', 'elephant', 'hi'])", "expected_output": "{'cat': 3, 'elephant': 8, 'hi': 2}"},
            {"input": "solution(['hello'])",                  "expected_output": "{'hello': 5}"},
            {"input": "solution([])",                         "expected_output": "{}"},
        ],
        "hint": "Dict comprehension syntax: {key_expr: value_expr for item in iterable}",
        "solution": (
            "def solution(words: list) -> dict:\n"
            "    return {word: len(word) for word in words}"
        ),
        "concepts": [
            {
                "title": "Dictionary Comprehensions",
                "explanation": (
                    "A dict comprehension builds a dict in one expression: "
                    "{key: value for item in iterable}. "
                    "It is the dict equivalent of a list comprehension."
                ),
                "examples": [
                    "# Word → length:",
                    "{w: len(w) for w in ['cat', 'dog']}   # {'cat':3, 'dog':3}",
                    "",
                    "# Number → square:",
                    "{n: n**2 for n in range(4)}  # {0:0, 1:1, 2:4, 3:9}",
                    "",
                    "# With filter:",
                    "{w: len(w) for w in words if len(w) > 3}",
                ],
                "watch_out": (
                    "If the iterable has duplicate keys, later values overwrite earlier ones. "
                    "{w[0]: w for w in ['ant','ape']} → {'a': 'ape'} — 'ant' is lost."
                ),
            },
            {
                "title": "len() on Strings",
                "explanation": (
                    "len(s) returns the number of characters in string s. "
                    "It counts every character including spaces and punctuation."
                ),
                "examples": [
                    'len("hello")    # 5',
                    'len("")         # 0',
                    'len("hi there") # 8  — space counts',
                ],
                "watch_out": (
                    "len() on a list counts elements, on a string it counts characters, "
                    "on a dict it counts key-value pairs. The function is universal — "
                    "it works on any sized container."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#dictionaries",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — BEGINNER (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "caesar-cipher",
        "topic": "scripting",
        "difficulty": "beginner",
        "language": "python",
        "title": "Caesar Cipher",
        "description": (
            "Write a function called `solution` that encrypts a string using a Caesar cipher. "
            "Shift each letter forward by n positions in the alphabet, wrapping around. "
            "Preserve case. Leave non-letter characters unchanged.\n\n"
            "Example:\n  solution('abc', 3) → 'def'\n  solution('xyz', 1) → 'yza'\n  solution('Hello!', 1) → 'Ifmmp!'"
        ),
        "starter_code": "def solution(text: str, n: int) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("abc", 3)',    "expected_output": "def"},
            {"input": 'solution("xyz", 1)',    "expected_output": "yza"},
            {"input": 'solution("Hello!", 1)', "expected_output": "Ifmmp!"},
            {"input": 'solution("abc", 0)',    "expected_output": "abc"},
        ],
        "hint": "Use ord() to get a character's ASCII value and chr() to convert back. Wrap with modulo 26.",
        "solution": (
            "def solution(text: str, n: int) -> str:\n"
            "    result = []\n"
            "    for ch in text:\n"
            "        if ch.isalpha():\n"
            "            base = ord('A') if ch.isupper() else ord('a')\n"
            "            shifted = (ord(ch) - base + n) % 26 + base\n"
            "            result.append(chr(shifted))\n"
            "        else:\n"
            "            result.append(ch)\n"
            "    return ''.join(result)"
        ),
        "concepts": [
            {
                "title": "ord() and chr() — Characters and ASCII",
                "explanation": (
                    "ord(ch) returns the ASCII integer for a character. "
                    "chr(n) converts an integer back to a character. "
                    "Together they let you do arithmetic on letters."
                ),
                "examples": [
                    'ord("a")   # 97',
                    'ord("z")   # 122',
                    'ord("A")   # 65',
                    'chr(98)    # "b"',
                    'chr(ord("a") + 1)  # "b"',
                ],
                "watch_out": (
                    "Uppercase 'A'=65 and lowercase 'a'=97 have different base values. "
                    "Always subtract the right base (ord('A') or ord('a')) before arithmetic."
                ),
            },
            {
                "title": "Modulo for Wrap-Around  % 26",
                "explanation": (
                    "The alphabet has 26 letters. After 'z' (or 'Z') you wrap back to 'a' (or 'A'). "
                    "Modulo keeps the shifted value in range 0..25."
                ),
                "examples": [
                    "# Shift 'x' (index 23) by 4:",
                    "(23 + 4) % 26  # 1  → 'b'",
                    "",
                    "# Shift 'z' (index 25) by 1:",
                    "(25 + 1) % 26  # 0  → 'a'",
                ],
                "watch_out": (
                    "Do the modulo on the offset (0..25 range), then add the base back. "
                    "The formula is: (ord(ch) - base + n) % 26 + base."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#ord",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "csv-row-parser",
        "topic": "scripting",
        "difficulty": "intermediate",
        "language": "python",
        "title": "CSV Row Parser",
        "description": (
            "Write a function called `solution` that takes a CSV string (multiple lines) "
            "and returns a list of dicts, where each dict maps column names to values. "
            "The first line is the header.\n\n"
            "Example:\n"
            "  Input: 'name,age\\nAlice,30\\nBob,25'\n"
            "  Output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]"
        ),
        "starter_code": "def solution(csv_text: str) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": 'solution("name,age\\nAlice,30\\nBob,25")',
                "expected_output": "[{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]",
            },
            {
                "input": 'solution("x,y\\n1,2")',
                "expected_output": "[{'x': '1', 'y': '2'}]",
            },
        ],
        "hint": "Split on newlines to get rows. The first row gives the headers. Use zip(headers, values) to pair them up.",
        "solution": (
            "def solution(csv_text: str) -> list:\n"
            "    lines = csv_text.strip().split('\\n')\n"
            "    headers = lines[0].split(',')\n"
            "    result = []\n"
            "    for line in lines[1:]:\n"
            "        values = line.split(',')\n"
            "        result.append(dict(zip(headers, values)))\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "zip() — Pairing Two Sequences",
                "explanation": (
                    "zip() takes two (or more) iterables and pairs up their elements. "
                    "It stops at the shortest one."
                ),
                "examples": [
                    "keys   = ['name', 'age']",
                    "values = ['Alice', '30']",
                    "list(zip(keys, values))    # [('name','Alice'), ('age','30')]",
                    "dict(zip(keys, values))    # {'name':'Alice', 'age':'30'}",
                ],
                "watch_out": (
                    "zip() returns a lazy iterator — wrap with list() or dict() to materialise it. "
                    "If the sequences have different lengths, extra elements are silently dropped."
                ),
            },
            {
                "title": "str.strip() — Removing Whitespace",
                "explanation": (
                    "strip() removes leading and trailing whitespace (spaces, newlines, tabs). "
                    "Always strip CSV/file content before splitting to avoid empty ghost rows."
                ),
                "examples": [
                    '"  hello\\n".strip()   # "hello"',
                    '"\\ndata\\n".strip()   # "data"',
                    '"hello".strip()      # "hello" — no change',
                ],
                "watch_out": (
                    "strip() only removes from the edges, not the middle. "
                    "'hello  world'.strip() → 'hello  world' (internal spaces unchanged)."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#zip",
    },

    {
        "id": "log-parser",
        "topic": "scripting",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Log File Parser",
        "description": (
            "Write a function called `solution` that takes a multi-line log string and returns "
            "a dict counting occurrences of each log level: ERROR, WARNING, and INFO. "
            "Each line follows the format: '2024-01-01 LEVEL message'.\n\n"
            "Example:\n"
            "  Input: '2024-01-01 ERROR disk full\\n2024-01-01 INFO started\\n2024-01-01 ERROR crash'\n"
            "  Output: {'ERROR': 2, 'WARNING': 0, 'INFO': 1}"
        ),
        "starter_code": "def solution(log_text: str) -> dict:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": 'solution("2024-01-01 ERROR disk full\\n2024-01-01 INFO started\\n2024-01-01 ERROR crash")',
                "expected_output": "{'ERROR': 2, 'WARNING': 0, 'INFO': 1}",
            },
            {
                "input": 'solution("2024-01-01 WARNING low memory")',
                "expected_output": "{'ERROR': 0, 'WARNING': 1, 'INFO': 0}",
            },
            {
                "input": 'solution("")',
                "expected_output": "{'ERROR': 0, 'WARNING': 0, 'INFO': 0}",
            },
        ],
        "hint": "Split the log on newlines. For each non-empty line, split on spaces and check the second word (the level). Initialise all three counts to 0 first.",
        "solution": (
            "def solution(log_text: str) -> dict:\n"
            "    counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}\n"
            "    for line in log_text.strip().splitlines():\n"
            "        if not line:\n"
            "            continue\n"
            "        parts = line.split()\n"
            "        if len(parts) >= 2 and parts[1] in counts:\n"
            "            counts[parts[1]] += 1\n"
            "    return counts"
        ),
        "concepts": [
            {
                "title": "str.splitlines() vs split('\\n')",
                "explanation": (
                    "splitlines() splits on all line endings (\\n, \\r\\n, \\r) and never produces "
                    "a trailing empty string. split('\\n') is simpler but can leave an empty string "
                    "at the end if the text ends with a newline."
                ),
                "examples": [
                    '"a\\nb\\n".split("\\n")    # ["a", "b", ""]  — trailing empty string',
                    '"a\\nb\\n".splitlines()  # ["a", "b"]      — clean',
                    '"a\\r\\nb".splitlines()  # ["a", "b"]      — handles Windows line endings',
                ],
                "watch_out": (
                    "Always strip() or use splitlines() when parsing file content — "
                    "trailing newlines create ghost empty lines that crash your parsing logic."
                ),
            },
            {
                "title": "Initialising Counts to Zero",
                "explanation": (
                    "Pre-populate the result dict with all expected keys set to 0. "
                    "This guarantees every key is present in the output, even if the log has no entries of that level."
                ),
                "examples": [
                    "counts = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}",
                    "# Now safe to do:",
                    "counts['ERROR'] += 1   # no KeyError",
                    "",
                    "# Without pre-init you would need:",
                    "counts['ERROR'] = counts.get('ERROR', 0) + 1",
                ],
                "watch_out": (
                    "The insertion order of the pre-populated dict determines the print order. "
                    "Python 3.7+ preserves insertion order, so {'ERROR':0,'WARNING':0,'INFO':0} "
                    "will always print in that order."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.splitlines",
    },

    # ──────────────────────────────────────────────
    # PYTHON — ADVANCED / COVERAGE EXPANSION
    # ──────────────────────────────────────────────

    {
        "id": "longest-unique-substring",
        "topic": "arrays-strings",
        "difficulty": "advanced",
        "language": "python",
        "title": "Longest Unique Substring",
        "description": (
            "Write a function called `solution` that takes a string and returns the length "
            "of the longest substring with no repeated characters.\n\n"
            "Example:\n  solution('abcabcbb') -> 3  ('abc')\n  solution('bbbbb') -> 1"
        ),
        "starter_code": "def solution(text: str) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("abcabcbb")', "expected_output": "3"},
            {"input": 'solution("bbbbb")', "expected_output": "1"},
            {"input": 'solution("pwwkew")', "expected_output": "3"},
            {"input": 'solution("")', "expected_output": "0"},
        ],
        "hint": "Use a sliding window with a left pointer and a dict mapping each character to its latest index.",
        "solution": (
            "def solution(text: str) -> int:\n"
            "    seen = {}\n"
            "    left = 0\n"
            "    best = 0\n"
            "    for right, char in enumerate(text):\n"
            "        if char in seen and seen[char] >= left:\n"
            "            left = seen[char] + 1\n"
            "        seen[char] = right\n"
            "        best = max(best, right - left + 1)\n"
            "    return best"
        ),
        "concepts": [
            {
                "title": "Sliding Window",
                "explanation": "A sliding window tracks a valid range with left and right pointers instead of rebuilding substrings repeatedly.",
                "examples": [
                    "left = 0",
                    "for right, char in enumerate(text):",
                    "    best = max(best, right - left + 1)",
                ],
                "watch_out": "Only move the left pointer forward. Moving it backward can make an invalid window look valid again.",
            },
            {
                "title": "Last-Seen Index Map",
                "explanation": "A dict can remember the most recent index where each character appeared.",
                "examples": [
                    "seen[char] = right",
                    "if char in seen and seen[char] >= left:",
                ],
                "watch_out": "A repeated character before the current window should not shrink the current window.",
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#dictionaries",
    },

    {
        "id": "lru-cache-simulation",
        "topic": "data-structures",
        "difficulty": "advanced",
        "language": "python",
        "title": "LRU Cache Simulation",
        "description": (
            "Write a function called `solution` that simulates a small least-recently-used cache. "
            "It receives a capacity and a list of operations. Each operation is either "
            "('put', key, value) or ('get', key). Return a list of values returned by get operations, "
            "using -1 when the key is missing."
        ),
        "starter_code": "def solution(capacity: int, operations: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": "solution(2, [('put','a',1), ('put','b',2), ('get','a'), ('put','c',3), ('get','b'), ('get','c')])",
                "expected_output": "[1, -1, 3]",
            },
            {
                "input": "solution(1, [('put','x',10), ('put','y',20), ('get','x'), ('get','y')])",
                "expected_output": "[-1, 20]",
            },
            {
                "input": "solution(2, [('get','missing')])",
                "expected_output": "[-1]",
            },
        ],
        "hint": "Python dicts preserve insertion order. Move a key to the end whenever it is used, and evict the oldest key when the cache is too large.",
        "solution": (
            "def solution(capacity: int, operations: list) -> list:\n"
            "    cache = {}\n"
            "    results = []\n"
            "    for op in operations:\n"
            "        if op[0] == 'get':\n"
            "            key = op[1]\n"
            "            if key not in cache:\n"
            "                results.append(-1)\n"
            "            else:\n"
            "                value = cache.pop(key)\n"
            "                cache[key] = value\n"
            "                results.append(value)\n"
            "        else:\n"
            "            _, key, value = op\n"
            "            if key in cache:\n"
            "                cache.pop(key)\n"
            "            cache[key] = value\n"
            "            if len(cache) > capacity:\n"
            "                oldest = next(iter(cache))\n"
            "                cache.pop(oldest)\n"
            "    return results"
        ),
        "concepts": [
            {
                "title": "Insertion-Ordered Dictionaries",
                "explanation": "Modern Python dicts preserve insertion order, which can be used to model oldest-to-newest ordering.",
                "examples": [
                    "cache.pop(key)",
                    "cache[key] = value  # reinsert at the end",
                ],
                "watch_out": "Updating an existing key does not automatically move it to the end; pop and reinsert it.",
            },
            {
                "title": "Evicting the Oldest Item",
                "explanation": "next(iter(cache)) reads the first key in insertion order.",
                "examples": [
                    "oldest = next(iter(cache))",
                    "cache.pop(oldest)",
                ],
                "watch_out": "Only call next(iter(cache)) when the cache is non-empty.",
            },
        ],
        "docs_url": "https://docs.python.org/3/library/collections.html#ordereddict-objects",
    },

    {
        "id": "plugin-registry",
        "topic": "oop",
        "difficulty": "advanced",
        "language": "python",
        "title": "Plugin Registry",
        "description": (
            "Create a small plugin system. Define `UppercasePlugin` and `ReversePlugin`, each with "
            "a `run(text)` method. Then write `solution(plugin_names, text)` that applies the named "
            "plugins in order and returns the final text. Supported names are 'upper' and 'reverse'."
        ),
        "starter_code": (
            "class UppercasePlugin:\n"
            "    pass\n\n"
            "class ReversePlugin:\n"
            "    pass\n\n"
            "def solution(plugin_names: list, text: str) -> str:\n"
            "    # Your code here\n"
            "    pass"
        ),
        "test_cases": [
            {"input": "solution(['upper'], 'hello')", "expected_output": "HELLO"},
            {"input": "solution(['reverse'], 'hello')", "expected_output": "olleh"},
            {"input": "solution(['upper', 'reverse'], 'hello')", "expected_output": "OLLEH"},
            {"input": "solution([], 'CodeCraft')", "expected_output": "CodeCraft"},
        ],
        "hint": "Create a dictionary that maps plugin names to plugin instances, then loop through the requested names and call run().",
        "solution": (
            "class UppercasePlugin:\n"
            "    def run(self, text: str) -> str:\n"
            "        return text.upper()\n\n"
            "class ReversePlugin:\n"
            "    def run(self, text: str) -> str:\n"
            "        return text[::-1]\n\n"
            "def solution(plugin_names: list, text: str) -> str:\n"
            "    registry = {\n"
            "        'upper': UppercasePlugin(),\n"
            "        'reverse': ReversePlugin(),\n"
            "    }\n"
            "    result = text\n"
            "    for name in plugin_names:\n"
            "        result = registry[name].run(result)\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "Polymorphic Methods",
                "explanation": "Different classes can expose the same method name, letting the caller use them through a shared interface.",
                "examples": [
                    "plugin.run(text)",
                    "UppercasePlugin().run('hi')",
                    "ReversePlugin().run('hi')",
                ],
                "watch_out": "Every plugin must implement the same method name. If one class misses run(), the caller will crash.",
            },
            {
                "title": "Registry Pattern",
                "explanation": "A registry maps names to objects so code can choose behavior dynamically without a long if/elif chain.",
                "examples": [
                    "registry = {'upper': UppercasePlugin()}",
                    "registry[name].run(text)",
                ],
                "watch_out": "If user input can contain unknown names, validate before indexing into the registry.",
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/classes.html",
    },

    {
        "id": "normalize-user-records",
        "topic": "best-practices",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Normalize User Records",
        "description": (
            "Write a function called `solution` that takes a list of user dictionaries and returns "
            "a cleaned list. Each output user should have lowercase, trimmed email and title-cased, "
            "trimmed name. Skip users missing either name or email."
        ),
        "starter_code": "def solution(users: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": "solution([{'name':' alice ', 'email':' ALICE@EXAMPLE.COM '}, {'name':'', 'email':'x@y.com'}])",
                "expected_output": "[{'name': 'Alice', 'email': 'alice@example.com'}]",
            },
            {
                "input": "solution([{'name':'bob stone', 'email':'Bob@Site.io'}])",
                "expected_output": "[{'name': 'Bob Stone', 'email': 'bob@site.io'}]",
            },
            {
                "input": "solution([{'name':'No Email'}, {'email':'missing@name.com'}])",
                "expected_output": "[]",
            },
        ],
        "hint": "Use small helper functions or clear local variables so validation and transformation stay easy to read.",
        "solution": (
            "def solution(users: list) -> list:\n"
            "    cleaned = []\n"
            "    for user in users:\n"
            "        name = user.get('name', '').strip()\n"
            "        email = user.get('email', '').strip()\n"
            "        if not name or not email:\n"
            "            continue\n"
            "        cleaned.append({\n"
            "            'name': name.title(),\n"
            "            'email': email.lower(),\n"
            "        })\n"
            "    return cleaned"
        ),
        "concepts": [
            {
                "title": "Data Normalisation",
                "explanation": "Normalisation turns messy input into a consistent shape before the rest of the program uses it.",
                "examples": [
                    "name = name.strip().title()",
                    "email = email.strip().lower()",
                ],
                "watch_out": "Normalise after checking for missing values so empty strings do not become misleading data.",
            },
            {
                "title": "Guarding Bad Records",
                "explanation": "A simple continue can skip invalid input and keep the main transformation path readable.",
                "examples": [
                    "if not name or not email:",
                    "    continue",
                ],
                "watch_out": "user['email'] raises KeyError when a key is missing. user.get('email', '') is safer for messy records.",
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#string-methods",
    },

    {
        "id": "validate-config",
        "topic": "best-practices",
        "difficulty": "advanced",
        "language": "python",
        "title": "Validate Config",
        "description": (
            "Write a function called `solution` that validates a config dictionary and returns a list "
            "of error messages. Required keys are host, port, and debug. host must be a non-empty string, "
            "port must be an int from 1 to 65535, and debug must be a boolean."
        ),
        "starter_code": "def solution(config: dict) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution({'host':'localhost', 'port':8000, 'debug':False})", "expected_output": "[]"},
            {"input": "solution({'host':'', 'port':70000, 'debug':'no'})", "expected_output": "['host must be a non-empty string', 'port must be between 1 and 65535', 'debug must be a boolean']"},
            {"input": "solution({'port':3000})", "expected_output": "['host is required', 'debug is required']"},
        ],
        "hint": "Validate one rule at a time and append clear error messages in a predictable order.",
        "solution": (
            "def solution(config: dict) -> list:\n"
            "    errors = []\n"
            "    if 'host' not in config:\n"
            "        errors.append('host is required')\n"
            "    elif not isinstance(config['host'], str) or not config['host'].strip():\n"
            "        errors.append('host must be a non-empty string')\n\n"
            "    if 'port' not in config:\n"
            "        errors.append('port is required')\n"
            "    elif not isinstance(config['port'], int) or not 1 <= config['port'] <= 65535:\n"
            "        errors.append('port must be between 1 and 65535')\n\n"
            "    if 'debug' not in config:\n"
            "        errors.append('debug is required')\n"
            "    elif not isinstance(config['debug'], bool):\n"
            "        errors.append('debug must be a boolean')\n\n"
            "    return errors"
        ),
        "concepts": [
            {
                "title": "Predictable Validation Order",
                "explanation": "Returning errors in a consistent order makes tests, logs, and user feedback easier to reason about.",
                "examples": [
                    "validate host",
                    "validate port",
                    "validate debug",
                ],
                "watch_out": "A set would remove duplicates but also make ordering less obvious. A list is better for ordered errors.",
            },
            {
                "title": "isinstance() for Type Checks",
                "explanation": "isinstance(value, type) checks whether a value has the expected type before using it.",
                "examples": [
                    "isinstance(config['port'], int)",
                    "isinstance(config['debug'], bool)",
                ],
                "watch_out": "In Python, bool is a subclass of int. For this exercise that only matters if you accept booleans as ports; stricter validation may need type(value) is int.",
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#isinstance",
    },

    {
        "id": "ini-section-parser",
        "topic": "scripting",
        "difficulty": "advanced",
        "language": "python",
        "title": "INI Section Parser",
        "description": (
            "Write a function called `solution` that parses a small INI-style config string. "
            "Section headers look like [database]. Key-value lines look like host=localhost. "
            "Return a nested dict of sections to key-value pairs. Ignore blank lines and lines starting with #."
        ),
        "starter_code": "def solution(config_text: str) -> dict:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": 'solution("[database]\\nhost=localhost\\nport=5432\\n\\n[app]\\ndebug=true")',
                "expected_output": "{'database': {'host': 'localhost', 'port': '5432'}, 'app': {'debug': 'true'}}",
            },
            {
                "input": 'solution("# comment\\n[server]\\nname=api\\nregion=eu")',
                "expected_output": "{'server': {'name': 'api', 'region': 'eu'}}",
            },
            {"input": 'solution("")', "expected_output": "{}"},
        ],
        "hint": "Track the current section as you read each line. When you see a key=value line, store it under that section.",
        "solution": (
            "def solution(config_text: str) -> dict:\n"
            "    result = {}\n"
            "    current = None\n"
            "    for raw_line in config_text.splitlines():\n"
            "        line = raw_line.strip()\n"
            "        if not line or line.startswith('#'):\n"
            "            continue\n"
            "        if line.startswith('[') and line.endswith(']'):\n"
            "            current = line[1:-1]\n"
            "            result[current] = {}\n"
            "        elif current is not None and '=' in line:\n"
            "            key, value = line.split('=', 1)\n"
            "            result[current][key.strip()] = value.strip()\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "Stateful Parsing",
                "explanation": "Some parsers need to remember context, such as which section later key-value lines belong to.",
                "examples": [
                    "current = None",
                    "current = line[1:-1]",
                    "result[current][key] = value",
                ],
                "watch_out": "Do not store key-value lines before a section exists unless the format says global keys are allowed.",
            },
            {
                "title": "Splitting Once",
                "explanation": "split('=', 1) splits only at the first equals sign, preserving any later equals signs in the value.",
                "examples": [
                    "'a=b=c'.split('=', 1)  # ['a', 'b=c']",
                ],
                "watch_out": "Using split('=') with no limit can create too many pieces for values that contain equals signs.",
            },
        ],
        "docs_url": "https://docs.python.org/3/library/configparser.html",
    },

    # ──────────────────────────────────────────────
    # JAVASCRIPT — BEGINNER
    # ──────────────────────────────────────────────

    {
        "id": "js-count-vowels",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "javascript",
        "title": "Count Vowels in JavaScript",
        "description": (
            "Write a function called `solution` that takes a string and returns the number "
            "of vowels it contains. Count a, e, i, o, and u, and ignore case.\n\n"
            "Example:\n  solution('hello') → 2\n  solution('JAVASCRIPT') → 3"
        ),
        "starter_code": "function solution(text) {\n  // Your code here\n  return 0;\n}",
        "test_cases": [
            {"input": 'solution("hello")', "expected_output": "2"},
            {"input": 'solution("JAVASCRIPT")', "expected_output": "3"},
            {"input": 'solution("rhythm")', "expected_output": "0"},
            {"input": 'solution("AEIOU")', "expected_output": "5"},
        ],
        "hint": "Convert the string to lowercase, then loop through each character and check whether it is in 'aeiou'.",
        "solution": (
            "function solution(text) {\n"
            "  const vowels = 'aeiou';\n"
            "  let count = 0;\n"
            "  for (const char of text.toLowerCase()) {\n"
            "    if (vowels.includes(char)) count++;\n"
            "  }\n"
            "  return count;\n"
            "}"
        ),
        "concepts": [
            {
                "title": "for...of Loops",
                "explanation": "A for...of loop reads each value from an iterable, such as each character in a string.",
                "examples": [
                    "for (const char of 'hello') {",
                    "  console.log(char);",
                    "}",
                ],
                "watch_out": "for...of gives you the character. for...in gives you the index keys, which is usually not what you want here.",
            },
            {
                "title": "String includes()",
                "explanation": "includes() checks whether a string contains another string and returns true or false.",
                "examples": [
                    "'aeiou'.includes('e') // true",
                    "'aeiou'.includes('z') // false",
                ],
                "watch_out": "includes() is case-sensitive, so convert input to lowercase first if the comparison should ignore case.",
            },
        ],
        "docs_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of",
    },

    {
        "id": "js-fizzbuzz",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "javascript",
        "title": "FizzBuzz in JavaScript",
        "description": (
            "Write a function called `solution` that takes a number and returns:\n"
            "  'Fizz' if it is divisible by 3\n"
            "  'Buzz' if it is divisible by 5\n"
            "  'FizzBuzz' if it is divisible by both\n"
            "  the number as a string otherwise"
        ),
        "starter_code": "function solution(n) {\n  // Your code here\n  return '';\n}",
        "test_cases": [
            {"input": "solution(15)", "expected_output": "FizzBuzz"},
            {"input": "solution(3)", "expected_output": "Fizz"},
            {"input": "solution(5)", "expected_output": "Buzz"},
            {"input": "solution(7)", "expected_output": "7"},
        ],
        "hint": "Check divisibility by both 3 and 5 before checking the individual cases.",
        "solution": (
            "function solution(n) {\n"
            "  if (n % 3 === 0 && n % 5 === 0) return 'FizzBuzz';\n"
            "  if (n % 3 === 0) return 'Fizz';\n"
            "  if (n % 5 === 0) return 'Buzz';\n"
            "  return String(n);\n"
            "}"
        ),
        "concepts": [
            {
                "title": "Modulo Operator",
                "explanation": "The % operator returns the remainder after division. A remainder of 0 means a number is divisible.",
                "examples": [
                    "15 % 5 // 0",
                    "7 % 3  // 1",
                ],
                "watch_out": "Check the combined FizzBuzz case first. If you return Fizz for 15, you never reach FizzBuzz.",
            },
            {
                "title": "String() Conversion",
                "explanation": "String(value) converts numbers, booleans, and other values into strings.",
                "examples": [
                    "String(7) // '7'",
                    "String(true) // 'true'",
                ],
                "watch_out": "Returning the number 7 is not the same as returning the string '7'.",
            },
        ],
        "docs_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder",
    },

    {
        "id": "js-sum-positive-numbers",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "javascript",
        "title": "Sum Positive Numbers",
        "description": (
            "Write a function called `solution` that takes an array of numbers and returns "
            "the sum of only the positive numbers.\n\n"
            "Example:\n  solution([1, -2, 3, 4]) → 8"
        ),
        "starter_code": "function solution(nums) {\n  // Your code here\n  return 0;\n}",
        "test_cases": [
            {"input": "solution([1, -2, 3, 4])", "expected_output": "8"},
            {"input": "solution([-1, -2, -3])", "expected_output": "0"},
            {"input": "solution([5, 0, 10])", "expected_output": "15"},
            {"input": "solution([])", "expected_output": "0"},
        ],
        "hint": "Start with total = 0. Loop over the array and add a number only if it is greater than 0.",
        "solution": (
            "function solution(nums) {\n"
            "  let total = 0;\n"
            "  for (const num of nums) {\n"
            "    if (num > 0) total += num;\n"
            "  }\n"
            "  return total;\n"
            "}"
        ),
        "concepts": [
            {
                "title": "Accumulating a Total",
                "explanation": "A common loop pattern is to start a total at 0, then add matching values as you iterate.",
                "examples": [
                    "let total = 0;",
                    "total += 5; // total is now 5",
                ],
                "watch_out": "Use let for a value that changes. const total = 0 cannot be reassigned.",
            },
            {
                "title": "Array Iteration",
                "explanation": "for...of works well when you need each value in an array and do not need the index.",
                "examples": [
                    "for (const num of [1, 2, 3]) {",
                    "  console.log(num);",
                    "}",
                ],
                "watch_out": "Do not add negative numbers if the requirement is positive numbers only.",
            },
        ],
        "docs_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of",
    },

    # ──────────────────────────────────────────────
    # TYPESCRIPT — BEGINNER / INTERMEDIATE
    # ──────────────────────────────────────────────

    {
        "id": "ts-is-palindrome",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "typescript",
        "title": "Palindrome Check in TypeScript",
        "description": (
            "Write a function called `solution` that takes a string and returns true if it reads "
            "the same forwards and backwards. Ignore spaces and case.\n\n"
            "Example:\n  solution('Race car') → true\n  solution('hello') → false"
        ),
        "starter_code": "function solution(text: string): boolean {\n  // Your code here\n  return false;\n}",
        "test_cases": [
            {"input": 'solution("Race car")', "expected_output": "true"},
            {"input": 'solution("A man a plan a canal Panama")', "expected_output": "true"},
            {"input": 'solution("hello")', "expected_output": "false"},
            {"input": 'solution("")', "expected_output": "true"},
        ],
        "hint": "Clean the string first by lowercasing it and removing spaces. Then compare it to its reverse.",
        "solution": (
            "function solution(text: string): boolean {\n"
            "  const cleaned = text.toLowerCase().replaceAll(' ', '');\n"
            "  const reversed = cleaned.split('').reverse().join('');\n"
            "  return cleaned === reversed;\n"
            "}"
        ),
        "concepts": [
            {
                "title": "Type Annotations",
                "explanation": "TypeScript lets you declare parameter and return types so function contracts are clear.",
                "examples": [
                    "function solution(text: string): boolean {",
                    "  return text.length === 0;",
                    "}",
                ],
                "watch_out": "The return type is boolean, so return true or false, not the strings 'true' or 'false'.",
            },
            {
                "title": "Reversing a String",
                "explanation": "Strings do not have reverse(), but arrays do. Split into characters, reverse, then join.",
                "examples": [
                    "'abc'.split('').reverse().join('') // 'cba'",
                ],
                "watch_out": "reverse() mutates arrays. In this pattern the array is temporary, so that is fine.",
            },
        ],
        "docs_url": "https://www.typescriptlang.org/docs/handbook/2/everyday-types.html",
    },

    {
        "id": "ts-find-longest-word",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "typescript",
        "title": "Find the Longest Word",
        "description": (
            "Write a function called `solution` that takes a sentence and returns the longest word. "
            "If there is a tie, return the first longest word.\n\n"
            "Example:\n  solution('the quick brown fox') → 'quick'"
        ),
        "starter_code": "function solution(sentence: string): string {\n  // Your code here\n  return '';\n}",
        "test_cases": [
            {"input": 'solution("the quick brown fox")', "expected_output": "quick"},
            {"input": 'solution("a tiny elephant")', "expected_output": "elephant"},
            {"input": 'solution("same size")', "expected_output": "same"},
            {"input": 'solution("typescript")', "expected_output": "typescript"},
        ],
        "hint": "Split the sentence into words, keep track of the best word so far, and update it when a longer word appears.",
        "solution": (
            "function solution(sentence: string): string {\n"
            "  const words = sentence.split(' ');\n"
            "  let longest = words[0] ?? '';\n"
            "  for (const word of words) {\n"
            "    if (word.length > longest.length) longest = word;\n"
            "  }\n"
            "  return longest;\n"
            "}"
        ),
        "concepts": [
            {
                "title": "Tracking the Best Value",
                "explanation": "Seed a variable with the first candidate, then replace it only when you find a better one.",
                "examples": [
                    "let longest = words[0];",
                    "if (word.length > longest.length) longest = word;",
                ],
                "watch_out": "Use > instead of >= if ties should keep the first longest word.",
            },
            {
                "title": "Nullish Coalescing",
                "explanation": "The ?? operator provides a fallback only when the left side is null or undefined.",
                "examples": [
                    "const first = words[0] ?? '';",
                ],
                "watch_out": "This protects against empty arrays without replacing valid empty strings elsewhere.",
            },
        ],
        "docs_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing",
    },

    {
        "id": "ts-grade-calculator",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "typescript",
        "title": "Grade Calculator",
        "description": (
            "Write a function called `solution` that takes a numeric score and returns a letter grade:\n"
            "  'A' for 90 and above\n"
            "  'B' for 80-89\n"
            "  'C' for 70-79\n"
            "  'D' for 60-69\n"
            "  'F' otherwise"
        ),
        "starter_code": "function solution(score: number): string {\n  // Your code here\n  return '';\n}",
        "test_cases": [
            {"input": "solution(95)", "expected_output": "A"},
            {"input": "solution(82)", "expected_output": "B"},
            {"input": "solution(71)", "expected_output": "C"},
            {"input": "solution(40)", "expected_output": "F"},
        ],
        "hint": "Use guard clauses from highest score to lowest. Once a condition matches, return immediately.",
        "solution": (
            "function solution(score: number): string {\n"
            "  if (score >= 90) return 'A';\n"
            "  if (score >= 80) return 'B';\n"
            "  if (score >= 70) return 'C';\n"
            "  if (score >= 60) return 'D';\n"
            "  return 'F';\n"
            "}"
        ),
        "concepts": [
            {
                "title": "Guard Clauses",
                "explanation": "A guard clause checks a condition and returns immediately, keeping the rest of the function flat.",
                "examples": [
                    "if (score >= 90) return 'A';",
                    "return 'F';",
                ],
                "watch_out": "Order matters. Check 90 before 80, otherwise every A score would return B.",
            },
            {
                "title": "number and string Types",
                "explanation": "TypeScript can state that score must be a number and the result must be a string.",
                "examples": [
                    "function solution(score: number): string {",
                    "  return 'A';",
                    "}",
                ],
                "watch_out": "Returning a number like 90 would violate the declared string return type.",
            },
        ],
        "docs_url": "https://www.typescriptlang.org/docs/handbook/2/functions.html",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — BEGINNER (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "longest-word",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Longest Word in a Sentence",
        "description": (
            "Write a function called `solution` that takes a sentence string and returns "
            "the longest word. If there is a tie, return the first longest word.\n\n"
            "Example:\n  solution('the quick brown fox') → 'quick'\n  solution('I love Python') → 'Python'"
        ),
        "starter_code": "def solution(sentence: str) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("the quick brown fox")', "expected_output": "quick"},
            {"input": 'solution("I love Python")',       "expected_output": "Python"},
            {"input": 'solution("hello")',               "expected_output": "hello"},
            {"input": 'solution("a bb ccc")',            "expected_output": "ccc"},
        ],
        "hint": "Split into words and use max() with len as the key function.",
        "solution": (
            "def solution(sentence: str) -> str:\n"
            "    return max(sentence.split(), key=len)"
        ),
        "concepts": [
            {
                "title": "max() with a key Function",
                "explanation": (
                    "max() finds the largest item in an iterable. "
                    "The key parameter lets you specify what to measure. "
                    "max(words, key=len) finds the word with the greatest length."
                ),
                "examples": [
                    'words = ["cat", "elephant", "ox"]',
                    'max(words)           # "ox" — alphabetically last',
                    'max(words, key=len)  # "elephant" — longest',
                    'min(words, key=len)  # "ox" — shortest',
                ],
                "watch_out": (
                    "max() with a tie returns the FIRST maximum it encounters. "
                    "If two words have the same length, the one that appears first in the list wins — "
                    "which is exactly what the problem requires."
                ),
            },
            {
                "title": "Passing Functions as Arguments",
                "explanation": (
                    "In Python, functions are objects — you can pass them around like values. "
                    "key=len passes the len function itself (not the result of calling it). "
                    "max() will call len(word) on each word internally."
                ),
                "examples": [
                    'max(["a","bb"], key=len)    # "bb"',
                    'sorted(["a","bb"], key=len) # ["a", "bb"]',
                    "",
                    "# key can be any callable — lambda or named function:",
                    "max(nums, key=lambda x: abs(x))  # largest absolute value",
                ],
                "watch_out": (
                    "key=len is correct. key=len() would call len with no arguments and raise a TypeError. "
                    "Pass the function reference, not its result."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#max",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — INTERMEDIATE (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "missing-number",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Find the Missing Number",
        "description": (
            "You are given a list of n-1 distinct integers drawn from 1 to n. "
            "Exactly one number is missing. Write a function called `solution` that finds it.\n\n"
            "Do not sort the list.\n\n"
            "Example:\n  solution([1, 2, 4, 5]) → 3   (n=5, missing 3)"
        ),
        "starter_code": "def solution(nums: list) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 4, 5])", "expected_output": "3"},
            {"input": "solution([2, 3, 4, 5])", "expected_output": "1"},
            {"input": "solution([1, 2, 3, 4])", "expected_output": "5"},
            {"input": "solution([2])",           "expected_output": "1"},
        ],
        "hint": "The sum of 1..n is n*(n+1)//2. Subtract the actual sum of the list to find the gap.",
        "solution": (
            "def solution(nums: list) -> int:\n"
            "    n = len(nums) + 1\n"
            "    expected = n * (n + 1) // 2\n"
            "    return expected - sum(nums)"
        ),
        "concepts": [
            {
                "title": "Gauss's Sum Formula  n*(n+1)//2",
                "explanation": (
                    "The sum of integers 1 through n equals n*(n+1)/2. "
                    "This lets you compute the expected total instantly without a loop."
                ),
                "examples": [
                    "# Sum of 1..5 = 1+2+3+4+5 = 15",
                    "5 * (5 + 1) // 2   # 15",
                    "# Sum of 1..100 = 5050",
                    "100 * 101 // 2     # 5050",
                ],
                "watch_out": (
                    "Use integer division // (not /) so you get an int, not a float. "
                    "n*(n+1) is always even, so the result is always a whole number."
                ),
            },
            {
                "title": "sum() — Summing an Iterable",
                "explanation": (
                    "sum(iterable) adds all elements together. "
                    "Combined with Gauss's formula: expected - actual = the missing number."
                ),
                "examples": [
                    "sum([1, 2, 4, 5])   # 12",
                    "# expected for n=5: 15",
                    "# missing: 15 - 12 = 3",
                ],
                "watch_out": (
                    "sum() starts from 0 by default. You can change the start: sum(nums, 10) begins at 10. "
                    "For this problem the default of 0 is correct."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#sum",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — ADVANCED (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "group-anagrams",
        "topic": "arrays-strings",
        "difficulty": "advanced",
        "language": "python",
        "title": "Group Anagrams",
        "description": (
            "Write a function called `solution` that takes a list of words and groups "
            "anagrams together. Return a list of groups. Each group preserves the original "
            "word order. Groups appear in order of first occurrence.\n\n"
            "Example:\n  solution(['eat','tea','tan','ate','nat','bat'])\n"
            "  → [['eat','tea','ate'], ['tan','nat'], ['bat']]"
        ),
        "starter_code": "def solution(words: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": "solution(['eat','tea','tan','ate','nat','bat'])",
                "expected_output": "[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]",
            },
            {
                "input": "solution(['abc','bca','xyz'])",
                "expected_output": "[['abc', 'bca'], ['xyz']]",
            },
            {
                "input": "solution(['a'])",
                "expected_output": "[['a']]",
            },
        ],
        "hint": "Use a dict where the key is the sorted letters of each word. Append each word to its matching group.",
        "solution": (
            "def solution(words: list) -> list:\n"
            "    groups = {}\n"
            "    for word in words:\n"
            "        key = ''.join(sorted(word))\n"
            "        if key not in groups:\n"
            "            groups[key] = []\n"
            "        groups[key].append(word)\n"
            "    return list(groups.values())"
        ),
        "concepts": [
            {
                "title": "Canonical Form as a Dict Key",
                "explanation": (
                    "To group 'equivalent' items, transform each into a canonical (standard) form "
                    "and use that as the dict key. For anagrams, the canonical form is the sorted letters."
                ),
                "examples": [
                    '"eat" → sorted → "aet"',
                    '"tea" → sorted → "aet"  ← same key, same group',
                    '"tan" → sorted → "ant"  ← different group',
                    "",
                    'groups["aet"] = ["eat", "tea", "ate"]',
                    'groups["ant"] = ["tan", "nat"]',
                ],
                "watch_out": (
                    "''.join(sorted(word)) turns the sorted character list back into a string "
                    "so it can be used as a dict key. Lists are not hashable and cannot be keys."
                ),
            },
            {
                "title": "dict.values() and Insertion Order",
                "explanation": (
                    "dict.values() returns all values in insertion order (guaranteed since Python 3.7). "
                    "Wrapping in list() materialises it into a proper list."
                ),
                "examples": [
                    "d = {'aet': ['eat','tea'], 'ant': ['tan']}",
                    "list(d.values())   # [['eat','tea'], ['tan']]",
                ],
                "watch_out": (
                    "dict.values() is a live view — it reflects changes to the dict. "
                    "Convert to list() before returning to get a stable snapshot."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#sorted",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — BEGINNER (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "is-power-of-two",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Is Power of Two?",
        "description": (
            "Write a function called `solution` that takes an integer and returns True "
            "if it is a power of 2 (1, 2, 4, 8, 16 …), False otherwise.\n\n"
            "Example:\n  solution(16) → True\n  solution(6) → False"
        ),
        "starter_code": "def solution(n: int) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(1)",  "expected_output": "True"},
            {"input": "solution(2)",  "expected_output": "True"},
            {"input": "solution(16)", "expected_output": "True"},
            {"input": "solution(6)",  "expected_output": "False"},
            {"input": "solution(0)",  "expected_output": "False"},
        ],
        "hint": "Keep dividing by 2. If you reach exactly 1, it is a power of 2. If you get an odd number before that, it is not.",
        "solution": (
            "def solution(n: int) -> bool:\n"
            "    if n <= 0:\n"
            "        return False\n"
            "    while n > 1:\n"
            "        if n % 2 != 0:\n"
            "            return False\n"
            "        n //= 2\n"
            "    return True"
        ),
        "concepts": [
            {
                "title": "Repeated Division to Check Divisibility",
                "explanation": (
                    "A power of 2 can be divided by 2 all the way down to 1 with no remainder. "
                    "If n % 2 != 0 at any point, it cannot be a power of 2."
                ),
                "examples": [
                    "16 → 8 → 4 → 2 → 1  (all even)  → True",
                    "6  → 3              (3 is odd)   → False",
                    "1  → loop skipped                → True  (2^0 = 1)",
                ],
                "watch_out": (
                    "n=0 must be handled up front. Without the guard, the while loop "
                    "would never run and you'd return True incorrectly."
                ),
            },
            {
                "title": "Bit-Trick Bonus  n & (n-1) == 0",
                "explanation": (
                    "Powers of 2 have exactly one bit set. Subtracting 1 flips all lower bits. "
                    "Their bitwise AND is always 0."
                ),
                "examples": [
                    "# 16 = 10000b, 15 = 01111b",
                    "16 & 15  # 0 → power of 2",
                    "# 6  = 110b,  5  = 101b",
                    "6  & 5   # 4 (non-zero) → not a power of 2",
                    "",
                    "# One-liner: n > 0 and (n & (n-1)) == 0",
                ],
                "watch_out": (
                    "The bit trick is O(1) and elegant, but requires understanding binary. "
                    "The loop approach is easier to reason about in an interview."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — INTERMEDIATE (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "insertion-sort",
        "topic": "algorithms",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Insertion Sort",
        "description": (
            "Write a function called `solution` that sorts a list of integers in ascending order "
            "using insertion sort. Return the sorted list. Do not use sort() or sorted().\n\n"
            "Pick each element and insert it into its correct position among the already-sorted "
            "elements to its left.\n\n"
            "Example:\n  solution([5, 2, 4, 6, 1, 3]) → [1, 2, 3, 4, 5, 6]"
        ),
        "starter_code": "def solution(nums: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([5, 2, 4, 6, 1, 3])", "expected_output": "[1, 2, 3, 4, 5, 6]"},
            {"input": "solution([3, 1, 2])",           "expected_output": "[1, 2, 3]"},
            {"input": "solution([1])",                 "expected_output": "[1]"},
            {"input": "solution([2, 2, 1])",           "expected_output": "[1, 2, 2]"},
        ],
        "hint": "For each element at index i, save it as 'key'. Shift larger elements one right until you find the correct slot, then place key there.",
        "solution": (
            "def solution(nums: list) -> list:\n"
            "    nums = nums[:]\n"
            "    for i in range(1, len(nums)):\n"
            "        key = nums[i]\n"
            "        j = i - 1\n"
            "        while j >= 0 and nums[j] > key:\n"
            "            nums[j + 1] = nums[j]\n"
            "            j -= 1\n"
            "        nums[j + 1] = key\n"
            "    return nums"
        ),
        "concepts": [
            {
                "title": "Insertion Sort Inner Loop",
                "explanation": (
                    "Pick nums[i] as the 'key'. Walk leftward while elements are bigger. "
                    "Shift each one right. When you stop, drop the key into the gap."
                ),
                "examples": [
                    "# [5, 2, 4] — insert 2 at i=1:",
                    "key=2, j=0",
                    "nums[0]=5 > 2 → shift: [5, 5, 4]",
                    "j=-1 → stop",
                    "nums[0] = 2 → [2, 5, 4]",
                ],
                "watch_out": (
                    "The while condition needs BOTH j >= 0 AND nums[j] > key. "
                    "Omitting j >= 0 causes an IndexError when the key belongs at position 0."
                ),
            },
            {
                "title": "Insertion Sort vs Bubble Sort",
                "explanation": (
                    "Both are O(n²) worst case, but insertion sort is adaptive — "
                    "it is O(n) on already-sorted input because the inner loop exits immediately."
                ),
                "examples": [
                    "# [1, 2, 3, 5, 4] — nearly sorted:",
                    "# Insertion: only fixes 5 and 4 — very fast",
                    "# Bubble: still makes multiple full passes",
                ],
                "watch_out": (
                    "Insertion sort is often used in practice for small arrays (< ~20 elements) "
                    "because its low constant factor beats O(n log n) algorithms at small sizes."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/howto/sorting.html",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — ADVANCED (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "count-primes",
        "topic": "algorithms",
        "difficulty": "advanced",
        "language": "python",
        "title": "Count Primes (Sieve of Eratosthenes)",
        "description": (
            "Write a function called `solution` that returns the count of prime numbers "
            "strictly less than n. Use the Sieve of Eratosthenes for efficiency.\n\n"
            "Example:\n  solution(10) → 4   (primes: 2, 3, 5, 7)\n  solution(20) → 8"
        ),
        "starter_code": "def solution(n: int) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(10)", "expected_output": "4"},
            {"input": "solution(2)",  "expected_output": "0"},
            {"input": "solution(20)", "expected_output": "8"},
            {"input": "solution(1)",  "expected_output": "0"},
        ],
        "hint": "Create a bool list of size n, all True. Set index 0 and 1 to False. For each unmarked number, mark its multiples False. Count the Trues.",
        "solution": (
            "def solution(n: int) -> int:\n"
            "    if n < 2:\n"
            "        return 0\n"
            "    is_prime = [True] * n\n"
            "    is_prime[0] = is_prime[1] = False\n"
            "    for i in range(2, int(n ** 0.5) + 1):\n"
            "        if is_prime[i]:\n"
            "            for j in range(i * i, n, i):\n"
            "                is_prime[j] = False\n"
            "    return sum(is_prime)"
        ),
        "concepts": [
            {
                "title": "The Sieve of Eratosthenes",
                "explanation": (
                    "Mark every number as prime. For each prime p (from 2 upward), "
                    "cross out all multiples of p starting at p². "
                    "What remains is every prime less than n."
                ),
                "examples": [
                    "is_prime: [F,F,T,T,T,T,T,T,T,T]  # indices 0..9",
                    "# p=2: mark 4,6,8   → [F,F,T,T,F,T,F,T,F,T]",
                    "# p=3: mark 9       → [F,F,T,T,F,T,F,T,F,F]",
                    "# sum = 4  (indices 2,3,5,7 are True)",
                ],
                "watch_out": (
                    "The outer loop only needs to reach sqrt(n). "
                    "Any composite number has a prime factor <= its square root, "
                    "so everything is already crossed out by then."
                ),
            },
            {
                "title": "[True] * n and sum() on Booleans",
                "explanation": (
                    "Multiplying a list by n creates n copies. "
                    "sum() counts True values because True == 1 in Python."
                ),
                "examples": [
                    "[True] * 5         # [True, True, True, True, True]",
                    "sum([True,False,True,True])  # 3",
                ],
                "watch_out": (
                    "sum(is_prime) is a clean idiom. Avoid looping with a counter — "
                    "the built-in sum is faster and more readable."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html",
    },

    # ──────────────────────────────────────────────
    # DATA STRUCTURES — INTERMEDIATE (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "sum-nested-list",
        "topic": "data-structures",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Sum a Nested List (Recursion)",
        "description": (
            "Write a function called `solution` that takes an arbitrarily nested list of integers "
            "and returns the sum of all numbers at any depth.\n\n"
            "Example:\n  solution([1, [2, 3], [4, [5, 6]]]) → 21\n  solution([[1, 2], [3, 4]]) → 10"
        ),
        "starter_code": "def solution(nested: list) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, [2, 3], [4, [5, 6]]])", "expected_output": "21"},
            {"input": "solution([[1, 2], [3, 4]])",          "expected_output": "10"},
            {"input": "solution([5])",                       "expected_output": "5"},
            {"input": "solution([])",                        "expected_output": "0"},
        ],
        "hint": "For each item: if it is a list, call solution() on it recursively; if it is an int, add it directly.",
        "solution": (
            "def solution(nested: list) -> int:\n"
            "    total = 0\n"
            "    for item in nested:\n"
            "        if isinstance(item, list):\n"
            "            total += solution(item)\n"
            "        else:\n"
            "            total += item\n"
            "    return total"
        ),
        "concepts": [
            {
                "title": "Recursion — Calling a Function from Itself",
                "explanation": (
                    "Recursion breaks a problem into a smaller version of itself. "
                    "Base case: item is an integer — add it. "
                    "Recursive case: item is a list — sum that sublist the same way."
                ),
                "examples": [
                    "solution([1, [2, 3]])",
                    "  → 1 + solution([2, 3])",
                    "  → 1 + (2 + 3)",
                    "  → 6",
                ],
                "watch_out": (
                    "Every recursive function needs a base case to stop. "
                    "Here, the base case is 'item is not a list'. "
                    "Without it you get infinite recursion and a RecursionError."
                ),
            },
            {
                "title": "isinstance(obj, type) — Runtime Type Check",
                "explanation": (
                    "isinstance(x, list) returns True if x is a list. "
                    "It is the Pythonic way to branch on an object's type."
                ),
                "examples": [
                    "isinstance([1, 2], list)     # True",
                    "isinstance(5, list)           # False",
                    "isinstance(5, int)            # True",
                    "isinstance(5, (int, float))  # True — check multiple types",
                ],
                "watch_out": (
                    "Avoid type(x) == list — it fails for subclasses. "
                    "isinstance handles inheritance correctly and is the preferred idiom."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#isinstance",
    },

    # ──────────────────────────────────────────────
    # DATA STRUCTURES — ADVANCED (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "bfs-shortest-path",
        "topic": "data-structures",
        "difficulty": "advanced",
        "language": "python",
        "title": "BFS Shortest Path",
        "description": (
            "Given a directed graph as an adjacency dict, write a function called `solution` "
            "that returns the number of edges in the shortest path from start to end. "
            "Return -1 if no path exists. Return 0 if start == end.\n\n"
            "Example:\n"
            "  graph = {'A':['B','C'], 'B':['D'], 'C':['D'], 'D':[]}\n"
            "  solution(graph, 'A', 'D') → 2"
        ),
        "starter_code": (
            "from collections import deque\n\n"
            "def solution(graph: dict, start: str, end: str) -> int:\n"
            "    # Your code here\n"
            "    pass"
        ),
        "test_cases": [
            {
                "input": "solution({'A':['B','C'],'B':['D'],'C':['D'],'D':[]}, 'A', 'D')",
                "expected_output": "2",
            },
            {
                "input": "solution({'A':['B'],'B':['C'],'C':[]}, 'A', 'C')",
                "expected_output": "2",
            },
            {
                "input": "solution({'A':[],'B':[]}, 'A', 'B')",
                "expected_output": "-1",
            },
            {
                "input": "solution({'A':['B'],'B':[]}, 'A', 'A')",
                "expected_output": "0",
            },
        ],
        "hint": "Use a deque. Store (node, distance) pairs. When you reach the destination, return the distance. Mark nodes visited when enqueued, not when processed.",
        "solution": (
            "from collections import deque\n\n"
            "def solution(graph: dict, start: str, end: str) -> int:\n"
            "    if start == end:\n"
            "        return 0\n"
            "    visited = {start}\n"
            "    queue = deque([(start, 0)])\n"
            "    while queue:\n"
            "        node, dist = queue.popleft()\n"
            "        for neighbour in graph.get(node, []):\n"
            "            if neighbour == end:\n"
            "                return dist + 1\n"
            "            if neighbour not in visited:\n"
            "                visited.add(neighbour)\n"
            "                queue.append((neighbour, dist + 1))\n"
            "    return -1"
        ),
        "concepts": [
            {
                "title": "BFS — Breadth-First Search",
                "explanation": (
                    "BFS explores level by level — all nodes 1 hop away first, then 2 hops, etc. "
                    "The first time it reaches the destination is guaranteed to be the shortest path."
                ),
                "examples": [
                    "# Graph: A→B, A→C, B→D",
                    "# BFS from A:",
                    "# Distance 0: [A]",
                    "# Distance 1: [B, C]",
                    "# Distance 2: [D]  ← first time we see D",
                ],
                "watch_out": (
                    "DFS does NOT guarantee shortest path — it goes deep, not wide. "
                    "Only BFS does, because shorter paths are always explored first."
                ),
            },
            {
                "title": "visited Set — Preventing Cycles",
                "explanation": (
                    "Without a visited set, cycles in the graph cause infinite loops. "
                    "Mark nodes visited when they are added to the queue."
                ),
                "examples": [
                    "visited = {start}",
                    "if neighbour not in visited:",
                    "    visited.add(neighbour)   # mark now, not on process",
                    "    queue.append((neighbour, dist + 1))",
                ],
                "watch_out": (
                    "Mark visited when ENQUEUING, not when DEQUEUING. "
                    "Late marking allows the same node to be added multiple times, "
                    "causing redundant work or incorrect distances."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/collections.html#collections.deque",
    },

    # ──────────────────────────────────────────────
    # OOP — BEGINNER (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "simple-calculator",
        "topic": "oop",
        "difficulty": "beginner",
        "language": "python",
        "title": "Simple Calculator Class",
        "description": (
            "Build a `Calculator` class that starts at 0 and supports:\n"
            "  - add(n) — adds n to the result\n"
            "  - subtract(n) — subtracts n\n"
            "  - multiply(n) — multiplies by n\n"
            "  - get_result() — returns the current result\n\n"
            "Write `solution(ops)` where ops is a list of ('add', n), ('subtract', n), "
            "or ('multiply', n) tuples. Return the final result.\n\n"
            "Example:\n  solution([('add', 10), ('multiply', 3)]) → 30"
        ),
        "starter_code": (
            "class Calculator:\n"
            "    def __init__(self):\n"
            "        pass\n\n"
            "    def add(self, n: int):\n"
            "        pass\n\n"
            "    def subtract(self, n: int):\n"
            "        pass\n\n"
            "    def multiply(self, n: int):\n"
            "        pass\n\n"
            "    def get_result(self) -> int:\n"
            "        pass\n\n\n"
            "def solution(ops: list) -> int:\n"
            "    pass"
        ),
        "test_cases": [
            {"input": "solution([('add', 10), ('multiply', 3)])",               "expected_output": "30"},
            {"input": "solution([('add', 10), ('subtract', 4)])",               "expected_output": "6"},
            {"input": "solution([('add', 6), ('multiply', 7)])",                "expected_output": "42"},
            {"input": "solution([('add', 10), ('multiply', 3), ('subtract', 5)])", "expected_output": "25"},
        ],
        "hint": "Store self.result = 0 in __init__. Each method updates self.result. get_result() just returns it.",
        "solution": (
            "class Calculator:\n"
            "    def __init__(self):\n"
            "        self.result = 0\n\n"
            "    def add(self, n: int):\n"
            "        self.result += n\n\n"
            "    def subtract(self, n: int):\n"
            "        self.result -= n\n\n"
            "    def multiply(self, n: int):\n"
            "        self.result *= n\n\n"
            "    def get_result(self) -> int:\n"
            "        return self.result\n\n\n"
            "def solution(ops: list) -> int:\n"
            "    calc = Calculator()\n"
            "    for op, n in ops:\n"
            "        if op == 'add':        calc.add(n)\n"
            "        elif op == 'subtract': calc.subtract(n)\n"
            "        elif op == 'multiply': calc.multiply(n)\n"
            "    return calc.get_result()"
        ),
        "concepts": [
            {
                "title": "State — Objects Remember Values Between Calls",
                "explanation": (
                    "self.result persists between method calls. "
                    "Each call to add() or multiply() modifies the stored state. "
                    "get_result() reads it back. This is the core value of encapsulation."
                ),
                "examples": [
                    "c = Calculator()",
                    "c.add(10)       # self.result = 10",
                    "c.multiply(3)   # self.result = 30",
                    "c.get_result()  # 30",
                ],
                "watch_out": (
                    "If you forget self. and write result = 0 in __init__, "
                    "it creates a local variable that disappears immediately. "
                    "State that must outlive a single method call MUST live on self."
                ),
            },
            {
                "title": "Tuple Unpacking in a for Loop",
                "explanation": (
                    "If each element of a list is a tuple, you can unpack it directly in the for statement."
                ),
                "examples": [
                    "ops = [('add', 5), ('subtract', 2)]",
                    "for op, n in ops:   # unpacks the tuple",
                    "    print(op, n)    # 'add' 5 → 'subtract' 2",
                ],
                "watch_out": (
                    "The number of variables must match the tuple length exactly. "
                    "for op, n in ops fails if any tuple has more or fewer than 2 elements."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/classes.html",
    },

    # ──────────────────────────────────────────────
    # OOP — INTERMEDIATE (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "library-catalog",
        "topic": "oop",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Library Catalog",
        "description": (
            "Write a class called `Library` with:\n"
            "  - add(title, author) — register a book\n"
            "  - find_by_author(author) — return a sorted list of titles by that author\n\n"
            "Write `solution(books, author)` where books is a list of (title, author) tuples. "
            "Return the alphabetically sorted list of titles by the given author.\n\n"
            "Example:\n"
            "  solution([('Fluent Python','Matthes'),('Clean Code','Martin'),\n"
            "             ('Python Crash Course','Matthes')], 'Matthes')\n"
            "  → ['Fluent Python', 'Python Crash Course']"
        ),
        "starter_code": (
            "class Library:\n"
            "    def __init__(self):\n"
            "        pass\n\n"
            "    def add(self, title: str, author: str):\n"
            "        pass\n\n"
            "    def find_by_author(self, author: str) -> list:\n"
            "        pass\n\n\n"
            "def solution(books: list, author: str) -> list:\n"
            "    pass"
        ),
        "test_cases": [
            {
                "input": "solution([('Fluent Python','Matthes'),('Clean Code','Martin'),('Python Crash Course','Matthes')], 'Matthes')",
                "expected_output": "['Fluent Python', 'Python Crash Course']",
            },
            {
                "input": "solution([('Clean Code','Martin')], 'Martin')",
                "expected_output": "['Clean Code']",
            },
            {
                "input": "solution([('Clean Code','Martin')], 'Beck')",
                "expected_output": "[]",
            },
        ],
        "hint": "Store books in a list of tuples. find_by_author filters by author and sorts with sorted().",
        "solution": (
            "class Library:\n"
            "    def __init__(self):\n"
            "        self.books = []\n\n"
            "    def add(self, title: str, author: str):\n"
            "        self.books.append((title, author))\n\n"
            "    def find_by_author(self, author: str) -> list:\n"
            "        return sorted(t for t, a in self.books if a == author)\n\n\n"
            "def solution(books: list, author: str) -> list:\n"
            "    lib = Library()\n"
            "    for title, auth in books:\n"
            "        lib.add(title, auth)\n"
            "    return lib.find_by_author(author)"
        ),
        "concepts": [
            {
                "title": "Filtering with a Generator in sorted()",
                "explanation": (
                    "sorted() accepts any iterable, including a generator expression. "
                    "You can filter and sort in one clean line."
                ),
                "examples": [
                    "books = [('Fluent Python','Matthes'), ('Clean Code','Martin')]",
                    "sorted(t for t, a in books if a == 'Matthes')",
                    "# ['Fluent Python']",
                ],
                "watch_out": (
                    "sorted() always returns a new list. "
                    "If no books match, the generator produces nothing and sorted() returns []."
                ),
            },
            {
                "title": "Choosing Your Internal Data Structure",
                "explanation": (
                    "A list of tuples is simple and naturally ordered. "
                    "A dict (title→author) is faster for direct title lookups but loses ordering. "
                    "Choose based on which operations you perform most."
                ),
                "examples": [
                    "# List — good for iterating, filtering:",
                    "self.books = [('Fluent Python', 'Matthes')]",
                    "",
                    "# Dict — good for O(1) title lookup:",
                    "self.books = {'Fluent Python': 'Matthes'}",
                ],
                "watch_out": (
                    "A dict keyed by title allows only one book per title. "
                    "A list allows duplicates. Think about which your design actually needs."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#sorted",
    },

    # ──────────────────────────────────────────────
    # BEST PRACTICES — BEGINNER (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "label-items",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "python",
        "title": "Label Items with enumerate()",
        "description": (
            "Write a function called `solution` that takes a list of strings and returns "
            "a new list where each item is prefixed with its index: '0: apple'.\n\n"
            "Use enumerate() — not a manual counter variable.\n\n"
            "Example:\n  solution(['apple','banana','cherry']) → ['0: apple','1: banana','2: cherry']"
        ),
        "starter_code": "def solution(items: list) -> list:\n    # Use enumerate()\n    pass",
        "test_cases": [
            {
                "input": "solution(['apple','banana','cherry'])",
                "expected_output": "['0: apple', '1: banana', '2: cherry']",
            },
            {"input": "solution(['only'])", "expected_output": "['0: only']"},
            {"input": "solution([])",       "expected_output": "[]"},
        ],
        "hint": "enumerate(items) gives (index, value) pairs. Use an f-string to format each label.",
        "solution": (
            "def solution(items: list) -> list:\n"
            "    return [f'{i}: {item}' for i, item in enumerate(items)]"
        ),
        "concepts": [
            {
                "title": "enumerate() — Index + Value Together",
                "explanation": (
                    "enumerate(iterable) yields (index, value) pairs. "
                    "It replaces the common pattern of maintaining a separate counter."
                ),
                "examples": [
                    "for i, val in enumerate(['a','b','c']):",
                    "    print(i, val)   # 0 a, 1 b, 2 c",
                    "",
                    "# Start from 1:",
                    "for i, val in enumerate(['a','b'], start=1):",
                    "    print(i, val)   # 1 a, 2 b",
                ],
                "watch_out": (
                    "for i, val in enumerate(items) is cleaner than for i in range(len(items)). "
                    "The range(len(...)) idiom is widely considered un-Pythonic."
                ),
            },
            {
                "title": "f-Strings — Inline Formatting",
                "explanation": (
                    "f-strings embed expressions directly in a string using {}. "
                    "Cleaner and faster than .format() or % formatting."
                ),
                "examples": [
                    'f"{0}: apple"     # "0: apple"',
                    'i, item = 2, "cherry"',
                    'f"{i}: {item}"    # "2: cherry"',
                    'f"{2 + 2}"        # "4"  — any expression works',
                ],
                "watch_out": (
                    "f-strings require Python 3.6+. "
                    "For older code you may see '{}: {}'.format(i, item). "
                    "f-strings are the modern standard — always prefer them."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#enumerate",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — BEGINNER (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "file-name-sanitizer",
        "topic": "scripting",
        "difficulty": "beginner",
        "language": "python",
        "title": "File Name Sanitizer",
        "description": (
            "Write a function called `solution` that cleans a file name by:\n"
            "  1. Converting all characters to lowercase\n"
            "  2. Replacing all spaces with underscores\n\n"
            "Return the sanitized name.\n\n"
            "Example:\n  solution('Hello World.txt') → 'hello_world.txt'\n"
            "  solution('My Script.PY') → 'my_script.py'"
        ),
        "starter_code": "def solution(filename: str) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("Hello World.txt")',   "expected_output": "hello_world.txt"},
            {"input": 'solution("My Script.PY")',      "expected_output": "my_script.py"},
            {"input": 'solution("already_clean.py")',  "expected_output": "already_clean.py"},
            {"input": 'solution("test file 123.txt")', "expected_output": "test_file_123.txt"},
        ],
        "hint": "Chain str methods: lower() then replace(' ', '_'). String methods return new strings, so they can be chained.",
        "solution": (
            "def solution(filename: str) -> str:\n"
            "    return filename.lower().replace(' ', '_')"
        ),
        "concepts": [
            {
                "title": "Method Chaining on Strings",
                "explanation": (
                    "String methods return a new string, so you can call another method "
                    "immediately on the result. This is called method chaining."
                ),
                "examples": [
                    '"Hello World".lower()                   # "hello world"',
                    '"Hello World".lower().replace(" ","_")  # "hello_world"',
                    "",
                    "# Equivalent with variables:",
                    's = "Hello World"',
                    's = s.lower()',
                    's = s.replace(" ", "_")',
                ],
                "watch_out": (
                    "Order matters. lower() then replace() is clearest here. "
                    "In general, think about what each step produces before chaining further."
                ),
            },
            {
                "title": "str.replace(old, new)",
                "explanation": (
                    "replace() substitutes every occurrence of old with new. "
                    "Strings are immutable, so it returns a new string."
                ),
                "examples": [
                    '"hello world".replace(" ", "_")   # "hello_world"',
                    '"aabaa".replace("a", "x")         # "xxbxx"',
                    '"hello".replace("z", "x")         # "hello" — no match, no change',
                ],
                "watch_out": (
                    "replace() replaces ALL occurrences. "
                    "Use replace(old, new, count) to cap replacements: 'aaa'.replace('a','b',2) → 'bba'."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.replace",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — BEGINNER (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "prime-checker",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Is Prime?",
        "description": (
            "Write a function called `solution` that takes an integer and returns True "
            "if it is a prime number, False otherwise.\n"
            "A prime is a number greater than 1 that has no divisors other than 1 and itself.\n\n"
            "Example:\n  solution(7) → True\n  solution(4) → False"
        ),
        "starter_code": "def solution(n: int) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(2)",  "expected_output": "True"},
            {"input": "solution(7)",  "expected_output": "True"},
            {"input": "solution(1)",  "expected_output": "False"},
            {"input": "solution(4)",  "expected_output": "False"},
            {"input": "solution(13)", "expected_output": "True"},
        ],
        "hint": "Check divisors from 2 up to the square root of n. If any divide n evenly, it's not prime.",
        "solution": (
            "def solution(n: int) -> bool:\n"
            "    if n < 2:\n"
            "        return False\n"
            "    for i in range(2, int(n ** 0.5) + 1):\n"
            "        if n % i == 0:\n"
            "            return False\n"
            "    return True"
        ),
        "concepts": [
            {
                "title": "Only Check Up to sqrt(n)",
                "explanation": (
                    "If n has a divisor larger than its square root, it must also have one smaller than it. "
                    "So checking up to sqrt(n) is sufficient — and much faster than checking all the way to n."
                ),
                "examples": [
                    "# Is 36 prime? sqrt(36) = 6",
                    "# Divisors of 36: 2,3,4,6 — all <= 6",
                    "# Once you find 2 divides 36, you're done",
                    "",
                    "int(n ** 0.5) + 1  # upper bound for range()",
                ],
                "watch_out": (
                    "int(n ** 0.5) truncates the float. Adding 1 ensures you include the square root itself. "
                    "For example, sqrt(25) = 5.0 → int = 5 → range(2, 6) checks 2,3,4,5 — 5 is tested."
                ),
            },
            {
                "title": "n % i == 0 — The Divisibility Test",
                "explanation": (
                    "n % i gives the remainder when n is divided by i. "
                    "If it is 0, i divides n evenly — so n is NOT prime."
                ),
                "examples": [
                    "10 % 2  # 0  → 2 divides 10 → not prime",
                    "7  % 2  # 1  → 2 doesn't divide 7",
                    "7  % 3  # 1  → 3 doesn't divide 7",
                    "7  % 4  # 3  → no divisor found → prime",
                ],
                "watch_out": (
                    "Handle n < 2 before the loop. 0 and 1 are not prime by definition, "
                    "and the loop would incorrectly return True for them."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#pow",
    },

    {
        "id": "most-frequent",
        "topic": "algorithms",
        "difficulty": "beginner",
        "language": "python",
        "title": "Most Frequent Element",
        "description": (
            "Write a function called `solution` that takes a non-empty list and returns "
            "the element that appears most often. If there is a tie, return the first one encountered.\n\n"
            "Example:\n  solution([1, 2, 2, 3, 3, 3]) → 3\n  solution(['a', 'b', 'a']) → 'a'"
        ),
        "starter_code": "def solution(items: list):\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1, 2, 2, 3, 3, 3])",     "expected_output": "3"},
            {"input": "solution(['a', 'b', 'a'])",          "expected_output": "a"},
            {"input": "solution([5])",                      "expected_output": "5"},
            {"input": "solution([1, 1, 2, 2])",            "expected_output": "1"},
        ],
        "hint": "Build a frequency dict first, then find the key with the highest value using max() with a key function.",
        "solution": (
            "def solution(items: list):\n"
            "    counts = {}\n"
            "    for item in items:\n"
            "        counts[item] = counts.get(item, 0) + 1\n"
            "    return max(counts, key=lambda k: counts[k])"
        ),
        "concepts": [
            {
                "title": "max() Over Dict Keys",
                "explanation": (
                    "Calling max(some_dict) iterates over the keys. "
                    "Pairing it with key=lambda k: counts[k] means 'find the key whose value is largest'."
                ),
                "examples": [
                    "counts = {'a': 1, 'b': 3, 'c': 2}",
                    "max(counts)                       # 'c' — alphabetically largest key",
                    "max(counts, key=lambda k: counts[k])  # 'b' — key with highest count",
                ],
                "watch_out": (
                    "max() on a dict iterates keys, NOT values. "
                    "Without the key argument you get the lexicographically largest key, "
                    "which is almost never what you want."
                ),
            },
            {
                "title": "collections.Counter — The Shortcut",
                "explanation": (
                    "Python's Counter class builds a frequency dict automatically. "
                    "most_common(1) returns the [(element, count)] pair with the highest count."
                ),
                "examples": [
                    "from collections import Counter",
                    "c = Counter([1, 2, 2, 3, 3, 3])",
                    "c                    # Counter({3:3, 2:2, 1:1})",
                    "c.most_common(1)     # [(3, 3)]",
                    "c.most_common(1)[0][0]  # 3",
                ],
                "watch_out": (
                    "Counter.most_common() returns a list of (element, count) tuples sorted by count. "
                    "Index [0][0] gets the element itself."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/collections.html#collections.Counter",
    },

    # ──────────────────────────────────────────────
    # ALGORITHMS — ADVANCED (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "max-subarray",
        "topic": "algorithms",
        "difficulty": "advanced",
        "language": "python",
        "title": "Maximum Subarray (Kadane's Algorithm)",
        "description": (
            "Write a function called `solution` that takes a list of integers and returns "
            "the largest sum of any contiguous subarray.\n\n"
            "Example:\n  solution([-2, 1, -3, 4, -1, 2, 1, -5, 4]) → 6\n"
            "  (subarray [4, -1, 2, 1] sums to 6)"
        ),
        "starter_code": "def solution(nums: list) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([-2, 1, -3, 4, -1, 2, 1, -5, 4])", "expected_output": "6"},
            {"input": "solution([1])",                               "expected_output": "1"},
            {"input": "solution([-1, -2, -3])",                     "expected_output": "-1"},
            {"input": "solution([5, 4, -1, 7, 8])",                 "expected_output": "23"},
        ],
        "hint": "Keep a running sum. If the running sum goes negative, reset it to 0 (start a fresh subarray). Track the best sum seen.",
        "solution": (
            "def solution(nums: list) -> int:\n"
            "    max_sum = nums[0]\n"
            "    current = nums[0]\n"
            "    for num in nums[1:]:\n"
            "        current = max(num, current + num)\n"
            "        max_sum = max(max_sum, current)\n"
            "    return max_sum"
        ),
        "concepts": [
            {
                "title": "Kadane's Algorithm",
                "explanation": (
                    "At each position, decide: is it better to extend the current subarray, "
                    "or start fresh from this element? "
                    "current = max(num, current + num). "
                    "Track the global best in max_sum."
                ),
                "examples": [
                    "nums = [-2, 1, -3, 4, -1, 2, 1]",
                    "# current: -2, 1, -2, 4, 3, 5, 6",
                    "# max_sum: -2, 1,  1, 4, 4, 5, 6",
                    "# Answer: 6",
                ],
                "watch_out": (
                    "Initialise max_sum and current to nums[0], NOT to 0. "
                    "If all numbers are negative, the answer is the least negative number — "
                    "starting at 0 would incorrectly return 0."
                ),
            },
            {
                "title": "max(a, b) as a Decision",
                "explanation": (
                    "max(num, current + num) is a one-liner for: "
                    "'if extending the subarray helps, extend it; otherwise start fresh here'."
                ),
                "examples": [
                    "# current = -5, num = 4:",
                    "max(4, -5 + 4)   # max(4, -1) = 4 → start fresh",
                    "",
                    "# current = 3, num = 2:",
                    "max(2, 3 + 2)    # max(2, 5) = 5 → extend",
                ],
                "watch_out": (
                    "This is O(n) time and O(1) space — far better than the O(n²) brute-force "
                    "of checking every possible subarray. Kadane's is the standard interview answer."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#max",
    },

    {
        "id": "merge-intervals",
        "topic": "algorithms",
        "difficulty": "advanced",
        "language": "python",
        "title": "Merge Overlapping Intervals",
        "description": (
            "Write a function called `solution` that takes a list of [start, end] intervals "
            "and merges all overlapping ones. Return the merged intervals sorted by start.\n\n"
            "Example:\n  solution([[1,3],[2,6],[8,10],[15,18]]) → [[1,6],[8,10],[15,18]]"
        ),
        "starter_code": "def solution(intervals: list) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([[1,3],[2,6],[8,10],[15,18]])", "expected_output": "[[1, 6], [8, 10], [15, 18]]"},
            {"input": "solution([[1,4],[4,5]])",                "expected_output": "[[1, 5]]"},
            {"input": "solution([[1,2]])",                      "expected_output": "[[1, 2]]"},
            {"input": "solution([[6,8],[1,9],[2,4]])",          "expected_output": "[[1, 9]]"},
        ],
        "hint": "Sort by start time. Walk through and if the current interval overlaps the last merged one (start <= last end), extend it; otherwise append a new interval.",
        "solution": (
            "def solution(intervals: list) -> list:\n"
            "    intervals.sort(key=lambda x: x[0])\n"
            "    merged = [intervals[0][:]]\n"
            "    for start, end in intervals[1:]:\n"
            "        if start <= merged[-1][1]:\n"
            "            merged[-1][1] = max(merged[-1][1], end)\n"
            "        else:\n"
            "            merged.append([start, end])\n"
            "    return merged"
        ),
        "concepts": [
            {
                "title": "Sort First, Then One Pass",
                "explanation": (
                    "Sorting by start time guarantees that any overlapping interval must "
                    "be adjacent after sorting. This reduces the problem to a single linear scan."
                ),
                "examples": [
                    "[[2,6],[1,3],[8,10]] → sorted → [[1,3],[2,6],[8,10]]",
                    "# Now [2,6] is right after [1,3] — easy to detect overlap",
                ],
                "watch_out": (
                    "Without sorting, you would need O(n²) to check every pair. "
                    "Sorting first makes the algorithm O(n log n) — the sort dominates."
                ),
            },
            {
                "title": "Detecting and Merging Overlap",
                "explanation": (
                    "Two intervals [a, b] and [c, d] overlap when c <= b. "
                    "The merged interval is [a, max(b, d)] — take the wider end."
                ),
                "examples": [
                    "# [1,3] and [2,6]: 2 <= 3 → overlap",
                    "# merged: [1, max(3,6)] = [1, 6]",
                    "",
                    "# [1,6] and [8,10]: 8 > 6 → no overlap",
                    "# append [8,10] as a new interval",
                ],
                "watch_out": (
                    "Use max(last_end, end) when merging — don't just take end. "
                    "A fully contained interval like [1,10] and [2,5] should produce [1,10], "
                    "but naively taking end=5 would shrink it incorrectly."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/howto/sorting.html",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — BEGINNER (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "chunk-list",
        "topic": "arrays-strings",
        "difficulty": "beginner",
        "language": "python",
        "title": "Split List into Chunks",
        "description": (
            "Write a function called `solution` that takes a list and an integer n, "
            "and returns the list split into sublists of size n. "
            "The last chunk may be smaller if the list doesn't divide evenly.\n\n"
            "Example:\n  solution([1,2,3,4,5], 2) → [[1,2],[3,4],[5]]"
        ),
        "starter_code": "def solution(items: list, n: int) -> list:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([1,2,3,4,5], 2)", "expected_output": "[[1, 2], [3, 4], [5]]"},
            {"input": "solution([1,2,3], 3)",      "expected_output": "[[1, 2, 3]]"},
            {"input": "solution([], 2)",            "expected_output": "[]"},
            {"input": "solution([1,2], 1)",         "expected_output": "[[1], [2]]"},
        ],
        "hint": "Use range(0, len(items), n) to step through starting indices, then slice items[i:i+n] for each.",
        "solution": (
            "def solution(items: list, n: int) -> list:\n"
            "    return [items[i:i + n] for i in range(0, len(items), n)]"
        ),
        "concepts": [
            {
                "title": "range(start, stop, step) — Stepping Through Indices",
                "explanation": (
                    "range(0, len(items), n) generates starting indices 0, n, 2n, 3n, … "
                    "For each index i, items[i:i+n] gives the next chunk."
                ),
                "examples": [
                    "list(range(0, 10, 3))   # [0, 3, 6, 9]",
                    "items = [1,2,3,4,5]",
                    "items[0:2]  # [1, 2]",
                    "items[2:4]  # [3, 4]",
                    "items[4:6]  # [5]   — slice past end is safe",
                ],
                "watch_out": (
                    "items[i:i+n] never raises an IndexError even if i+n > len(items). "
                    "Python slicing clamps silently, so the last chunk is naturally shorter."
                ),
            },
            {
                "title": "List Comprehension Over a Range",
                "explanation": (
                    "You can put any expression inside a list comprehension — "
                    "including a slice. This is a clean one-liner for chunking."
                ),
                "examples": [
                    "[items[i:i+n] for i in range(0, len(items), n)]",
                    "# For items=[1..5], n=2:",
                    "# i=0 → [1,2]",
                    "# i=2 → [3,4]",
                    "# i=4 → [5]",
                ],
                "watch_out": (
                    "range(0, 0, n) is empty, so an empty list returns [] correctly — "
                    "the comprehension produces zero iterations."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#func-range",
    },

    # ──────────────────────────────────────────────
    # ARRAYS & STRINGS — INTERMEDIATE (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "longest-common-prefix",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Longest Common Prefix",
        "description": (
            "Write a function called `solution` that takes a list of strings and returns "
            "the longest prefix shared by all of them. Return an empty string if there is none.\n\n"
            "Example:\n  solution(['flower','flow','flight']) → 'fl'\n"
            "  solution(['dog','racecar','car']) → ''"
        ),
        "starter_code": "def solution(words: list) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(['flower','flow','flight'])", "expected_output": "fl"},
            {"input": "solution(['dog','racecar','car'])",    "expected_output": ""},
            {"input": "solution(['abc','abc','abc'])",        "expected_output": "abc"},
            {"input": "solution(['a'])",                     "expected_output": "a"},
        ],
        "hint": "Use the first word as the reference. Keep trimming one character from the end until all words start with the current prefix.",
        "solution": (
            "def solution(words: list) -> str:\n"
            "    if not words:\n"
            "        return ''\n"
            "    prefix = words[0]\n"
            "    for word in words[1:]:\n"
            "        while not word.startswith(prefix):\n"
            "            prefix = prefix[:-1]\n"
            "            if not prefix:\n"
            "                return ''\n"
            "    return prefix"
        ),
        "concepts": [
            {
                "title": "str.startswith(prefix)",
                "explanation": (
                    "startswith() returns True if the string begins with the given prefix. "
                    "It is cleaner and faster than slicing s[:len(prefix)] == prefix."
                ),
                "examples": [
                    '"flower".startswith("fl")   # True',
                    '"flight".startswith("fl")   # True',
                    '"dog".startswith("fl")      # False',
                    '"".startswith("")           # True — empty prefix matches everything',
                ],
                "watch_out": (
                    "startswith('') is always True for any string. "
                    "The inner while loop exits as soon as prefix becomes empty, "
                    "so you need to check for that and return '' early."
                ),
            },
            {
                "title": "Shrinking a String  s[:-1]",
                "explanation": (
                    "s[:-1] returns everything except the last character. "
                    "Repeatedly applying it trims the string one character at a time."
                ),
                "examples": [
                    '"flower"[:-1]   # "flowe"',
                    '"flowe"[:-1]    # "flow"',
                    '"flow"[:-1]     # "flo"',
                    '"f"[:-1]        # ""  — empty string',
                ],
                "watch_out": (
                    '"[:-1] on an empty string returns "" without error, '
                    "but the while condition 'while not word.startswith(prefix)' "
                    "would loop forever on '' since startswith('') is always True. "
                    "Always add: if not prefix: return ''."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.startswith",
    },

    {
        "id": "matrix-diagonal-sum",
        "topic": "arrays-strings",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Matrix Diagonal Sum",
        "description": (
            "Write a function called `solution` that takes a square matrix (list of lists) "
            "and returns the sum of its main diagonal (top-left to bottom-right).\n\n"
            "Example:\n  solution([[1,2,3],[4,5,6],[7,8,9]]) → 15   (1 + 5 + 9)"
        ),
        "starter_code": "def solution(matrix: list) -> int:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution([[1,2,3],[4,5,6],[7,8,9]])", "expected_output": "15"},
            {"input": "solution([[1,0],[0,1]])",             "expected_output": "2"},
            {"input": "solution([[5]])",                     "expected_output": "5"},
            {"input": "solution([[1,2],[3,4]])",             "expected_output": "5"},
        ],
        "hint": "The main diagonal consists of elements where row index == column index. Sum matrix[i][i] for i in range(len(matrix)).",
        "solution": (
            "def solution(matrix: list) -> int:\n"
            "    return sum(matrix[i][i] for i in range(len(matrix)))"
        ),
        "concepts": [
            {
                "title": "Accessing a Matrix Cell  matrix[row][col]",
                "explanation": (
                    "A matrix is a list of lists. matrix[i] gives row i. "
                    "matrix[i][j] gives the element at row i, column j."
                ),
                "examples": [
                    "m = [[1,2,3],[4,5,6],[7,8,9]]",
                    "m[0]      # [1, 2, 3]  — row 0",
                    "m[0][0]   # 1  — top-left",
                    "m[1][1]   # 5  — centre",
                    "m[2][2]   # 9  — bottom-right",
                ],
                "watch_out": (
                    "matrix[i][i] only gives the MAIN diagonal. "
                    "The anti-diagonal (top-right to bottom-left) uses matrix[i][n-1-i]."
                ),
            },
            {
                "title": "Generator Expression with sum()",
                "explanation": (
                    "sum(matrix[i][i] for i in range(len(matrix))) is a clean one-liner. "
                    "It avoids creating an intermediate list."
                ),
                "examples": [
                    "m = [[1,2],[3,4]]",
                    "sum(m[i][i] for i in range(2))  # m[0][0]+m[1][1] = 1+4 = 5",
                ],
                "watch_out": (
                    "This assumes the matrix is square (n × n). "
                    "If rows and columns differ, len(matrix) != len(matrix[0]) "
                    "and you may need to use min(len(matrix), len(matrix[0]))."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html",
    },

    # ──────────────────────────────────────────────
    # BEST PRACTICES — BEGINNER (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "zip-to-dict",
        "topic": "best-practices",
        "difficulty": "beginner",
        "language": "python",
        "title": "Zip Two Lists into a Dict",
        "description": (
            "Write a function called `solution` that takes a list of keys and a list of values "
            "and returns a dictionary pairing them up. Use zip() — not a manual loop.\n\n"
            "Example:\n  solution(['a','b','c'], [1,2,3]) → {'a':1,'b':2,'c':3}"
        ),
        "starter_code": "def solution(keys: list, values: list) -> dict:\n    # Use zip()\n    pass",
        "test_cases": [
            {"input": "solution(['a','b','c'], [1,2,3])",  "expected_output": "{'a': 1, 'b': 2, 'c': 3}"},
            {"input": "solution(['x'], [42])",             "expected_output": "{'x': 42}"},
            {"input": "solution([], [])",                  "expected_output": "{}"},
        ],
        "hint": "dict(zip(keys, values)) is a Python one-liner. zip() pairs elements by position, dict() converts the pairs.",
        "solution": (
            "def solution(keys: list, values: list) -> dict:\n"
            "    return dict(zip(keys, values))"
        ),
        "concepts": [
            {
                "title": "zip() + dict() — The Classic Combo",
                "explanation": (
                    "zip(keys, values) produces pairs: (keys[0],values[0]), (keys[1],values[1]) … "
                    "dict() turns a sequence of (key, value) pairs into a dictionary."
                ),
                "examples": [
                    "keys   = ['a', 'b', 'c']",
                    "values = [1,   2,   3  ]",
                    "list(zip(keys, values))      # [('a',1), ('b',2), ('c',3)]",
                    "dict(zip(keys, values))      # {'a':1, 'b':2, 'c':3}",
                ],
                "watch_out": (
                    "zip() stops at the shorter list. "
                    "If keys=['a','b','c'] and values=[1,2], the result is {'a':1,'b':2} — 'c' is dropped silently."
                ),
            },
            {
                "title": "dict() Constructor Forms",
                "explanation": (
                    "dict() can be called several ways. Knowing them all is useful."
                ),
                "examples": [
                    "dict(a=1, b=2)                 # {'a':1,'b':2} — keyword args",
                    "dict([('a',1),('b',2)])        # {'a':1,'b':2} — list of pairs",
                    "dict(zip(keys, values))        # {'a':1,'b':2} — zip pairs",
                    "{k: v for k,v in zip(keys,values)}  # dict comprehension",
                ],
                "watch_out": (
                    "dict(a=1) only works when keys are valid Python identifiers (no spaces, no numbers first). "
                    "dict(zip(...)) works for any hashable keys."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/functions.html#zip",
    },

    # ──────────────────────────────────────────────
    # BEST PRACTICES — INTERMEDIATE (batch 2)
    # ──────────────────────────────────────────────

    {
        "id": "flatten-dict",
        "topic": "best-practices",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Flatten a Nested Dict",
        "description": (
            "Write a function called `solution` that takes a nested dictionary (one level deep) "
            "and returns a flat dict where nested keys are joined with a dot.\n\n"
            "Example:\n  solution({'a': {'b': 1, 'c': 2}, 'd': 3})\n  → {'a.b': 1, 'a.c': 2, 'd': 3}"
        ),
        "starter_code": "def solution(nested: dict) -> dict:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": "solution({'a': {'b': 1, 'c': 2}, 'd': 3})",
                "expected_output": "{'a.b': 1, 'a.c': 2, 'd': 3}",
            },
            {
                "input": "solution({'x': 1})",
                "expected_output": "{'x': 1}",
            },
            {
                "input": "solution({})",
                "expected_output": "{}",
            },
        ],
        "hint": "Iterate items(). If the value is a dict, iterate its items and build 'outer.inner' keys. Otherwise keep the key as-is.",
        "solution": (
            "def solution(nested: dict) -> dict:\n"
            "    flat = {}\n"
            "    for key, value in nested.items():\n"
            "        if isinstance(value, dict):\n"
            "            for sub_key, sub_val in value.items():\n"
            "                flat[f'{key}.{sub_key}'] = sub_val\n"
            "        else:\n"
            "            flat[key] = value\n"
            "    return flat"
        ),
        "concepts": [
            {
                "title": "Iterating Nested Dicts with .items()",
                "explanation": (
                    "dict.items() yields (key, value) pairs. "
                    "When the value is itself a dict, you can call .items() on it again "
                    "to iterate one level deeper."
                ),
                "examples": [
                    "d = {'a': {'b': 1, 'c': 2}}",
                    "for key, value in d.items():",
                    "    for sub_key, sub_val in value.items():",
                    "        print(f'{key}.{sub_key}', sub_val)",
                    "# prints: a.b 1,  a.c 2",
                ],
                "watch_out": (
                    "This only works for one level of nesting. "
                    "For arbitrarily deep dicts you would need a recursive approach."
                ),
            },
            {
                "title": "f-Strings for Building Compound Keys",
                "explanation": (
                    "f'{key}.{sub_key}' is the cleanest way to build the dotted key. "
                    "It is equivalent to key + '.' + sub_key but more readable."
                ),
                "examples": [
                    "key, sub_key = 'a', 'b'",
                    "f'{key}.{sub_key}'       # 'a.b'",
                    "key + '.' + sub_key      # 'a.b' — same result",
                ],
                "watch_out": (
                    "If a key already contains a dot (e.g. 'a.x'), the output can be ambiguous. "
                    "For production code, consider using a separator that cannot appear in keys."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#dict.items",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — BEGINNER (batch 4)
    # ──────────────────────────────────────────────

    {
        "id": "validate-email",
        "topic": "scripting",
        "difficulty": "beginner",
        "language": "python",
        "title": "Simple Email Validator",
        "description": (
            "Write a function called `solution` that takes a string and returns True if it "
            "looks like a valid email address, False otherwise.\n\n"
            "Rules:\n"
            "  - Contains exactly one '@'\n"
            "  - The part after '@' contains at least one '.'\n"
            "  - No spaces anywhere\n"
            "  - Not empty before '@' or after the last '.'\n\n"
            "Example:\n  solution('user@example.com') → True\n  solution('invalid') → False"
        ),
        "starter_code": "def solution(email: str) -> bool:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": 'solution("user@example.com")',  "expected_output": "True"},
            {"input": 'solution("invalid")',           "expected_output": "False"},
            {"input": 'solution("no@dot")',            "expected_output": "False"},
            {"input": 'solution("two@@at.com")',       "expected_output": "False"},
            {"input": 'solution("a @b.com")',          "expected_output": "False"},
        ],
        "hint": "Split on '@'. Check you get exactly two parts. Then check the second part contains a dot, and neither side is empty.",
        "solution": (
            "def solution(email: str) -> bool:\n"
            "    if ' ' in email:\n"
            "        return False\n"
            "    parts = email.split('@')\n"
            "    if len(parts) != 2:\n"
            "        return False\n"
            "    local, domain = parts\n"
            "    if not local or not domain:\n"
            "        return False\n"
            "    if '.' not in domain:\n"
            "        return False\n"
            "    return True"
        ),
        "concepts": [
            {
                "title": "Guard Clauses for Validation",
                "explanation": (
                    "Validation functions are a perfect fit for guard clauses. "
                    "Check each rule and return False early. "
                    "The happy path — return True — sits cleanly at the end."
                ),
                "examples": [
                    "if ' ' in email: return False",
                    "if len(parts) != 2: return False",
                    "if not local: return False",
                    "if '.' not in domain: return False",
                    "return True  # all checks passed",
                ],
                "watch_out": (
                    "Order matters. Check for spaces before splitting, "
                    "because a space could interfere with other checks."
                ),
            },
            {
                "title": "str.split(sep) and Checking the Result Length",
                "explanation": (
                    "email.split('@') splits on every '@'. "
                    "A valid email has exactly one '@', so the result should have exactly 2 parts."
                ),
                "examples": [
                    '"user@example.com".split("@")   # ["user", "example.com"]  — len 2',
                    '"two@@at.com".split("@")        # ["two", "", "at.com"]    — len 3',
                    '"invalid".split("@")            # ["invalid"]              — len 1',
                ],
                "watch_out": (
                    "len(parts) != 2 catches both missing '@' and multiple '@'. "
                    "This single check replaces two separate conditions."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/stdtypes.html#str.split",
    },

    # ──────────────────────────────────────────────
    # SCRIPTING — INTERMEDIATE (batch 3)
    # ──────────────────────────────────────────────

    {
        "id": "template-filler",
        "topic": "scripting",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Simple Template Engine",
        "description": (
            "Write a function called `solution` that takes a template string and a dict, "
            "and replaces every {{key}} placeholder with the corresponding value from the dict.\n\n"
            "Example:\n  solution('Hello {{name}}!', {'name': 'Mario'}) → 'Hello Mario!'\n"
            "  solution('{{a}} + {{b}} = {{c}}', {'a':'1','b':'2','c':'3'}) → '1 + 2 = 3'"
        ),
        "starter_code": "def solution(template: str, context: dict) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {
                "input": "solution('Hello {{name}}!', {'name': 'Mario'})",
                "expected_output": "Hello Mario!",
            },
            {
                "input": "solution('{{a}} + {{b}} = {{c}}', {'a': '1', 'b': '2', 'c': '3'})",
                "expected_output": "1 + 2 = 3",
            },
            {
                "input": "solution('No placeholders', {})",
                "expected_output": "No placeholders",
            },
        ],
        "hint": "Loop over the context dict and call str.replace('{{key}}', value) for each pair.",
        "solution": (
            "def solution(template: str, context: dict) -> str:\n"
            "    for key, value in context.items():\n"
            "        template = template.replace('{{' + key + '}}', value)\n"
            "    return template"
        ),
        "concepts": [
            {
                "title": "str.replace() for Templating",
                "explanation": (
                    "Iterating the context dict and calling replace() for each key is the simplest "
                    "template engine you can write. Each pass substitutes one placeholder."
                ),
                "examples": [
                    "t = 'Hello {{name}}, you are {{age}}!'",
                    "t = t.replace('{{name}}', 'Alice')",
                    "# t = 'Hello Alice, you are {{age}}!'",
                    "t = t.replace('{{age}}', '30')",
                    "# t = 'Hello Alice, you are 30!'",
                ],
                "watch_out": (
                    "replace() mutates the template string step by step. "
                    "Reassign: template = template.replace(...). "
                    "Without the reassignment the original string stays unchanged."
                ),
            },
            {
                "title": "String Concatenation for Dynamic Patterns",
                "explanation": (
                    "'{{' + key + '}}' builds the placeholder string at runtime. "
                    "This is cleaner than f'{{{{' + key + '}}}}' (double-brace escaping)."
                ),
                "examples": [
                    "key = 'name'",
                    "'{{' + key + '}}'     # '{{name}}'",
                    "f'{{{{{key}}}}}'      # '{{name}}' — f-string version (harder to read)",
                ],
                "watch_out": (
                    "In f-strings, {{ means a literal { and }} means a literal }. "
                    "String concatenation avoids the confusion entirely."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/library/string.html#template-strings",
    },

    {
        "id": "number-to-roman",
        "topic": "scripting",
        "difficulty": "intermediate",
        "language": "python",
        "title": "Number to Roman Numerals",
        "description": (
            "Write a function called `solution` that converts a positive integer (1–3999) "
            "to its Roman numeral representation.\n\n"
            "Example:\n  solution(3) → 'III'\n  solution(4) → 'IV'\n  solution(1994) → 'MCMXCIV'"
        ),
        "starter_code": "def solution(n: int) -> str:\n    # Your code here\n    pass",
        "test_cases": [
            {"input": "solution(3)",    "expected_output": "III"},
            {"input": "solution(4)",    "expected_output": "IV"},
            {"input": "solution(9)",    "expected_output": "IX"},
            {"input": "solution(58)",   "expected_output": "LVIII"},
            {"input": "solution(1994)", "expected_output": "MCMXCIV"},
        ],
        "hint": "Build a table of value→symbol pairs in descending order. Repeatedly subtract the largest value that fits and append its symbol.",
        "solution": (
            "def solution(n: int) -> str:\n"
            "    table = [\n"
            "        (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),\n"
            "        (100,'C'),(90,'XC'),(50,'L'),(40,'XL'),\n"
            "        (10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'),\n"
            "    ]\n"
            "    result = ''\n"
            "    for value, symbol in table:\n"
            "        while n >= value:\n"
            "            result += symbol\n"
            "            n -= value\n"
            "    return result"
        ),
        "concepts": [
            {
                "title": "Greedy Algorithm — Always Take the Largest That Fits",
                "explanation": (
                    "Work through the value table from largest to smallest. "
                    "While n >= current value, subtract that value and append its symbol. "
                    "This greedy approach produces the correct Roman numeral."
                ),
                "examples": [
                    "# n = 1994:",
                    "1994 >= 1000 → 'M',   n=994",
                    " 994 >= 900  → 'CM',  n=94",
                    "  94 >= 90   → 'XC',  n=4",
                    "   4 >= 4    → 'IV',  n=0",
                    "# Result: 'MCMXCIV'",
                ],
                "watch_out": (
                    "The subtractive cases (IV=4, IX=9, XL=40, etc.) must be in the table. "
                    "Without them, 4 would become 'IIII' instead of 'IV'."
                ),
            },
            {
                "title": "A Lookup Table as a List of Tuples",
                "explanation": (
                    "A list of (value, symbol) tuples is ideal here — it preserves order "
                    "and is easy to iterate. A dict would lose the ordering guarantee needed "
                    "for the greedy pass."
                ),
                "examples": [
                    "table = [(1000,'M'), (900,'CM'), ..., (1,'I')]",
                    "for value, symbol in table:",
                    "    while n >= value:",
                    "        result += symbol; n -= value",
                ],
                "watch_out": (
                    "Order is critical — the table MUST be descending. "
                    "Iterating in ascending order would produce wrong results."
                ),
            },
        ],
        "docs_url": "https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences",
    },

]
