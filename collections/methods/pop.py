# =====================================================
#               Method: pop()
# =====================================================
#
# pop() removes an element AND returns it.
#
# It is supported by:
#   - list
#   - set
#   - dict
#
# It is NOT supported by:
#   - tuple (immutable)
#   - str (immutable)
#
# pop() always modifies the collection (in-place).
#
# =====================================================
# 1. list.pop()
# =====================================================
#
# Syntax:
#   list.pop(index)
#
# If index is omitted → removes last element.
# Returns removed element.
# Raises IndexError if list is empty or index invalid.

lst = [10, 20, 30]

value = lst.pop()
# Removes 30
# lst becomes [10, 20]
# value = 30

value = lst.pop(0)
# Removes 10
# lst becomes [20]
# value = 10

# Time Complexity:
#   pop()        → O(1)
#   pop(0)       → O(n)  (shifts elements)


# =====================================================
# 2. set.pop()
# =====================================================
#
# Syntax:
#   set.pop()
#
# Removes and returns a RANDOM element.
# (Sets are unordered.)
# Raises KeyError if set is empty.

s = {1, 2, 3}

value = s.pop()
# Removes random element
# s size decreases by 1

# Time Complexity:
#   Average: O(1)


# =====================================================
# 3. dict.pop()
# =====================================================
#
# Syntax:
#   dict.pop(key)
#   dict.pop(key, default)
#
# Removes key-value pair and returns VALUE.
# Raises KeyError if key missing (unless default provided).

d = {"a": 10, "b": 20}

value = d.pop("a")
# value = 10
# d becomes {"b": 20}

# Safe version:
value = d.pop("x", 0)
# No error
# value = 0

# Time Complexity:
#   Average: O(1)


# =====================================================
# 4. COMPARISON TABLE
# =====================================================
#
# Collection | pop() behavior                   | Returns       | Error if empty?
# ---------------------------------------------------------------
# list       | Removes by index (default last)  | removed item  | Yes (IndexError)
# set        | Removes random element           | removed item  | Yes (KeyError)
# dict       | Removes by key                   | value only    | Yes (KeyError)
#
# =====================================================
# 5. IMPORTANT EXAM TRAPS
# =====================================================
#
# 1. set.pop() does NOT remove the "first" element.
#    Sets are unordered.
#
# 2. dict.pop() returns VALUE, not (key, value).
#
# 3. list.pop() without argument removes LAST element.
#
# 4. pop() modifies the original object.
#
# 5. pop() is not available for tuple or str.
#
# =====================================================
# 6. PRACTICAL EXAMPLE
# =====================================================

# Simple stack behavior using list

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

while stack:
    print("Removed:", stack.pop())

# Output:
# Removed: 3
# Removed: 2
# Removed: 1

# Demonstrates LIFO behavior (Last-In, First-Out)
