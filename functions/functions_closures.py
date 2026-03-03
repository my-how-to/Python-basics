# ==========================================================
#                       CLOSURES
# ==========================================================
#
# 1) WHAT IS A CLOSURE?
#
# A closure is a function object that:
# - is defined inside another function
# - remembers variables from the outer (enclosing) scope
# - even after the outer function has finished executing
#
# Key idea:
# A closure "closes over" its surrounding state.
#
# ==========================================================
# 2) BASIC STRUCTURE
# ==========================================================
#
# def outer():
#     x = value
#
#     def inner():
#         use x
#
#     return inner
#
# inner() forms a closure over x.
#
# ==========================================================
# 3) SIMPLE EXAMPLE
# ==========================================================

def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


func = outer()
func()  
# Output: Hello

#
# Even though outer() has finished,
# inner() still remembers "message".
#

# ==========================================================
# 4) WHY DOES THIS WORK?
# ==========================================================
#
# Because Python stores the variable in a special place:
# → function.__closure__
#
# The inner function keeps a reference to variables
# from the enclosing scope.
#

def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()

print(f.__closure__)
# Shows cell object storing x

# ==========================================================
# 5) CLOSURE WITH PARAMETERS
# ==========================================================

def multiplier(n):

    def multiply(x):
        return x * n

    return multiply


double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

#
# Here:
# double remembers n = 2
# triple remembers n = 3
#

# ==========================================================
# 6) IMPORTANT RULES
# ==========================================================
#
# For a closure to exist:
#
# 1) Nested function
# 2) Inner function references outer variable
# 3) Outer function returns inner function
#
# If inner does not use outer variable → no closure.
#

# ==========================================================
# 7) nonlocal KEYWORD
# ==========================================================
#
# If you want to MODIFY the outer variable,
# you must use nonlocal.

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())  # 1
print(c())  # 2
print(c())  # 3

#
# Without nonlocal → UnboundLocalError
#

# ==========================================================
# 8) HOW CLOSURES DIFFER FROM GLOBALS
# ==========================================================
#
# Closures:
# - Encapsulated state
# - No global variables
# - Cleaner and safer design
#
# Globals:
# - Shared everywhere
# - Harder to control
#

# ==========================================================
# 9) PRACTICAL USE CASES
# ==========================================================
#
# - Function factories
# - Data hiding
# - Decorators
# - Maintaining state without classes
#

# Example: simple function factory

def power_factory(exp):
    def power(x):
        return x ** exp
    return power

square = power_factory(2)
cube = power_factory(3)

print(square(4))   # 16
print(cube(4))     # 64


# ==========================================================
# 10) CLOSURE VS CLASS
# ==========================================================
#
# Closure:
# - Lightweight
# - Functional style
#
# Class:
# - More explicit structure
# - Better for complex state
#

# Equivalent class example:

class Multiplier:
    def __init__(self, n):
        self.n = n

    def multiply(self, x):
        return x * self.n


m = Multiplier(2)
print(m.multiply(5))   # 10


# ==========================================================
# 11) KEY RULES
# ==========================================================
#
# - A closure remembers variables from outer scope.
# - Works even after outer function returns.
# - Uses function.__closure__ internally.
# - Use nonlocal to modify enclosed variables.
# - Frequently used in decorators.
#
# ==========================================================
# END OF LESSON
# ==========================================================