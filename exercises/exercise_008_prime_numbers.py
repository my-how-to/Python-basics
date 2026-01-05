# ============================================================
#            EXERCISE 008 — PRIME NUMBERS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Write two functions that check if a number is prime:
#   1) A slow version (check all numbers).
#   2) A faster version (check up to the square root).
# ============================================================


print("\n# -----------------------------")
print("# Prime check (slow version)")
print("# -----------------------------\n")


# Slow prime check: try every divisor from 2 to n-1.
def is_prime_slow(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False

    return True


for n in range(1, 21):
    if is_prime_slow(n):
        print(n, end=" ")
print()  # end with a newline


print("\n# -----------------------------")
print("# Prime check (square root)")
print("# -----------------------------\n")


# Why sqrt(n) works:
# - Divisors come in pairs: (a * b = n).
# - If a is greater than sqrt(n), then b must be smaller than sqrt(n).
# - So if no divisor <= sqrt(n) is found, no larger one can exist either.
# - For perfect squares, sqrt(n) is an exact divisor, so include it.

# Faster prime check: test divisors only up to sqrt(n).
def is_prime_sqrt(n):
    if n < 2:
        return False

    limit = int(n ** 0.5)
    for divisor in range(2, limit + 1):
        if n % divisor == 0:
            return False
    return True


for n in range(1, 21):
    if is_prime_sqrt(n):
        print(n, end=" ")
print()  # end with a newline

n = 5
limit = int(n ** 0.5) 
n % 10 == 3
