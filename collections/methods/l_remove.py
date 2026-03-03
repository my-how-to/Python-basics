# ==========================================================
#               remove()
# ==========================================================
#
# 1) WHAT IS remove()?
#
# remove() deletes the FIRST occurrence of a value from a list.
#
# It modifies the list in-place.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.remove(value)
#
# value → element to remove
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available on:
# - list
#
# Not available on:
# - tuple (immutable)
# - str (immutable)
# - set (uses different remove())
# - dict (no remove() method)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def remove(self, value):
#     for i in range(len(self)):
#         if self[i] == value:
#             del self[i]
#             return
#     raise ValueError("list.remove(x): x not in list")
#
# Key ideas:
# - Linear search (O(n))
# - Stops after first match
# - Raises ValueError if not found
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

numbers = [1, 2, 3, 2, 4]

numbers.remove(2)

print(numbers)
# Output: [1, 3, 2, 4]
# Only first 2 removed


# ==========================================================
# 6) ERROR CASE
# ==========================================================

values = [10, 20, 30]

# values.remove(40)
# Raises:
# ValueError: list.remove(x): x not in list


# ==========================================================
# 7) IMPORTANT BEHAVIOR
# ==========================================================
#
# remove() returns None
#

lst = [5, 6, 7]

result = lst.remove(6)

print(result)
# Output: None


# ==========================================================
# 8) REMOVE VS POP VS DEL
# ==========================================================
#
# remove(value)
#   - Removes by VALUE
#   - First occurrence only
#   - Raises ValueError if missing
#
# pop(index)
#   - Removes by INDEX
#   - Returns removed element
#
# del list[index]
#   - Removes by INDEX
#   - Does not return value
#
# ==========================================================
# 9) HOW TO REMOVE ALL OCCURRENCES
# ==========================================================

numbers = [1, 2, 2, 3, 2]

while 2 in numbers:
    numbers.remove(2)

print(numbers)
# Output: [1, 3]


# Better approach (cleaner and faster):

numbers = [1, 2, 2, 3, 2]

numbers = [x for x in numbers if x != 2]

print(numbers)
# Output: [1, 3]


# ==========================================================
# 10) SET NOTE (IMPORTANT DIFFERENCE)
# ==========================================================
#
# set.remove(value)
#   - Removes element
#   - Raises KeyError if not found
#
# set.discard(value)
#   - Removes element
#   - Does NOT raise error if not found
#
# ==========================================================
# 11) KEY RULES
# ==========================================================
#
# - Works only on lists.
# - Removes FIRST occurrence only.
# - Modifies list in-place.
# - Returns None.
# - Raises ValueError if value not found.
# - Time complexity O(n).
#
# ==========================================================
# END OF LESSON
# ==========================================================
