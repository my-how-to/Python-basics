# ==========================================================
#               sort()
# ==========================================================
#
# 1) WHAT IS sort()?
#
# sort() sorts a LIST in-place.
#
# It modifies the original list.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.sort()
# list.sort(key=...)
# list.sort(reverse=True/False)
#
# key     → function used for custom sorting
# reverse → if True, sorts in descending order
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - list ONLY
#
# Not available on:
# - tuple (immutable)
# - set (unordered)
# - dict (no sort method)
# - str (immutable)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Python uses Timsort algorithm:
# - Hybrid of merge sort + insertion sort
# - Stable sort (preserves order of equal elements)
# - Time complexity: O(n log n)
#
# Conceptually:
#
# def sort(self, key=None, reverse=False):
#     rearrange elements inside self
#     return None
#
# Important:
# sort() does NOT create a new list.
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

numbers = [4, 1, 3, 2]

numbers.sort()

print(numbers)
# Output: [1, 2, 3, 4]


# ==========================================================
# 6) reverse PARAMETER
# ==========================================================

numbers = [1, 4, 2, 3]

numbers.sort(reverse=True)

print(numbers)
# Output: [4, 3, 2, 1]


# ==========================================================
# 7) key PARAMETER (VERY IMPORTANT)
# ==========================================================

# Sort by length

words = ["apple", "kiwi", "banana"]

words.sort(key=len)

print(words)
# Output: ['kiwi', 'apple', 'banana']


# Sort by last digit

numbers = [21, 34, 12, 45]

numbers.sort(key=lambda x: x % 10)

print(numbers)
# Output: [21, 12, 34, 45]


# ==========================================================
# 8) sort() VS sorted()
# ==========================================================
#
# list.sort()
#   - Works only on lists
#   - Modifies list in-place
#   - Returns None
#
# sorted(iterable)
#   - Works on any iterable
#   - Returns NEW list
#   - Does NOT modify original
#
# Example:

numbers = [3, 1, 2]

new_list = sorted(numbers)

print(numbers)   # [3, 1, 2]
print(new_list)  # [1, 2, 3]


# ==========================================================
# 9) ERROR CASES
# ==========================================================
#
# Cannot sort mixed incomparable types in Python 3:
#

# lst = [1, "a", 3]
# lst.sort()
# Raises TypeError because int and str cannot be compared for sorting.


# ==========================================================
# 10) STABILITY (EXAM IMPORTANT)
# ==========================================================
#
# sort() is STABLE.
# Equal elements keep their original order.
#

data = [("A", 2), ("B", 2), ("C", 1)]

data.sort(key=lambda x: x[1]) # Sort by second element of tuple

print(data)
# Output:
# [('C', 1), ('A', 2), ('B', 2)]
# A stays before B (same key value)


# ==========================================================
# 11) TIME COMPLEXITY
# ==========================================================
#
# Average: O(n log n)
# Best case: O(n)  (nearly sorted data)
#
# ==========================================================
# 12) KEY RULES
# ==========================================================
#
# - Works ONLY on lists.
# - Modifies list in-place.
# - Returns None.
# - Stable sorting algorithm (Timsort).
# - Supports key and reverse parameters.
#
# ==========================================================
# END OF LESSON
# ==========================================================
