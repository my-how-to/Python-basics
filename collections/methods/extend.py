# ==========================================================
#               Method: extend()
# ==========================================================
#
# 1) WHAT IS extend()?
#
# extend() is a list method that adds elements from another
# iterable to the end of the list.
#
# It modifies the list in place.
# It does NOT return a new list.
#
# Return value: None
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# list.extend(iterable)
#
# iterable = any iterable object:
# - list
# - tuple
# - set
# - range
# - string (each character will be added separately)
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Only with:
# - list
#
# NOT available for:
# - tuple (immutable)
# - set (uses update())
# - dict (uses update())
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Rough internal idea:
#
# def extend(self, iterable):
#     for item in iterable:
#         self.append(item)
#
# That means:
# extend() iterates through the iterable
# and appends each element individually.
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

numbers = [1, 2]
more = [3, 4]

numbers.extend(more)

print(numbers)
# Output: [1, 2, 3, 4]


# ----------------------------------------------------------

# Using tuple

a = [10]
b = (20, 30)

a.extend(b)
print(a)
# Output: [10, 20, 30]


# ----------------------------------------------------------

# Using string

letters = ["A"]
letters.extend("BC")

print(letters)
# Output: ['A', 'B', 'C']
# Each character is added separately.


# ==========================================================
# 6) DIFFERENCE BETWEEN append() AND extend()
# ==========================================================

x = [1, 2]
y = [3, 4]

x.append(y)
print(x)
# Output: [1, 2, [3, 4]]
# append() adds the entire object as one element


x = [1, 2]
x.extend(y)
print(x)
# Output: [1, 2, 3, 4]
# extend() adds elements individually


# ==========================================================
# 7) IMPORTANT RULES
# ==========================================================
#
# - extend() modifies the original list.
# - It returns None.
# - It expects an iterable.
# - It does NOT create nested structures (unlike append).
#
# ==========================================================
# END OF LESSON
# ==========================================================
