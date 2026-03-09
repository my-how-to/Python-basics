
# closure
def outer_func_call(x_val):
    def inner_func_call(y_val):
        return x_val + y_val
    return inner_func_call

closure_instance = outer_func_call(10)
print("closure_instance: ", closure_instance(5)) # 15 


print(type(print))