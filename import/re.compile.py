# ============================================================
#            LESSON — REGULAR EXPRESSIONS & RE.COMPILE
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from Google Gemini)
#
# Description:
#   This lesson explains what regular expressions (Regex) are,
#   how their syntax works, and how to use the re.compile 
#   function in Python for efficient text processing.
#
# Contents:
#   1. What is a Regular Expression (Regex)?
#   2. Basic Regex Syntax (The Cheat Sheet)
#   3. What is re.compile?
#   4. Basic syntax and creating Regex objects
#   5. re.compile() vs Inline Regex (re.search)
#   6. Reusing patterns for performance
#   7. Using compilation flags (re.IGNORECASE, etc.)
#   8. Common Regex object methods (.match, .findall, .finditer)
#   9. Practical mini-examples
# ============================================================

import re

# ------------------------------------------------------------
# 1. WHAT IS A REGULAR EXPRESSION (REGEX)?
# ------------------------------------------------------------
# A Regular Expression (shortened as "Regex" or "Regexp") is 
# a powerful tool for searching, matching, and manipulating text 
# based on defined patterns. 
#
# Think of standard search (Ctrl+F) as looking for a SPECIFIC word 
# (e.g., "apple"). Regex is looking for a RULE or PATTERN 
# (e.g., "any word that starts with 'a', has 5 letters, and ends in 'e'").


# ------------------------------------------------------------
# 2. BASIC REGEX SYNTAX (THE CHEAT SHEET)
# ------------------------------------------------------------
# To build patterns, Regex uses special characters (metacharacters):
# 
#  \d  -> Any single digit (0-9)
#  \w  -> Any alphanumeric character (letter, digit, or underscore)
#  \s  -> Any whitespace (space, tab, newline)
#  .   -> Any character except a newline
#  +   -> Matches 1 or more repetitions of the preceding character
#  *   -> Matches 0 or more repetitions of the preceding character
#  {3} -> Matches exactly 3 repetitions (e.g., \d{3} means 3 digits)
#  \b  -> Word boundary (defines where a word starts or ends)


print("\n------------------------------------------------------------")
print("3. WHAT IS RE.COMPILE?")
print("------------------------------------------------------------\n")

# re.compile is a function from the built-in 're' module. It takes 
# a raw regex pattern string and compiles it into a reusable 
# "Regex Object". This makes future searches significantly faster.


print("\n------------------------------------------------------------")
print("4. BASIC SYNTAX & CREATING REGEX OBJECTS")
print("------------------------------------------------------------\n")

# Step 1: Compile a pattern (looking for 3 digits in a row)
# We use raw strings (r"...") to avoid escaping backslashes in Python
digit_pattern = re.compile(r"\d{3}")

text = "The secret code is 456 and 789."

# Step 2: Use the compiled object to search the text
result = digit_pattern.search(text)

print(f"Compiled Object Type: {type(digit_pattern).__name__}")
print(f"Search Result:        {result}")
print(f"Found Value:          {result.group()}")


# ------------------------------------------------------------
# 5. RE.COMPILE() VS INLINE REGEX
# ------------------------------------------------------------
# You can use regex without re.compile, but compiling is cleaner.
#
# Inline approach (Python compiles the string every time):
# re.search(r"\d{3}", text)
#
# Compiled approach (Python compiles once, reuses many times):
# pattern = re.compile(r"\d{3}")
# pattern.search(text)


print("\n------------------------------------------------------------")
print("6. REUSING PATTERNS FOR PERFORMANCE")
print("------------------------------------------------------------\n")

# If you need to search the same pattern in thousands of lines,
# re.compile saves CPU cycles because it avoids recompiling.
email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

user_emails = ["user1@test.com", "invalid_email", "admin@company.org"]

print("Filtering valid emails with a reused pattern:")
for email in user_emails:
    if email_pattern.match(email):
        print(f" -> VALID:   {email}")
    else:
        print(f" -> INVALID: {email}")


# ------------------------------------------------------------
# 7. USING COMPILATION FLAGS
# ------------------------------------------------------------
# re.compile allows you to pass modifiers (flags) as a second 
# argument to change how the pattern behaves.
#
# Common flags:
# * re.IGNORECASE (re.I) -> Makes the pattern case-insensitive.
# * re.MULTILINE  (re.M) -> Affects ^ and $ anchors for newlines.
# * re.DOTALL     (re.S) -> Makes the dot (.) match newlines too.


print("\n------------------------------------------------------------")
print("8. COMMON REGEX OBJECT METHODS")
print("------------------------------------------------------------\n")

# Let's create a pattern to find words starting with 'p'
p_word_pattern = re.compile(r"\bp\w+", re.IGNORECASE)
sample_text = "Python is a powerful programming language."

# .findall() returns a list of strings
all_words = p_word_pattern.findall(sample_text)
print(f"findall() result: {all_words}")

# .finditer() returns an iterator yielding Match objects (gives positions)
print("finditer() positions:")
for match in p_word_pattern.finditer(sample_text):
    print(f" -> Found '{match.group()}' at positions {match.span()}")


print("\n------------------------------------------------------------")
print("9. PRACTICAL MINI-EXAMPLES")
print("------------------------------------------------------------\n")

# Real-world task: Redacting sensitive data (phone numbers) from logs
phone_pattern = re.compile(r"\+\d{1,3}-\d{3}-\d{3}-\d{4}")

log_data = "User Alice logged in. Contact: +1-555-123-4567. IP: 192.168.1.1"

# .sub() replaces matched patterns with a replacement string
clean_log = phone_pattern.sub("[REDACTED PHONE]", log_data)

print(f"Original Log: {log_data}")
print(f"Cleaned Log:  {clean_log}")
