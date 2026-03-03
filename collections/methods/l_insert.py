# ==========================================================
#               insert()
# ==========================================================
#
# 1) WHAT IS insert()?
#
# insert() adds an element to a specific position in a list.
#
# It modifies the list in-place.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.insert(index, value)
#
# index → position where element will be inserted
# value → element to insert
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
# - dict (no insert method)
# - str (immutable)
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def insert(self, index, value):
#     shift all elements from index to the right
#     place value at index
#     return None
#
# Key ideas:
# - Elements are shifted right
# - Time complexity: O(n)
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

numbers = [1, 2, 4]

numbers.insert(2, 3)

print(numbers)
# Output: [1, 2, 3, 4]


# ==========================================================
# 6) INDEX BEHAVIOR
# ==========================================================

# If index is greater than length → append to end

numbers = [1, 2, 3]
numbers.insert(100, 4)

print(numbers)
# Output: [1, 2, 3, 4]


# If index is negative → counts from left boundary

numbers = [1, 2, 3, 4, 5]
numbers.insert(-2, 99)

print(numbers)
# Output: [1, 2, 3, 99, 4, 5]
# -2 means insert before the second-to-last element, which is 4 in this case.


# ==========================================================
# 7) insert() VS append() VS extend()
# ==========================================================
#
# append(value)
#   - Adds element at END
#
# insert(index, value)
#   - Adds element at SPECIFIC position
#
# extend(iterable)
#   - Adds multiple elements at END
#
# Example:

lst = [1, 2]

lst.append(3)
# [1, 2, 3]

lst.insert(1, 99)
# [1, 99, 2, 3]

lst.extend([7, 8])
# [1, 99, 2, 3, 7, 8]


# ==========================================================
# 8) IMPORTANT BEHAVIOR
# ==========================================================
#
# insert() returns None
#

lst = [1, 2, 3]

result = lst.insert(1, 10)

print(result)
# Output: None


# ==========================================================
# 9) TIME COMPLEXITY
# ==========================================================
#
# O(n) because elements must be shifted.
#
# Slower than append(), which is O(1) average.
#
# ==========================================================
# 10) KEY RULES
# ==========================================================
#
# - Works ONLY on lists.
# - Modifies list in-place.
# - Returns None.
# - Shifts elements to the right.
# - If index > len(list) → behaves like append().
# - Time complexity O(n).
#
# ==========================================================
# END OF LESSON
# ==========================================================
