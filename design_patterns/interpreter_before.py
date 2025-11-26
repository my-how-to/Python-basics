# ==============================================
# BEFORE — Interpreter Pattern
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Before the Interpreter pattern existed, rule evaluation was
#   implemented manually using string splitting, many IF/ELSE
#   statements, and procedural parsing logic.
#
#   This example evaluates a tiny rule language:
#       "age > 18 AND country == 'MD'"
#
#   The logic works, but it is tightly coupled, hard to extend,
#   and difficult to maintain as soon as more rules or operators
#   are added.
# ==============================================


# -----------------------------
# BEFORE: Manual Rule Evaluator
# -----------------------------
# Supported:
#   - variable > number
#   - variable == string
#   - AND operator
#
# Example rule:
#     "age > 18 AND country == 'MD'"
#
# Limitations:
#   - Adding OR, >=, <=, parentheses, or nested rules becomes messy.
#   - Parsing logic and evaluation logic are mixed together.
# -----------------------------
def evaluate_rule(rule: str, context: dict) -> bool:
    tokens = rule.split()
    # Example: ['age', '>', '18', 'AND', 'country', '==', "'MD'"]

    # Evaluate first comparison
    left_var = tokens[0]
    operator = tokens[1]
    right_value = tokens[2].strip("'")

    # Convert number if needed
    if right_value.isdigit():
        right_value = int(right_value)

    # First comparison result
    if operator == ">":
        result = context[left_var] > right_value
    elif operator == "==":
        result = context[left_var] == right_value
    else:
        raise ValueError("Unsupported operator")

    # If no AND part → return result
    if "AND" not in tokens:
        return result

    # Process AND right-hand side
    and_index = tokens.index("AND")

    next_left = tokens[and_index + 1]
    next_op = tokens[and_index + 2]
    next_right = tokens[and_index + 3].strip("'")

    # Convert number if needed
    if next_right.isdigit():
        next_right = int(next_right)

    if next_op == "==":
        second = context[next_left] == next_right
    elif next_op == ">":
        second = context[next_left] > next_right
    else:
        raise ValueError("Unsupported operator")

    # Only AND supported in this BEFORE version
    return result and second


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- BEFORE Interpreter Example (Rule Evaluator) ---\n")

    rule = "age > 18 AND country == 'MD'"
    context = {"age": 25, "country": "MD"}

    print("Rule:", rule)
    print("Context:", context)

    result = evaluate_rule(rule, context)
    print("Result:", result)


# -----------------------------
# Example Output
# -----------------------------
# --- BEFORE Interpreter Example (Rule Evaluator) ---
# Rule: age > 18 AND country == 'MD'
# Context: {'age': 25, 'country': 'MD'}
# Result: True
#
#
# ==============================================
# History
# ==============================================
# The Interpreter pattern grew out of early work in
# symbolic languages such as Smalltalk and Lisp (1970s–1980s),
# where developers often needed to evaluate small rule-based
# expressions such as:
#     - logical conditions
#     - symbolic expressions (Lisp S-expressions)
#     - workflow or configuration rules
#     - mini query languages
#
# Before the pattern existed, these small languages were
# implemented using large, procedural functions full of
# if/else statements. The parsing logic, evaluation logic,
# and grammar structure were all mixed together, which made
# extension difficult.
#
# Interpreter formalized the idea of mapping each grammar
# rule to a separate class that knows how to interpret itself.
# This gave structure to early rule engines and tiny DSLs
# (domain-specific languages). The GoF book (1994) helped
# popularize the pattern as a way to build flexible and
# extensible mini-languages.
# ==============================================
