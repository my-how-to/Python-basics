# ==========================================================
#               reverse()
# ==========================================================
#
# 1) WHAT IS reverse()?
#
# reverse() reverses the elements of a list IN-PLACE.
#
# It modifies the original list.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.reverse()
#
# No arguments.
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available only on:
# - list
#
# Not available on:
# - tuple (immutable)
# - set (unordered)
# - dict (no reverse method)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def reverse(self):
#     left = 0
#     right = len(self) - 1
#     while left < right:
#         swap(self[left], self[right])
#         left += 1
#         right -= 1
#
# Key idea:
# - Swaps elements from both ends toward the center
# - Time complexity: O(n)
# - Space complexity: O(1) (in-place)
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE REVERSE ----------

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)
# Output: [4, 3, 2, 1]


# ---------- REVERSE STRINGS IN LIST ----------

words = ["a", "b", "c"]

words.reverse()

print(words)
# Output: ['c', 'b', 'a']


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# reverse() modifies the list directly.
# It does NOT create a new list.
#
# Example:

a = [1, 2, 3]

b = a
a.reverse()

print(b)
# Output: [3, 2, 1]
# Because both refer to the same list object.


# ==========================================================
# 7) reverse() vs reversed()
# ==========================================================
#
# list.reverse()
#     → modifies the list in-place
#
# reversed(iterable)
#     → returns an iterator
#     → does NOT modify original object
#
# Example:
#
# a = [1, 2, 3]
#
# r = reversed(a)
# print(list(r))   # [3, 2, 1]
# print(a)         # [1, 2, 3]
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================

numbers = [1, 2, 3]

result = numbers.reverse()

print(result)
# Output: None
#
# reverse() modifies in-place and returns None.
# Do NOT assign its result.
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Only for lists.
# - Modifies list in-place.
# - Returns None.
# - O(n) time.
# - Use reversed() if you need a new reversed iterator.
#
# ==========================================================
# END OF LESSON
# ==========================================================