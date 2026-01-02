# ============================================================
#            EXERCISE 006 — LEAP YEAR FUNCTIONS
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Write a function that determines whether a year is a leap year.
#   Use the Gregorian rules and test a few examples.
#
# Leap year rules (Gregorian calendar):
#   - divisible by 4  -> leap year
#   - except divisible by 100 -> NOT leap year
#   - except divisible by 400 -> leap year
#
# Why 100 and 400:
#   The 100-year rule removes leap days to fix the Julian drift.
#   The 400-year rule adds some back, slowing the 100-year rule.
#
# Historical background (short):
#   The Gregorian calendar (1582) refined the older Julian system
#   because the solar year is about 365.2422 days, not 365.25.
#   To keep calendars aligned with seasons, we add leap days, but
#   we skip some century years unless they are divisible by 400.
#
# Add two examples:
#   1) A clear step-by-step function
#   2) A shorter version using list comprehension
# ============================================================

print("\n# -----------------------------")
print("# 1. Example 1: function + single year check")
print("# -----------------------------\n")

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

print("1996 ->", is_leap_year(1996))  # True
print("1900 ->", is_leap_year(1900))  # False
print("2000 ->", is_leap_year(2000))  # True


print("\n# -----------------------------")
print("# 2. Example 2: shorter version with list comprehension")
print("# -----------------------------\n")

# Use a compact function and a comprehension to filter a range.

def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
years = list(range(1990, 2035))
leap_years = [y for y in years if is_leap(y)]

print("Years:", years)
print("Leap years:", leap_years)
# Expected: [1992, 1996, 2000, 2004]