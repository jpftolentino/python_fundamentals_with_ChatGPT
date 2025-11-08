# 🔹 Week 3 — Day 3: Dictionaries & Sets (Problems 121–130)

# #121
# Combine two lists into a dictionary using zip().
# Input: ['a', 'b', 'c'], [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

ch = ["a", "b", "c"]
nums = [1, 2, 3]
dict_one = {}

for c, n in zip(ch, nums):
    dict_one[c] = n

print(dict_one)


# #122
# Get all keys from a dictionary as a list.
# Input: {'x': 10, 'y': 20, 'z': 30}
# Output: ['x', 'y', 'z']

dict_two = {"x": 10, "y": 20, "z": 30}
solution_two = []

# for key in dict_two.keys():
#     solution_two.append(key)

solution_two = list(dict_two.keys())

print(solution_two)


# #123
# Get all values from a dictionary as a list.
# Input: {'x': 10, 'y': 20, 'z': 30}
# Output: [10, 20, 30]

solution_three = []

# for value in dict_two.values():
#     solution_three.append(value)

solution_three = list(dict_two.values())

print(solution_three)


# #124
# Create a dictionary from a string counting each letter.
# Input: "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}

text = "banana"
solution_four = {}

for ch in text:
    solution_four[ch] = solution_four.get(ch, 0) + 1

print(solution_four)


# #125
# Swap keys and values in a dictionary.
# Input: {'a': 1, 'b': 2, 'c': 3}
# Output: {1: 'a', 2: 'b', 3: 'c'}

dictionary_five = {"a": 1, "b": 2, "c": 3}
swapped = {}

# for key, val in dictionary_five.items():
#     swapped[val] = key

swapped = {v: k for k, v in dictionary_five.items()}

print(swapped)

# #126
# Find the key with the maximum value.
# Input: {'x': 5, 'y': 9, 'z': 3}
# Output: 'y'

dictionary_six = {"x": 5, "y": 9, "z": 3}
solution_six = float("-inf")
answer = ""

for key, val in dictionary_six.items():
    if val > solution_six:
        solution_six = val
        answer = key

alternative_solution = max(dictionary_six, key=lambda k: dictionary_six[k])

print(alternative_solution)

# #127
# Merge multiple dictionaries into one.
# Input: {'a': 1}, {'b': 2}, {'c': 3}
# Output: {'a': 1, 'b': 2, 'c': 3}

d_one, d_two, d_three = {"a": 1}, {"b": 2}, {"c": 3}

dictionary_seven = d_one | d_two | d_three

print(dictionary_seven)

# #128
# Remove duplicate values from a dictionary.
# Input: {'a': 1, 'b': 2, 'c': 1}
# Output: {'a': 1, 'b': 2}

dictionary_eight = {"a": 1, "b": 2, "c": 1}
unique_dict = {}

for key, value in dictionary_eight.items():
    if value not in unique_dict.values():
        unique_dict[key] = value

print(unique_dict)


# #129
# Create a dictionary where keys are numbers and values are their squares.
# Input: [1, 2, 3, 4]
# Output: {1: 1, 2: 4, 3: 9, 4: 16}

nums = [1, 2, 3, 4]

dictionary_nine = {n: n**2 for n in nums}

print(dictionary_nine)


# #130
# Count how many times each word appears in a list.
# Input: ['cat', 'dog', 'cat', 'bird']
# Output: {'cat': 2, 'dog': 1, 'bird': 1}
#
words = ["cat", "dog", "cat", "bird"]
count_words = {}

for word in words:
    count_words[word] = count_words.get(word, 0) + 1

print(count_words)
