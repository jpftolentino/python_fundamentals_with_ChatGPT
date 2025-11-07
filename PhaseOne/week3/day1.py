# 🔹 Week 3 — Day 1: Dictionaries & Sets (Problems 101–110)

# #101
# Create a dictionary of three fruits and their prices.
# Input: N/A
# Output: {'apple': 1.2, 'banana': 0.8, 'mango': 1.5}

fruits = {"apple": 1.2, "banana": 0.8, "mango": 1.5}

print(fruits)


# #102
# Access the price of 'banana' from the dictionary.
# Input: 'banana'
# Output: 0.8

print(fruits["banana"])


# #103
# Add a new fruit 'orange' with its price.
# Input: 'orange', 1.1
# Output: {'apple':1.2, 'banana':0.8, 'mango':1.5, 'orange':1.1}

fruits["orange"] = 1.1

print(fruits)


# #104
# Check if 'grape' exists in the dictionary.
# Input: 'grape'
# Output: False

print("grape" in fruits)


# #105
# Loop through fruit names only.
# Input: {'apple':1.2,'banana':0.8,'mango':1.5}
# Output: apple banana mango

for key in fruits:
    print(key)


# #106
# Loop through fruit names and prices together.
# Input: {'apple':1.2,'banana':0.8}
# Output: apple 1.2
#         banana 0.8

for key, value in fruits.items():
    print(key, value)


# #107
# Get all fruit prices as a list.
# Input: {'apple':1.2,'banana':0.8,'mango':1.5}
# Output: [1.2, 0.8, 1.5]

prices = []

for key, value in fruits.items():
    prices.append(value)

print(prices)


# #108
# Remove 'banana' from the dictionary.
# Input: 'banana'
# Output: {'apple':1.2,'mango':1.5}

fruits.pop("banana")

print(fruits)


# #109
# Merge two dictionaries.
# Input: {'a':1,'b':2}, {'b':3,'c':4}
# Output: {'a':1,'b':3,'c':4}

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
merged_dict = {**dict_a, **dict_b}

print(merged_dict)

# #110
# Count occurrences of numbers in a list using a dictionary.
# Input: [1, 2, 2, 3, 1]
# Output: {1:2, 2:2, 3:1}

nums = [1, 2, 2, 3, 1]

count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

print(count)
