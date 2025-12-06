# ============================================================
#                   PYTHON IDENTITY OPERATOR — is
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson extends "identity_vs_equality.py" by diving into the
#   nuanced uses of the identity operator:
#       - diagnosing aliasing in complex structures
#       - shallow vs deep copies and their identities
#       - singleton sentinels beyond None
#       - string interning and manual control with sys.intern()
#       - type objects and strict identity checks
#       - debugging helpers using id()
#
# Run this file to explore the advanced side of the "is" operator.
# ============================================================


# ============================================================
# 1. DIAGNOSING ALIASING IN NESTED STRUCTURES
# ============================================================
print("\n--- SECTION 1: Nested Aliasing ---")

row = [0, 0, 0]
grid_bad = [row] * 3           # repeats the same list reference
grid_good = [row.copy() for _ in range(3)]

grid_bad[0][1] = 99
print("grid_bad:", grid_bad)   # every row reflects the change
print("grid_good:", grid_good) # only first row changes

print("id(grid_bad[0]):", id(grid_bad[0]))
print("id(grid_bad[1]):", id(grid_bad[1]))
print("IDs identical → rows share identity.\n")


# ============================================================
# 2. SHALLOW vs DEEP COPIES
# ============================================================
print("\n--- SECTION 2: Copy Semantics ---")

import copy

original = [[1], [2]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print("original:", original)
print("shallow:", shallow)  # inner list shared with original
print("deep:", deep)        # deep copy keeps its own structures

print("original[0] is shallow[0]:", original[0] is shallow[0])
print("original[0] is deep[0]:", original[0] is deep[0])


# ============================================================
# 3. SINGLETONS AND CUSTOM SENTINELS
# ============================================================
print("\n--- SECTION 3: Singletons & Sentinels ---")

# Built-in singletons
print("None is None:", None is None)
print("True is True:", True is True)
print("Ellipsis is ...:", (Ellipsis is ...))
print("NotImplemented is NotImplemented:", NotImplemented is NotImplemented)

# Custom sentinel for optional parameters
MISSING = object()

def load_user(user_id=MISSING):
    if user_id is MISSING:
        print("load_user called without an ID.")
    else:
        print(f"load_user({user_id})")

load_user()
load_user(42)


# ============================================================
# 4. STRING INTERNING & CONTROLLED IDENTITY
# ============================================================
print("\n--- SECTION 4: String Interning ---")

import sys

name1 = "py" + "thon"
name2 = "".join(["py", "thon"])

print("Before interning:", name1 is name2)  # often False

name1 = sys.intern(name1)
name2 = sys.intern(name2)

print("After interning:", name1 is name2)   # guaranteed True

# Interning also speeds up dictionary key comparisons.
symbols = {}
for token in ["for", "if", "else", "for"]:
    token = sys.intern(token)
    symbols[token] = symbols.get(token, 0) + 1
print("symbols dict:", symbols)


# ============================================================
# 5. TYPE OBJECTS AND STRICT IDENTITY CHECKS
# ============================================================
print("\n--- SECTION 5: Type Identity ---")

class Base: ...
class Derived(Base): ...

base = Base()
derived = Derived()

print("type(base) is Base:", type(base) is Base)
print("type(derived) is Base:", type(derived) is Base)         # False
print("isinstance(derived, Base):", isinstance(derived, Base)) # True

# Identity checks are appropriate when subclassing must be rejected.
def must_be_exact_base(obj):
    if type(obj) is not Base:
        raise TypeError("Only Base instances allowed.")
    print("Exact Base accepted.")

must_be_exact_base(base)
try:
    must_be_exact_base(derived)
except TypeError as exc:
    print("Rejected:", exc)


# ============================================================
# 6. DEBUGGING WITH id()
# ============================================================
print("\n--- SECTION 6: Tracking Objects via id() ---")

class Tracker:
    def __init__(self):
        self.history = []

    def remember(self, obj):
        info = (id(obj), type(obj).__name__, repr(obj))
        self.history.append(info)
        print(f"Tracked {info}")

tracker = Tracker()

target = []
alias = target
clone = target.copy()

tracker.remember(target)
tracker.remember(alias)
tracker.remember(clone)

print("\nHistory records show identical IDs only for aliases.")

print("\nLesson complete: 'is' becomes powerful once you inspect aliasing, singletons, and interning mechanics.")
