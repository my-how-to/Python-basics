# ============================================================
#                  LESSON — GENERIC EXCEPT RULES
# ============================================================
# Author: Alexandru Petrenco (with AI assistance from OpenAI GPT-5)
#
# Description:
#   This lesson explains the concept of "generic except" in Python:
#       - what a generic except is
#       - why it's considered dangerous
#       - when it is acceptable to use
#       - how to use it safely
#       - recommended best practices
#       - difference between `except:` and `except Exception:`
#       - catching specific exceptions
#
# Each section prints a separator for clear educational output.
# ============================================================


# ============================================================
# 1. WHAT IS A GENERIC EXCEPT?
# ============================================================

print("\n--- SECTION 1: What is a Generic Except? ---")

try:
    x = 10 / 0
except:
    print("Caught an error (generic except)")

# This catches ALL exceptions, including system interrupts.
# It hides what type of error occurred.


# ============================================================
# 2. WHY GENERIC EXCEPT IS DANGEROUS
# ============================================================

print("\n--- SECTION 2: Why Generic Except Is Dangerous ---")

nums = [1, 2, 3]

try:
    print(nums[10])      # IndexError
except:
    print("Error hidden — program continues")  # hides real bugs

# Generic except blocks real debugging.
# You cannot see what went wrong.
# It also catches KeyboardInterrupt and SystemExit accidentally.


# ============================================================
# 3. DANGEROUS BEHAVIOR: CATCHING KEYBOARD INTERRUPT
# ============================================================

print("\n--- SECTION 3: Dangerous Behavior (KeyboardInterrupt) ---")

print("NOTE: The following example is *demonstrative* and will NOT be run here.\n"
      "It shows why `except:` is dangerous in real programs.\n")

code_example = """
try:
    while True:
        pass
except:
    print("You cannot stop this with Ctrl+C — dangerous!")
"""
print(code_example)


# ============================================================
# 4. SAFE VERSION OF GENERIC CATCH: except Exception
# ============================================================

print("\n--- SECTION 4: Safe Alternative — except Exception ---")

try:
    value = int("abc")   # ValueError
except Exception as e:
    print("Caught safely:", type(e).__name__)

# except Exception catches all NORMAL runtime errors,
# but does NOT catch:
#   - KeyboardInterrupt
#   - SystemExit
#   - GeneratorExit
# This is MUCH safer.


# ============================================================
# 5. BEST PRACTICE: CATCH ONLY WHAT YOU EXPECT
# ============================================================

print("\n--- SECTION 5: Best Practice — Catch Specific Errors ---")

try:
    items = [1, 2, 3]
    print(items[5])
except IndexError:
    print("Handled IndexError correctly")

# This is the cleanest and safest method.
# Catch only the error types you expect.


# ============================================================
# 6. CATCHING MULTIPLE SPECIFIC EXCEPTIONS
# ============================================================

print("\n--- SECTION 6: Multiple Specific Exceptions ---")

try:
    data = {"age": "22"}
    age = int(data["agee"])   # KeyError due to typo
except (ValueError, KeyError) as e:
    print("Handled:", type(e).__name__)

# Useful when you know precisely which errors might occur.


# ============================================================
# 7. TOP-LEVEL HANDLER: GOOD USE OF EXCEPT Exception
# ============================================================

print("\n--- SECTION 7: Top-Level Application Error Handling ---")

def run_app():
    x = 1 / 0   # will raise ZeroDivisionError

try:
    run_app()
except Exception as e:
    print("Top-level handler caught:", type(e).__name__)
    print("Application shutting down cleanly.")

# Top-level catch is acceptable for:
#   - CLI tools
#   - GUIs
#   - Web service entry points
#   - Any place you want graceful shutdown


# ============================================================
# 8. LOGGING BEFORE RE-RAISING
# ============================================================

print("\n--- SECTION 8: Logging Before Re-Raising ---")

def process():
    return 10 / 0

try:
    process()
except Exception as e:
    print("LOG:", type(e).__name__, "-", e)
    raise   # re-raise the exception after logging

# Re-raising keeps the stack trace intact.


# ============================================================
# 9. SUPPRESSING ONLY SAFE ERRORS (CLOSE OPERATIONS)
# ============================================================

print("\n--- SECTION 9: Suppressing Only Safe Errors ---")

class FakeConnection:
    def close(self):
        raise RuntimeError("Connection already closed")

conn = FakeConnection()

try:
    conn.close()
except Exception:
    pass   # allowed in cleanup code — closing should never crash

print("Program continues safely after cleanup.")


# ============================================================
# 10. SUMMARY OF RULES
# ============================================================

print("\n--- SECTION 10: Summary of Rules ---")
print("""
BAD:
    except:
        pass

AVOID:
    except:
        print("Error")

GOOD:
    except SpecificError:
        handle_it()

ACCEPTABLE:
    except Exception as e:
        log_and_recover(e)

ADVANCED & RIGHT:
    except Exception as e:
        log(e)
        raise
""")
