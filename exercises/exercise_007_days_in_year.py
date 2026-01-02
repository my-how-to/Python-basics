# ============================================================
#            EXERCISE 007 — DAYS IN A MONTH
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Exercise:
#   Calculate the number of days in a month for several test cases.
#   Reuse the leap-year function from exercise_006_leap_years.py.
# ============================================================

from exercise_006_leap_years import is_leap_year  # run this file from the exercises folder


def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


test_cases = [
    (1900, 2),
    (1999, 2),
    (2000, 2),
    (2004, 2),
    (2100, 2),
    (2023, 4),
    (2023, 7),
]

for year, month in test_cases:
    print(f"{year}-{month:02d} -> {days_in_month(year, month)}")

# Expected:
# 1900-02 -> 28
# 1999-02 -> 28
# 2000-02 -> 29
# 2004-02 -> 29
# 2100-02 -> 28
# 2023-04 -> 30
# 2023-07 -> 31
