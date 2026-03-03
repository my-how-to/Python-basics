# ==========================================================
#               split()
# ==========================================================
#
# 1) WHAT IS split()?
#
# split() divides a string into a list of substrings.
#
# It does NOT modify the original string.
#
# Return type: list
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# str.split()
# str.split(separator)
# str.split(separator, maxsplit)
#
# separator → delimiter used to split the string
# maxsplit  → maximum number of splits
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - str ONLY
#
# Not available on:
# - list
# - tuple
# - set
# - dict
#
# ==========================================================
# 4) DEFAULT BEHAVIOR (IMPORTANT)
# ==========================================================
#
# If no separator is provided:
#
# - Splits on ANY whitespace
# - Treats multiple spaces as one
#

text = "  Python   is   powerful  "

result = text.split()

print(result)
# Output: ['Python', 'is', 'powerful']


# ==========================================================
# 5) USING A CUSTOM SEPARATOR
# ==========================================================

text = "apple,banana,orange"

print(text.split(","))
# Output: ['apple', 'banana', 'orange']


# ==========================================================
# 6) USING maxsplit
# ==========================================================

text = "one two three four"

print(text.split(" ", 2))
# Output: ['one', 'two', 'three four']

# Only first 2 splits are performed


# ==========================================================
# 7) EDGE CASES
# ==========================================================

# Separator not found

text = "hello"

print(text.split(","))
# Output: ['hello']


# Splitting empty string

text = ""

print(text.split())
# Output: []


# Explicit separator with empty string

text = ""

print(text.split(","))
# Output: ['']


# ==========================================================
# 8) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Conceptually:
#
# def split(self, separator=None, maxsplit=-1):
#     scan string from left to right
#     break into pieces when separator found
#     return list of substrings
#
# Time complexity: O(n)
#
# ==========================================================
# 9) split() VS rsplit()
# ==========================================================
#
# split()  → splits from LEFT
# rsplit() → splits from RIGHT
#
# Example:

text = "a-b-c-d"

print(text.split("-", 1))
# Output: ['a', 'b-c-d']

print(text.rsplit("-", 1))
# Output: ['a-b-c', 'd']


# ==========================================================
# 10) KEY RULES
# ==========================================================
#
# - Works only on strings.
# - Returns a NEW list.
# - Default separator = any whitespace.
# - maxsplit limits number of splits.
# - Does NOT modify original string.
# - Time complexity O(n).
#
# ==========================================================
# END OF LESSON
# ==========================================================
