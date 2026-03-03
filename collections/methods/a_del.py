# ==========================================================
#               Statement: del
# ==========================================================
#
# 1) WHAT IS del?
#
# del is a STATEMENT (not a method, not a function).
#
# It removes:
# - variables
# - list elements
# - slices
# - dictionary keys
# - object attributes
#
# It does NOT return anything.
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# del variable
# del list[index]
# del list[start:end]
# del dict[key]
# del object.attribute
#
# ==========================================================
# 3) DELETING VARIABLES
# ==========================================================

x = 10
del x

# print(x)
# Raises:
# NameError


# ==========================================================
# 4) USING del WITH LISTS
# ==========================================================

numbers = [10, 20, 30, 40]

# Delete by index
del numbers[1]

print(numbers)
# Output: [10, 30, 40]


# Delete slice
del numbers[0:2]

print(numbers)
# Output: [40] # Remaining list after deleting first two elements
# Note: del shifts elements left after deletion, so indices change.


# ==========================================================
# 5) USING del WITH DICTIONARIES
# ==========================================================

d = {"a": 1, "b": 2}

del d["a"]

print(d)
# Output: {'b': 2}


# ==========================================================
# 6) USING del WITH OBJECT ATTRIBUTES
# ==========================================================

class A:
    def __init__(self):
        self.value = 100

obj = A()

del obj.value

# print(obj.value)
# Raises:
# AttributeError


# ==========================================================
# 7) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# del removes a reference to an object.

a = [1, 2, 3]
b = a
del a
print(b)

# Output: [1, 2, 3] Because del removed the name a, not the object.

# If no references remain:
# → Python's garbage collector may free memory.
#
# Important:
# del does NOT delete the object directly.
# It deletes the name/reference.
#
# ==========================================================
# 8) del VS pop() VS remove()
# ==========================================================
#
# del list[index]
#   - Removes by index
#   - No return value
#
# list.pop(index)
#   - Removes by index
#   - Returns removed element
#
# list.remove(value)
#   - Removes by value
#   - Returns None
#
# dict.pop(key)
#   - Removes key
#   - Returns value
#
# ==========================================================
# 9) ERROR CASES
# ==========================================================

lst = [1, 2, 3]

# del lst[10]
# Raises IndexError

d = {"a": 1}

# del d["b"]
# Raises KeyError


# ==========================================================
# 10) TIME COMPLEXITY
# ==========================================================
#
# list del by index → O(n) (elements shift)
# list del slice    → O(n)
# dict del key      → O(1) average
#
# ==========================================================
# 11) KEY RULES
# ==========================================================
#
# - del is a statement, not a method.
# - Removes references.
# - Does not return anything.
# - Works on variables, lists, dicts, attributes.
# - Raises errors if target does not exist.
#
# ==========================================================
# END OF LESSON
# ==========================================================