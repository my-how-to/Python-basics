

counter_step_limit = 10
while counter_step_limit > 0:
    counter_step_limit -= 3

print(counter_step_limit) # Output: 1, because the loop will run 4 times, subtracting 3 each time: 10 -> 7 -> 4 -> 1 -> -2 (loop stops when counter_step_limit is no longer greater than 0).    


list_length_check = [1, 2, 3]
for i in range(len(list_length_check)):
    list_length_check.insert(1, i)
print(list_length_check[2]) # Output: 1, because the loop iterates over the original length of the list (which is 3), and inserts values at index 1. The list evolves as follows:


list_length_check = [10, 20] # length 2
for i in range(len(list_length_check)): # range(2), i.е. i = 0, then i = 1
    list_length_check.insert(1, i)





