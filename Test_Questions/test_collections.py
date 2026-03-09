# duplicates key are not counted, and no error is thrown
print(len({1: "a", 1: "b", 2: "c"}))
# output: 2