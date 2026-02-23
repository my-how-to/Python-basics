# =====================================================
# PYTHON COLLECTION METHODS — ALPHABETICAL REFERENCE
# =====================================================
#
# Covered types:
#   list, tuple, set, dict, str
#
# For each method/function:
#   - Supported collections
#   - What it does
#   - Return value
#
# Methods that return None:
#   - add(), append(), clear(), copy(), discard(), extend(), insert(), remove(), reverse(), update()
#
# Methods that return a new collection:
#   - difference(), intersection(), symmetric_difference(), union(), sorted()
#
# Methods that return a value:
#   - all(), any(), count(), get(), index(), issubset(), issuperset(), items(), keys(), len(), max(), min(), pop(), popitem(), setdefault(),
#     values(), reversed()
#
# Methods that raise errors if conditions aren't met:
#   - remove() (if item not found, returns ValueError), 
#   - index() (if value not found, returns ValueError), 
#   - pop() (if list empty, returns IndexError; if dict key missing, returns KeyError), 
#   - popitem() (if dict empty, returns KeyError), 
#   - get() (if key not found and no default provided, returns None, but does not raise an error)
# Note: str is immutable. Any "modifying" behavior returns a NEW object.
#
# Methods that return lists:
#   - sorted(), reversed()
#
#
# NOTE:
# str is immutable. Any "modifying" behavior returns a NEW object.
#
# =====================================================
# add(x)
# =====================================================
# Supported: set
# Adds element
# Returns: None

{1, 2}.add(3) # {1, 2, 3}
x = {1, 2}.add(3) # x is None, because add() modifies the set in place and returns None.
print(x) # None

# =====================================================
# all(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys), str
# Returns True if all elements are truthy

all([1, True])
all("abc")

# =====================================================
# any(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys), str
# Returns True if at least one element is truthy

any([0, False, 1])
any("abc")

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
# Supported: list, tuple, str
# Counts occurrences
# Returns: int

[1,1,2].count(1)
(1,1,2).count(1)
"banana".count("a") # 3

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
# Supported: list, tuple, str
# Returns first index
# Raises ValueError if not found

[10,20,30].index(20)
(10,20,30).index(30)
"banana".index("n")

items = [1, 2, 3, 2, 1]
output = items.index(2, 2)
print(output) # 3 - index(value, start) searches for the value starting from the given index.

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
# Supported: list, tuple, set, dict, str
# Returns number of elements

len([1,2])
len("hello")

# =====================================================
# max(iterable)
# =====================================================
# Supported: list, tuple, set, str
# Returns largest element

max([3,1,2])
max("abc")

# =====================================================
# min(iterable)
# =====================================================
# Supported: list, tuple, set, str
# Returns smallest element

min((3,1,2))
min("abc")

# =====================================================
# pop()
# =====================================================
# Supported: list, set, dict
#
# list.pop(index) → removes & returns element
# set.pop() → removes random element
# dict.pop(key) → removes & returns value

[1,2,3].pop() # removes and returns last item: 3
{1,2,3}.pop() # removes and returns a random element (e.g., 2), but since sets are unordered, you cannot predict which one will be removed.
{"a":1}.pop("a") # removes "a" and returns its value: 1

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
# Supported: list, tuple, str
# Returns iterator

list(reversed([1,2,3]))
list(reversed("abc"))

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
lst.sort() # lst becomes [1, 2, 3]

# =====================================================
# sorted(iterable)
# =====================================================
# Supported: list, tuple, set, dict (keys), str
# Returns NEW sorted list

sorted([3,1,2]) # [1, 2, 3]
sorted((3,1,2)) # [1, 2, 3] - sorted() returns a new list, not a tuple. If you want a sorted tuple, you can convert it back
sorted({3,1,2})
sorted({"b":2,"a":1})
sorted("cba") # ['a', 'b', 'c'] - sorted() returns a new list of characters, not a string. If you want a sorted string, you can join the list back into a string: ''.join(sorted("cba")) → "abc"

# =====================================================
# sum(iterable)
# =====================================================
# Supported: list, tuple, set (numeric values only)
# NOT supported: str
# Returns total sum

sum([1,2,3])
sum((1,2,3))

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
