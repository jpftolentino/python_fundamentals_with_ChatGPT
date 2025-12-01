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

# 🔹 #223
# Given a list of dicts, extract all unique keys into a set.
# Example: [{'a':1}, {'b':2,'c':3}] → {'a','b','c'}

# 🔹 #224
# Return a list of words whose length is greater than 4.
# Example: ["cat","house","window","bat"] → ["house","window"]

# 🔹 #225
# Given a dict of items and prices, return the item with the highest price.
# Example: {'apple':2,'banana':5,'pear':3} → 'banana'

# 🔹 #226
# Create a list of tuples (word, length) from a given string.
# Example: "hi there you" → [('hi',2),('there',5),('you',3)]

# 🔹 #227
# Invert a dictionary (swap keys and values).
# Example: {'a':1,'b':2} → {1:'a',2:'b'}

# 🔹 #228
# Filter a dictionary to include only items with values greater than 10.
# Example: {'a':5,'b':15,'c':8} → {'b':15}

# 🔹 #229
# Given a list of lists, return a list of their sums.
# Example: [[1,2,3],[4,5],[6]] → [6,9,6]

# 🔹 #230
# Combine two lists of equal length into a dictionary but ignore any
# None values in the keys list.
# Example: ['a',None,'c'],[1,2,3] → {'a':1,'c':3}
