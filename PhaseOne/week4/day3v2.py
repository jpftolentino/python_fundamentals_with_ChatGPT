# 🔹 Week 4 — Day 3: Lambda + map, filter, zip, enumerate
# Problems 171–180

# #171
# Use map() with a lambda to square all numbers.
# Example: [1, 2, 3, 4] → [1, 4, 9, 16]

list_one = [1, 2, 3, 4]

square = map(lambda x: x * x, list_one)

print(list(square))


# #172
# Use filter() with a lambda to keep only even numbers.
# Example: [1, 2, 3, 4, 5, 6] → [2, 4, 6]

list_two = [1, 2, 3, 4, 5, 6]

evens = filter(lambda x: x % 2 == 0, list_two)

print(list(evens))


# #173
# Use map() and filter() together to triple only odd numbers.
# Example: [1, 2, 3, 4] → [3, 9]

list_three = [1, 2, 3, 4]

triple_odd = map(lambda y: y * 3, filter(lambda x: x % 2 != 0, list_three))

print(list(triple_odd))


# #174
# Combine two lists using zip() and make tuples of (name, age).
# Example: ["A", "B"], [20, 25] → [("A", 20), ("B", 25)]

name = ["A", "B"]
age = [20, 25]

print(list(zip(name, age)))


# #175
# Given two lists of equal length, sum corresponding elements
# using map() and lambda.
# Example: [1, 2, 3], [4, 5, 6] → [5, 7, 9]

nums_a, nums_b = [1, 2, 3], [4, 5, 6]

total = map(lambda x, y: x + y, nums_a, nums_b)

print(list(total))


# #176
# Use enumerate() to print index and element for a list of words.
# Example: ["alpha", "beta"] → 0: alpha, 1: beta

words = ["alpha", "beta"]

for i, word in enumerate(words):
    print(f"{i}: {word}")


# #177
# Use map() and str.upper to convert all words to uppercase.
# Example: ["cat", "dog"] → ["CAT", "DOG"]

words_two = ["cat", "dog"]

to_upper = map(str.upper, words_two)

print(list(to_upper))


# #178
# Use filter() with lambda to remove empty strings from a list.
# Example: ["a", "", "b", "", "c"] → ["a", "b", "c"]

letters = ["a", "", "b", "", "c"]

remove_empty = filter(None, letters)

print(list(remove_empty))


# #179
# Use zip() to combine two lists, then convert to a dict.
# Example: ["x", "y"], [10, 20] → {"x": 10, "y": 20}

ch_list, nums_list = ["x", "y"], [10, 20]

print(dict(zip(ch_list, nums_list)))


# #180
# Given a list of numbers, use enumerate() to make tuples
# of (index, number^2).
# Example: [2, 3, 4] → [(0, 4), (1, 9), (2, 16)]

nums_nine = [2, 3, 4]
result_nine = []

for i, num in enumerate(nums_nine):
    temp = (i, num**2)
    result_nine.append(temp)

# list(enumerate((n*n for n in nums_nine)))

print(result_nine)
