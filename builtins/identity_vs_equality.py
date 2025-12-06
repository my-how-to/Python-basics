# ============================================================
#           IDENTITY vs EQUALITY — PYTHON LESSON
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains the difference between:
#       - "=="  (equality — compares values)
#       - "is"  (identity — compares memory references)
#   with clear, runnable examples.
#
# Contents:
#   1. Equality (==)
#   2. Identity (is)
#   3. Mutables vs immutables
#   4. When to use "is"
#   5. Common mistakes
#   6. Diagnostic example
#   7. Advanced note: Why "1000 is 1000" may be True or False
# ============================================================


# ============================================================
# 1. EQUALITY USING ==
# ============================================================
print("\n--- SECTION 1: Equality (==) ---")

a = [1, 2]
b = [1, 2]

print("a == b:", a == b)   # True — lists contain the same values
print("a is b:", a is b)   # False — different list objects


# ============================================================
# 2. IDENTITY USING is
# ============================================================
print("\n--- SECTION 2: Identity (is) ---")

x = [10, 20]
y = x

print("x == y:", x == y)   # True — same content
print("x is y:", x is y)   # True — same object in memory


# ============================================================
# 3. MUTABLE VS IMMUTABLE OBJECTS
# ============================================================
print("\n--- SECTION 3: Mutable vs Immutable ---")

# Immutable values like small integers may be reused internally.
n1 = 100
n2 = 100
print("n1 is n2:", n1 is n2)   # True — small integer caching (-5 to 256)

# Larger integers are not guaranteed to be reused.
n3 = 1000
n4 = 1000
print("n3 is n4:", n3 is n4)   # True or False — depends on compiler optimizations

# Strings may or may not be interned.
s1 = "hello"
s2 = "hello"
print("s1 is s2:", s1 is s2)   # often True (interned)

s3 = "a long string with spaces"
s4 = "a long string with spaces"
print("s3 is s4:", s3 is s4)   # may be False


# ============================================================
# 4. WHEN TO USE "is"
# ============================================================
print("\n--- SECTION 4: Correct usage of 'is' ---")

value = None

# The interpreter stores only one real None object, 
# so `is` confirms you have that exact object.
print("value is None:", value is None)   # correct

# Equality checks can be overloaded, so `value == None` 
# might call custom logic instead of the plain None comparison.
print("value == None:", value == None)   # allowed but not recommended


# ============================================================
# 5. COMMON MISTAKES
# ============================================================
print("\n--- SECTION 5: Common mistakes ---")

print("5 is 5:", 5 is 5)     # may be True but should not be relied on
print("5 == 5:", 5 == 5)     # correct way to compare numbers

print('"ab" is "ab":', "ab" is "ab")   # unpredictable
print('"ab" == "ab":', "ab" == "ab")   # correct


# ============================================================
# 6. PRACTICAL DIAGNOSTIC EXAMPLE
# ============================================================
print("\n--- SECTION 6: Practical diagnostic example ---")

try:
    5 / "2"
except Exception as e:
    print("Exception type:", type(e).__name__)
    print("Exception class is TypeError:", type(e) is TypeError)


# ============================================================
# 7. ADVANCED NOTE: WHY "1000 is 1000" MAY BE TRUE OR FALSE
# ============================================================
print("\n--- SECTION 7: Advanced note — integer identity behavior ---")

# Python guarantees caching only for integers in the range [-5, 256].
# Outside that range, identity reuse is NOT guaranteed.

# Example 1: Variables written literally in code may share the same object.
a = 1000
b = 1000
print("a is b (literal assignment):", a is b)  # True on some systems, False on others

# Example 2: Creating integers dynamically forces new objects.
c = int("1000")
d = int("1000")
print("c is d (from int()):", c is d)  # usually False

# Example 3: Re-evaluation inside functions often creates new integers.
def make():
    return 1000

x = make()
y = make()
print("x is y (from function):", x is y)  # usually False

# Key rule:
#    DO NOT use "is" for comparing integers or strings.
#    Use == for values.
