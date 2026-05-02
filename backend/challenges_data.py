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

]
