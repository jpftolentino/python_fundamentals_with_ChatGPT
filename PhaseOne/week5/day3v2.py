# 🔹 #221
# Given a list of dictionaries with 'name' and 'age' keys, return the
# average age.
# Example: [{'name':'A','age':20},{'name':'B','age':30}] → 25.0


def avg_age(data: list[dict]) -> float:
    total = 0
    for item in data:
        for key, value in item.items():
            if key == "age":
                total += value
    return total / len(data)


print(avg_age([{"name": "A", "age": 20}, {"name": "B", "age": 30}]))


# 🔹 #222
# Convert a dictionary of lists into a list of dictionaries.
# Example: {'a':[1,2], 'b':[3,4]} → [{'a':1,'b':3}, {'a':2,'b':4}]


def list_of_dict(data: dict[str, list]) -> list[dict]:
    keys = list(data.keys())
    values_zipped = zip(*data.values())
    return [dict(zip(keys, vals)) for vals in values_zipped]


print(list_of_dict({"a": [1, 2], "b": [3, 4]}))

# 🔹 #223
# Given a list of dicts, extract all unique keys into a set.
# Example: [{'a':1}, {'b':2,'c':3}] → {'a','b','c'}


def extract_unique_keys(data: list[dict]) -> set:
    unique_keys = set()
    for item in data:
        for key in item.keys():
            unique_keys.add(key)

    return unique_keys


print(extract_unique_keys([{"a": 1}, {"b": 2, "c": 3}]))

# 🔹 #224
# Return a list of words whose length is greater than 4.
# Example: ["cat","house","window","bat"] → ["house","window"]


def greater_four(words: list[str]) -> list[str]:
    return [word for word in words if len(word) > 4]


print(greater_four(["cat", "house", "window", "bat"]))

# 🔹 #225
# Given a dict of items and prices, return the item with the highest price.
# Example: {'apple':2,'banana':5,'pear':3} → 'banana'


def highest_price(data: dict[str, int]) -> str:
    return max(data, key=lambda k: data[k])


print(highest_price({"apple": 2, "banana": 5, "pear": 3}))

# 🔹 #226
# Create a list of tuples (word, length) from a given string.
# Example: "hi there you" → [('hi',2),('there',5),('you',3)]


def list_of_tuples(text: str) -> list[tuple]:
    word_arr = text.split(" ")
    return [(word, len(word)) for word in word_arr]


print(list_of_tuples("hi there you"))

# 🔹 #227
# Invert a dictionary (swap keys and values).
# Example: {'a':1,'b':2} → {1:'a',2:'b'}


def invert_dict(data: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in data.items()}


print(invert_dict({"a": 1, "b": 2}))

# 🔹 #228
# Filter a dictionary to include only items with values greater than 10.
# Example: {'a':5,'b':15,'c':8} → {'b':15}


def greater_ten(data: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in data.items() if v > 10}


print(greater_ten({"a": 5, "b": 15, "c": 8}))

# 🔹 #229
# Given a list of lists, return a list of their sums.
# Example: [[1,2,3],[4,5],[6]] → [6,9,6]


def sum_of_lists(data: list) -> list:
    return [sum(nums) for nums in data]


print(sum_of_lists([[1, 2, 3], [4, 5], [6]]))

# 🔹 #230
# Combine two lists of equal length into a dictionary but ignore any
# None values in the keys list.
# Example: ['a',None,'c'],[1,2,3] → {'a':1,'c':3}


def combined_list(arr_one: list, arr_two: list) -> dict:
    return {k: v for k, v in zip(arr_one, arr_two) if k}


print(combined_list(["a", None, "c"], [1, 2, 3]))
