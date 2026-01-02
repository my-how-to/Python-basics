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


print("\n# -----------------------------")
print("# Days in a month (function)")
print("# -----------------------------\n")

# Function to get days in a month, considering leap years for February.

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


print("\n# -----------------------------")
print("# Day of year (function)")
print("# -----------------------------\n")

# Calculate the day of the year given year, month, day.
def day_of_year(year, month, day):
    # validate month
    if month < 1 or month > 12:
        return None

    # validate day
    if day < 1 or day > days_in_month(year, month):
        return None

    # sum days in previous months, then add the current day
    total = 0
    for m in range(1, month):
        total += days_in_month(year, m)
    return total + day

print(day_of_year(2000, 1, 30)) # 30
print(day_of_year(2000, 4, 29))  # 120
print(day_of_year(2001, 16, 1))  # None (invalid month)
print(day_of_year(2001, 10, 32))  # None (invalid day)
