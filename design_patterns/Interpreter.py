# ==============================================
# Pattern Name: Interpreter
# Pattern Type: Behavioral
# ==============================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   Interpreter defines a tiny rule language using a hierarchy of
#   Expression classes. Each class represents one grammar rule.
#
#   This example interprets simple rule expressions like:
#       "age > 18 AND country == 'MD'"
#
# What Makes It Unique:
#   Interpreter turns each grammar rule (AND, OR, comparison)
#   into its own object. Expression trees evaluate themselves,
#   making the language easy to extend.
# ==============================================


# -----------------------------
# Base Expression
# -----------------------------
class Expression:
    def interpret(self, context):
        raise NotImplementedError


# -----------------------------
# Terminal Expression: Variable
# -----------------------------
# Example: age, country
# -----------------------------
class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

    def interpret(self, context):
        return context[self.name]


# -----------------------------
# Terminal Expression: Literal
# -----------------------------
# Example: 18, 'MD'
# -----------------------------
class LiteralExpression(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


# -----------------------------
# Nonterminal: Comparison
# -----------------------------
# Example: age > 18
# -----------------------------
class GreaterThanExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) > self.right.interpret(context)


class EqualsExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) == self.right.interpret(context)


# -----------------------------
# Nonterminal: Logical AND / OR
# -----------------------------
class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) and self.right.interpret(context)


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) or self.right.interpret(context)


# -----------------------------
# Very Simple Parser
# NOTE:
#   This is intentionally tiny and limited:
#   - Supports only one AND, one OR, and one comparison
#   - Enough to demonstrate the pattern without complexity
# -----------------------------
def parse(rule: str) -> Expression:
    tokens = rule.split()

    # Example: age > 18 AND country == 'MD'
    left_var = VariableExpression(tokens[0])
    operator = tokens[1]
    right_value = tokens[2].strip("'")

    # detect number or string
    if right_value.isdigit():
        right_expr = LiteralExpression(int(right_value))
    else:
        right_expr = LiteralExpression(right_value)

    # Create comparison expression
    if operator == ">":
        expr = GreaterThanExpression(left_var, right_expr)
    elif operator == "==":
        expr = EqualsExpression(left_var, right_expr)
    else:
        raise ValueError("Unsupported operator")

    # Check for AND / OR
    if len(tokens) > 3:
        logical = tokens[3]  # AND / OR
        next_left_var = VariableExpression(tokens[4])
        next_operator = tokens[5]
        next_right = tokens[6].strip("'")

        if next_right.isdigit():
            next_right_expr = LiteralExpression(int(next_right))
        else:
            next_right_expr = LiteralExpression(next_right)

        if next_operator == "==":
            right_comparison = EqualsExpression(next_left_var, next_right_expr)
        else:
            raise ValueError("Unsupported operator")

        if logical == "AND":
            expr = AndExpression(expr, right_comparison)
        elif logical == "OR":
            expr = OrExpression(expr, right_comparison)

    return expr


# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    print("--- Interpreter Pattern Example (Rule Evaluator) ---\n")

    rule = "age > 18 AND country == 'MD'"
    context = {"age": 25, "country": "MD"}

    print("Rule:", rule)
    print("Context:", context)

    tree = parse(rule)
    result = tree.interpret(context)

    print("Result:", result)


# -----------------------------
# Example Output
# -----------------------------
# --- Interpreter Pattern Example (Rule Evaluator) ---
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

