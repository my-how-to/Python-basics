

# What is the output?
x = 10
x += x == 10
print(x) # Output: 11, because x == 10 is True (which is 1), so x += 1 adds 1 to x, resulting in 11.

# This demonstrates that the result of a comparison (True or False) can be used in arithmetic operations, where True is treated as 1 and False is treated as 0.
x = 10
x += x == 5
print(x) # Output: 10, because x == 5 is False (which is 0), so x += 0 does not change x, leaving it at 10.

# This demonstrates that the result of a comparison (True or False) can be used in arithmetic operations, where True is treated as 1 and False is treated as 0.
flag_val = True
count_val = 10
count_val += flag_val # count_val += 1, because flag_val is True (which is 1), so count_val becomes 11.
print(count_val)



try:
    val_num = int("10.5") # This will raise a ValueError because "10.5" is not a valid integer string.
except ValueError:
    print("Wrong value for int()")
except:
    print("other")

def test_val():
    try:
        return 1 # This will be returned if there are no exceptions. However, since there are no exceptions in this code, it will return 1.
    finally:
        return 2 # This will override the previous return statement, so the function will always return 2.

print("Return override: ", test_val()) # Output: 2, because the finally block's return statement overrides the try block's return statement.
# it ovverrides because the finally block is guaranteed to execute, and its return value takes precedence over any previous return statements in the try block.


def outer_func_call(x_val):
    def inner_func_call(y_val):
        return x_val + y_val
    return inner_func_call

closure_instance = outer_func_call(10)
print("closure_instance: ", closure_instance(5)) # 15 


counter_step_limit = 10
while counter_step_limit > 0:
    counter_step_limit -= 3

print(counter_step_limit) # Output: 1, because the loop will run 4 times, subtracting 3 each time: 10 -> 7 -> 4 -> 1 -> -2 (loop stops when counter_step_limit is no longer greater than 0).    

x_axis_pos = 1
y_axis_pos = 0
z_axis_pos = x_axis_pos ^ y_axis_pos
y_axis_pos = x_axis_pos ^ z_axis_pos
x_axis_pos = y_axis_pos ^ z_axis_pos
print(x_axis_pos, y_axis_pos, z_axis_pos) # Output: 1 0 1, because the XOR operator (^) is used to swap the values without a temporary variable. After the operations, x_axis_pos remains 1, y_axis_pos becomes 0, and z_axis_pos becomes 1.

list_length_check = [1, 2, 3]
for i in range(len(list_length_check)):
    list_length_check.insert(1, i)
print(list_length_check[2]) # Output: 1, because the loop iterates over the original length of the list (which is 3), and inserts values at index 1. The list evolves as follows:

list_length_check = [10, 20] # длина 2
for i in range(len(list_length_check)): # range(2), т.е. i = 0, затем i = 1
    list_length_check.insert(1, i)

