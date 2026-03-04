
x_axis_pos = 1
y_axis_pos = 0
z_axis_pos = x_axis_pos ^ y_axis_pos
y_axis_pos = x_axis_pos ^ z_axis_pos
x_axis_pos = y_axis_pos ^ z_axis_pos
print(x_axis_pos, y_axis_pos, z_axis_pos) # Output: 1 0 1, because the XOR operator (^) is used to swap the values without a temporary variable. After the operations, x_axis_pos remains 1, y_axis_pos becomes 0, and z_axis_pos becomes 1.


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

