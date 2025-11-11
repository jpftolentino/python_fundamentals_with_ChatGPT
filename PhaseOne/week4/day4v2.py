# 🔹 Week 4 — Day 4: List & Dict Comprehensions
# Problems 181–190

# #181
# Create a list of squares from 1 to 5 using a comprehension.
# Example: → [1, 4, 9, 16, 25]

squares = [x * x for x in range(1, 6)]

print(squares)


# #182
# From a list of numbers, create a new list containing only even numbers.
# Example: [1, 2, 3, 4, 5, 6] → [2, 4, 6]

nums_two = [1, 2, 3, 4, 5, 6]

even = [x for x in nums_two if x % 2 == 0]

print(even)


# #183
# Given a list of words, return a list of their lengths.
# Example: ["hi", "hello", "hey"] → [2, 5, 3]

list_three = ["hi", "hello", "hey"]

ch_count = [len(x) for x in list_three]

print(ch_count)


# #184
# Create a list of uppercase versions of each string in a list.
# Example: ["cat", "dog"] → ["CAT", "DOG"]

list_four = ["cat", "dog"]

to_upper = [word.upper() for word in list_four]

print(to_upper)


# #185
# From a list of words, keep only those with length > 3.
# Example: ["hi", "python", "is", "fun"] → ["python", "fun"]

list_five = ["hi", "python", "is", "fun"]

only_three = [word for word in list_five if len(word) >= 3]

print(only_three)


# #186
# Build a dictionary of squares from 1 to 4.
# Example: → {1: 1, 2: 4, 3: 9, 4: 16}

dict_squares = {v: v * v for v in range(1, 5)}

print(dict_squares)


# #187
# Given two lists, combine them into a dictionary using comprehension.
# Example: ["a", "b"], [1, 2] → {"a": 1, "b": 2}

list_seven_a, list_seven_b = ["a", "b"], [1, 2]

combine_dict = {a: b for a, b in zip(list_seven_a, list_seven_b)}

print(combine_dict)


# #188
# Invert a dictionary’s keys and values using comprehension.
# Example: {"a": 1, "b": 2} → {1: "a", 2: "b"}

dict_eight = {"a": 1, "b": 2}

invert_dict = {v: k for k, v in dict_eight.items()}

print(invert_dict)


# #189
# From a dictionary of scores, keep only entries ≥ 70.
# Example: {"Ann": 80, "Bob": 65} → {"Ann": 80}

scores = {"Ann": 80, "Bob": 65}

seventy_plus = {k: v for k, v in scores.items() if v >= 70}

print(seventy_plus)


# #190
# Given a string, make a dict of each char and its count.
# Example: "level" → {"l": 2, "e": 2, "v": 1}

text_ten = "level"
# count_ch = {}
#
# for ch in text_ten:
#     count_ch[ch] = count_ch.get(ch, 0) + 1

count_ch = {ch: text_ten.count(ch) for ch in set(text_ten)}
# We turn the string into a set because we don't want to count the ch twice

print(count_ch)
