x = {"data": {"val": 10}}
y = x.copy()
y["data"] = {"val": 50}
print(x)
print(y)
print(x["data"]["val"])

x = {"data": {"val": 10}}
y = x.copy()
y["data"]['val'] = 50
print(x)
print(y)
print(x["data"]["val"])

first = {"meta": {"id": 100}}
second = first.copy()

print(second)
second["meta"].update({"id": 200})

print(first)
print(second)


print(first["meta"]["id"])

original = {"alpha": 1}
cloned = original.copy()
print(original is cloned)

items = {"milk": 1, "bread": 2}
removed_value = items.pop("milk", 0)
print(removed_value)

counters = {"clicks": 5, "views": 10}
for key in counters:
    if key == "clicks":
        counters[key] = counters[key] + 2
print(counters["clicks"])