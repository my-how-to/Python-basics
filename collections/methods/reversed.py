# ==========================================================
#               reversed()
# ==========================================================
#
# 1) WHAT IS reversed()?
#
# reversed() returns an iterator that produces elements
# of an iterable in reverse order.
#
# It does NOT modify the original object.
#
# Return value:
# - reverse iterator object
#
# ==========================================================
# 2) CORE SYNTAX
# ==========================================================
#
# reversed(iterable)
#
# iterable → must support:
# - __reversed__() method
# OR
# - sequence protocol (__len__() and __getitem__())
#
# ==========================================================
# 3) WHERE CAN IT BE USED?
# ==========================================================
#
# Works with:
# - list
# - tuple
# - str
# - range
#
# Does NOT work directly with:
# - set (unordered)
# - dict (unless explicitly converted)
#
# Example:
# reversed(set_object)  → TypeError
#
# ==========================================================
# 4) HOW IT WORKS INTERNALLY (CONCEPTUAL CORE)
# ==========================================================
#
# Conceptually:
#
# def reversed(seq):
#     index = len(seq) - 1
#     while index >= 0:
#         yield seq[index]
#         index -= 1
#
# Key idea:
# - Creates an iterator
# - Does NOT copy data
# - Memory efficient
# - Time complexity: O(n)
# - Space complexity: O(1)

# why do we need reversed() if we can just use slicing with a negative step to reverse a sequence?
# 1. Memory Efficiency: reversed() returns an iterator that produces items one at a time, 
#    while slicing with a negative step creates a new reversed copy of the entire sequence in memory. 
#    This can be a significant advantage when working with large sequences, 
#    as it avoids the overhead of creating a full copy.
#
# 2. Performance: For large sequences, using reversed() can be faster than slicing with a negative step 
#    because it does not require copying the entire sequence. The slicing operation has to create a
#    new list (or string) in memory, which takes time proportional to the size of the sequence, 
#    while reversed() simply iterates through the existing sequence in reverse order.
# 
# 3. Readability: Using reversed() can make it clearer to readers of the code
#    that the intention is to iterate through the sequence in reverse, while slicing 
#    with a negative step might be less immediately obvious to some readers, 
#    especially those who are less familiar with Python's slicing syntax.
#
# 4. Compatibility: reversed() can be used with any iterable that supports the sequence protocol
#    (i.e., has __len__() and __getitem__()), while slicing with a negative step only works with 
#    sequences that support slicing (like lists and strings). This means that reversed() 
#    can be used with a wider variety of objects, such as custom classes that implement the sequence protocol.
# 
# 5. Functionality: reversed() can be used in contexts where an iterator is required
#    (e.g., in a for loop or with functions that consume iterators), while slicing with a negative step 
#    always produces a new list (or string) object, which may not be desirable in all cases.
#  
# In summary, while slicing with a negative step can be a convenient way to reverse a sequence in some cases, 
#    reversed() offers advantages in terms of memory efficiency, performance, readability, 
#    compatibility, and functionality, making it a better choice in many situations.
#
# ==========================================================
# 5) BASIC EXAMPLES
# ==========================================================

# ---------- LIST ----------

numbers = [1, 2, 3, 4]

r = reversed(numbers)

print(r)    # <list_reverseiterator object at 0x...>

print(list(r))
# Output: [4, 3, 2, 1]

print(numbers)
# Output: [1, 2, 3, 4]  (unchanged)


# ---------- TUPLE ----------

t = (10, 20, 30)

print(tuple(reversed(t)))
# Output: (30, 20, 10)


# ---------- STRING ----------

text = "Python"

print("".join(reversed(text)))
# Output: nohtyP


# ==========================================================
# 6) IMPORTANT BEHAVIOR
# ==========================================================
#
# reversed() returns an iterator.
#
# That means:
# - It is consumed once.
#
# Example:

nums = [1, 2, 3]

r = reversed(nums)

print(list(r))  # [3, 2, 1]
print(list(r))  # []  (iterator exhausted)


# ==========================================================
# 7) reversed() vs reverse()
# ==========================================================
#
# reversed(iterable)
#     → returns iterator
#     → does NOT modify original
#
# list.reverse()
#     → modifies list in-place
#     → returns None
#
# ==========================================================
# 8) COMMON MISTAKE
# ==========================================================
#
# ❌ result = reversed([1,2,3])
#    print(result)  → shows iterator object
#
# ✔ Correct:
#    print(list(reversed([1,2,3])))
#
# ==========================================================
# 9) KEY RULES
# ==========================================================
#
# - Built-in function.
# - Returns iterator.
# - Does NOT modify original object.
# - Memory efficient.
# - Works only on reversible sequences.
#
# ==========================================================
# END OF LESSON
# ==========================================================