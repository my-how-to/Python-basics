# ==========================================================
#               add()
# ==========================================================
#
# 1) WHAT IS add()?
#
# add() adds a SINGLE element to a set.
#
# It modifies the set in-place.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# set.add(element)
#
# element → must be hashable (immutable type)
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Available only on:
# - set
#
# Not available on:
# - list (use append())
# - tuple (immutable)
# - dict (use assignment or update())
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough conceptual implementation:
#
# def add(self, element):
#     if element not in self:
#         insert element into internal hash table
#
# Key idea:
# - Uses hashing
# - Average time complexity: O(1)
# - Worst case: O(n) (rare hash collisions)
#
# Sets store elements in a hash table.
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- SIMPLE ADD ----------

numbers = {1, 2, 3}

numbers.add(4)

print(numbers)
# Output: {1, 2, 3, 4}


# ---------- ADDING DUPLICATE ----------

numbers.add(2)

print(numbers)
# Output: {1, 2, 3, 4}
# Duplicate ignored (sets do not allow duplicates)


# ---------- ADDING DIFFERENT TYPES ----------

data = set()

data.add(10)
data.add("hello")
data.add((1, 2))

print(data)
# Output: {10, 'hello', (1, 2)}

# data.add([1, 2])  # TypeError: list is not hashable


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# add() inserts the element AS-IS.
#
# The element must be:
# - Immutable
# - Hashable
#
# Allowed:
# - int
# - float
# - str
# - tuple (if it contains immutable elements)
#
# Not allowed:
# - list
# - dict
# - set
#
# ==========================================================
# 7) add() vs update()
# ==========================================================
#
# add(x)
#     → adds x as a single element
#
# update(iterable)
#     → adds each element of iterable separately
#
# Example:
#
# s = {1, 2}
#
# s.add((3, 4))
# # {1, 2, (3, 4)}
#
# s = {1, 2}
# s.update([3, 4])
# # {1, 2, 3, 4}
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================

numbers = {1, 2, 3}

result = numbers.add(4)

print(result)
# Output: None
#
# add() modifies in-place and returns None.
# Do NOT assign its result to a variable.
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Only for sets.
# - Modifies set in-place.
# - Returns None.
# - Adds exactly ONE element.
# - O(1) average time.
# - Element must be hashable.
#
# ==========================================================
# END OF LESSON
# ==========================================================