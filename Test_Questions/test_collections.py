print("Dictionary practice")

# duplicates key are not counted, and no error is thrown
print("duplicates key", len({1: "a", 1: "b", 2: "c"}))
# output: 2

# key True is rewritten by key 1, and the value associated with key True is now "no".
flags = {True: "yes", 1: "no"}
print(flags) # output: {True: 'no'}
print(flags[True])
# output: no

basket = {"orange": 5}
basket.pop("orange", 0)
res = basket.pop("orange", -1) 
# output: -1


low_caps = ["a", "b"]
upper_dict = {k.upper(): k for k in low_caps}
print("A" in upper_dict)
# output: True

inventory = {"gold": 100, "iron": 50, "wood": 10}
res = ""
for item in sorted(inventory):
    res += item[0]
print(res)
# output: "giw"

info = {"name": "Alice"}
info.update([("age", 20), ("city", "NY")])
print(len(info), info)
# output: 3 {'name': 'Alice', 'age': 20, 'city': 'NY'}
