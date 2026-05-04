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
]
