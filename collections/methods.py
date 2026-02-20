# =====================================================
# PYTHON COLLECTION METHODS — ALPHABETICAL REFERENCE
# =====================================================
#
# Covered types:
#   list, tuple, set, dict
#
# For each method:
#   - Supported collections
#   - What it does
#   - Return value
# 
# Methods are organized alphabetically for easy reference. This is not a tutorial, but a quick lookup guide.
# For detailed explanations and examples, refer to the individual collection type lessons.
# 
# Methods covered:
#   add(x)                      | set
#   all(iterable)               | list, tuple, set, dict (keys)
#   any(iterable)               | list, tuple, set, dict (keys)    
#   append(x)                   | list
#   clear()                     | list, set, dict
#   copy()                      | list, set, dict
#   count(value)                | list, tuple
#   difference(other)           | set
#   discard(x)                  | set
#   extend(iterable)            | list
#   get(key, default=None)      | dict
#   index(value)                | list, tuple   
#   insert(index, value)        | list
#   intersection(other)         | set
#   issubset(other)             | set
#   issuperset(other)           | set
#   items()                     | dict
#   keys()                      | dict
#   len(collection)             | list, tuple, set, dict    
#   max(iterable)               | list, tuple, set
#   min(iterable)               | list, tuple, set
#   pop()                       | list, set, dict
#   popitem()                   | dict
#   remove(value)               | list, set
#   reverse()                   | list
#   reversed(iterable)          | list, tuple
#   setdefault(key, default)    | dict
#   sort()                      | list
#   sorted(iterable)            | list, tuple, set, dict (keys)
#   sum(iterable)               | list, tuple, set (numeric values)
#   symmetric_difference(other) | set
#   union(other)                | set
#   update(iterable_or_dict)    | set, dict
#   values()                    | dict
#
# =====================================================
# add(x)
# =====================================================
# Supported: set
# Adds element
# Returns: None

s = {1, 2}
s.add(3)

# =====================================================
# all(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys)
# Returns True if all elements are truthy

all([1, True])  # True

# =====================================================
# any(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys)
# Returns True if at least one element is truthy

any([0, False, 1])  # True

# =====================================================
# append(x)
# =====================================================
# Supported: list
# Adds element to end
# Returns: None

lst = [1, 2]
lst.append(3)

# =====================================================
# clear()
# =====================================================
# Supported: list, set, dict
# Removes all elements
# Returns: None

lst.clear()

# =====================================================
# copy()
# =====================================================
# Supported: list, set, dict
# Returns shallow copy

new_lst = lst.copy()

# =====================================================
# count(value)
# =====================================================
# Supported: list, tuple
# Counts occurrences
# Returns: int

[1,1,2].count(1)
(1,1,2).count(1)

# =====================================================
# difference(other)
# =====================================================
# Supported: set
# Returns new set

{1,2}.difference({2})

# =====================================================
# discard(x)
# =====================================================
# Supported: set
# Removes element if exists (no error if missing)
# Returns: None

{1,2}.discard(2)

# =====================================================
# extend(iterable)
# =====================================================
# Supported: list
# Adds multiple elements
# Returns: None

lst.extend([4,5])

# =====================================================
# get(key, default=None)
# =====================================================
# Supported: dict
# Safe key access
# Returns value or default

{"a":1}.get("a")
{"a":1}.get("x", 0)

# =====================================================
# index(value)
# =====================================================
# Supported: list, tuple
# Returns first index
# Raises ValueError if not found

[10,20,30].index(20)
(10,20,30).index(30)

# =====================================================
# insert(index, value)
# =====================================================
# Supported: list
# Inserts element
# Returns: None

lst.insert(1, 100)

# =====================================================
# intersection(other)
# =====================================================
# Supported: set
# Returns common elements

{1,2}.intersection({2,3})

# =====================================================
# issubset(other)
# =====================================================
# Supported: set
# Returns True/False

{1}.issubset({1,2})

# =====================================================
# issuperset(other)
# =====================================================
# Supported: set
# Returns True/False

{1,2}.issuperset({1})

# =====================================================
# items()
# =====================================================
# Supported: dict
# Returns view of key-value pairs

{"a":1}.items()

# =====================================================
# keys()
# =====================================================
# Supported: dict
# Returns view of keys

{"a":1}.keys()

# =====================================================
# len(collection)
# =====================================================
# Supported: list, tuple, set, dict
# Returns number of elements

len([1,2])
len({"a":1})

# =====================================================
# max(iterable)
# =====================================================
# Supported: list, tuple, set
# Returns largest element

max([3,1,2])

# =====================================================
# min(iterable)
# =====================================================
# Supported: list, tuple, set
# Returns smallest element

min((3,1,2))

# =====================================================
# pop()
# =====================================================
# Supported: list, set, dict
#
# list.pop(index) → removes & returns element
# set.pop() → removes random element
# dict.pop(key) → removes & returns value

[1,2,3].pop()
{1,2,3}.pop()
{"a":1}.pop("a")

# =====================================================
# popitem()
# =====================================================
# Supported: dict
# Removes last inserted pair
# Returns tuple (key, value)

{"a":1}.popitem()

# =====================================================
# remove(value)
# =====================================================
# Supported: list, set
# Removes element
# Raises error if not found
# Returns: None

[1,2,3].remove(2)
{1,2,3}.remove(2)

# =====================================================
# reverse()
# =====================================================
# Supported: list
# Reverses in-place
# Returns: None

lst.reverse()

# =====================================================
# reversed(iterable)
# =====================================================
# Supported: list, tuple
# Returns iterator

list(reversed([1,2,3]))

# =====================================================
# setdefault(key, default)
# =====================================================
# Supported: dict
# Returns value if exists; otherwise inserts default

d = {}
d.setdefault("x", 10)

# =====================================================
# sort()
# =====================================================
# Supported: list
# Sorts in-place
# Returns: None

lst = [3,1,2]
lst.sort()

# =====================================================
# sorted(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys)
# Returns NEW sorted list

sorted([3,1,2])
sorted((3,1,2))
sorted({3,1,2})
sorted({"b":2,"a":1})

# =====================================================
# sum(iterable)
# =====================================================
# Supported: list, tuple, set (numeric values)
# Returns total sum

sum([1,2,3]) # 6
sum((4,5))   # 9
sum({10,20}) # 30

# =====================================================
# symmetric_difference(other)
# =====================================================
# Supported: set
# Returns elements in either set but not both

{1,2}.symmetric_difference({2,3})

# =====================================================
# union(other)
# =====================================================
# Supported: set
# Returns new set with all unique elements

{1,2}.union({2,3})

# =====================================================
# update(iterable_or_dict)
# =====================================================
# Supported: set, dict
#
# set.update(iterable) → adds multiple elements
# dict.update(dict) → merges dictionaries
# Returns: None

{1}.update([2,3])
{"a":1}.update({"b":2})

# =====================================================
# values()
# =====================================================
# Supported: dict
# Returns view of values

{"a":1}.values()
