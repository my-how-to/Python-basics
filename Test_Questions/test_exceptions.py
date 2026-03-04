# what will be printed?
try:
    val_num = int("10.5") # This will raise a ValueError because "10.5" is not a valid integer string.
except ValueError:
    print("Wrong value for int()")
except:
    print("other")


# what will be returned?
def test_val():
    try:
        return 1 # This will be returned if there are no exceptions. However, since there are no exceptions in this code, it will return 1.
    finally:
        return 2 # This will override the previous return statement, so the function will always return 2.

print("Return override: ", test_val()) # Output: 2, because the finally block's return statement overrides the try block's return statement.
# it ovverrides because the finally block is guaranteed to execute, and its return value takes precedence over any previous return statements in the try block.



try:
    raise Exception("Critical")
except BaseException:
    print("A")
except Exception:
    print("B")