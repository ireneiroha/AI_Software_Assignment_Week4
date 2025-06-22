Used GitHub Copilot.

My code:

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_data = sort_dict_list(data, "age")
print(sorted_data)



GitHub Copilot suggested code:

def sort_dict_list(lst, key):
    return sorted(lst, key=lambda x: x[key])

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_data = sort_dict_list(data, "age")
print(sorted_data)
