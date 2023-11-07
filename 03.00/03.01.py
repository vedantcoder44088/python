contains_value = lambda val, group: bool(list(filter(lambda x: x == val, group)))
test_data = {
    3: [1, 5, 8, 3],
    -1: [1, 5, 8, 3]
}

for key, value in test_data.items():
    result = contains_value(key, value)
    print(f"{key} -> {value} : {result}")
