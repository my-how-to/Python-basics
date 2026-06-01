# ============================================================
#            LESSON — THE JSON.LOADS FUNCTION
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from Google Gemini)
#
# Description:
#   This lesson explains the json.loads function in Python: 
#   what it is, basic syntax, differences from json.load(), 
#   and handling common data types and conversion errors.
#
# Contents:
#   1. What is json.loads?
#   2. Basic syntax and string parsing
#   3. json.loads() vs json.load()
#   4. Data types mapping (JSON to Python)
#   5. Handling JSONDecodeError with try-except
#   6. Parsing nested JSON structures
#   7. Practical mini-examples
# ============================================================

import json

# ------------------------------------------------------------
# 1. WHAT IS JSON.LOADS?
# ------------------------------------------------------------
# json.loads (stands for "load string") is a function from the 
# built-in 'json' module. It takes a text string formatted as 
# JSON and converts (deserializes) it into a Python dictionary, 
# list, or other native Python data types.


print("\n------------------------------------------------------------")
print("2. BASIC SYNTAX & STRING PARSING")
print("------------------------------------------------------------\n")

# A valid JSON must use double quotes for strings inside
json_string = '{"name": "Alex", "age": 28, "is_student": false}'

# Converting JSON string to Python dictionary
user_dict = json.loads(json_string)

print(f"Original string type: {type(json_string).__name__}")
print(f"Parsed object type:   {type(user_dict).__name__}")
print(f"Resulting dictionary: {user_dict}")
print(f"Accessing data:       User name is {user_dict['name']}")


# ------------------------------------------------------------
# 3. JSON.LOADS() VS JSON.LOAD()
# ------------------------------------------------------------
# * json.loads() -> The 's' stands for STRING. It parses raw text.
# * json.load()  -> No 's'. It reads directly from a FILE object.
#
# Example of difference (Concept only):
# data = json.loads('{"id": 1}')       <- Parses text directly
# data = json.load(open("data.json"))  <- Parses file stream


# ------------------------------------------------------------
# 4. DATA TYPES MAPPING (JSON TO PYTHON)
# ------------------------------------------------------------
# Python automatically translates JSON data types to its own:
#
# JSON Type          Python Type      Example Conversion
# ---------          -----------      ------------------
# object      --->   dict             {"a": 1}  ->  {'a': 1}
# array       --->   list             [1, 2]    ->  [1, 2]
# string      --->   str              "hello"   ->  'hello'
# number      --->   int / float      5 / 3.14  ->  5 / 3.14
# true/false  --->   True/False       true      ->  True
# null        --->   None             null      ->  None


print("\n------------------------------------------------------------")
print("5. HANDLING JSONDECODEERROR WITH TRY-EXCEPT")
print("------------------------------------------------------------\n")

# This JSON is invalid because it uses single quotes internally
invalid_json = "{'name': 'Alex', 'age': 28}"

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as error:
    print("Parsing failed! JSON requires double quotes for strings.")
    print(f"Error message: {error}")


print("\n------------------------------------------------------------")
print("6. PARSING NESTED JSON STRUCTURES")
print("------------------------------------------------------------\n")

nested_json = '''
{
    "company": "TechCorp",
    "employees": [
        {"name": "Alice", "role": "Dev"},
        {"name": "Bob", "role": "Designer"}
    ]
}
'''

data = json.loads(nested_json)
print(f"Company: {data['company']}")
# Accessing the second employee's role from the nested list
print(f"Bob's Role: {data['employees'][1]['role']}")


print("\n------------------------------------------------------------")
print("7. PRACTICAL MINI-EXAMPLES")
print("------------------------------------------------------------\n")

# Real-world task: Parsing API response text into total balance
api_response = '{"status": "success", "transactions": [100.50, -20.00, 50.00]}'

parsed_response = json.loads(api_response)
transactions = parsed_response["transactions"]
total_balance = sum(transactions)

print(f"Parsed Transactions: {transactions}")
print(f"Calculated Total Balance: {total_balance}")
