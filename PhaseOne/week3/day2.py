# 🔹 Week 3 — Day 2: Dictionaries & Sets (Problems 111–120)

# #111
# Create a set of unique numbers from a list.
# Input: [1, 2, 2, 3, 1, 4]
# Output: {1, 2, 3, 4}

unique_num = set([1, 2, 2, 3, 1, 4])

print(unique_num)


# #112
# Add a new element to a set.
# Input: {1, 2, 3}, element = 4
# Output: {1, 2, 3, 4}

set_one = set([1, 2, 3])
set_one.add(4)

print(set_one)


# #113
# Remove an element from a set if it exists.
# Input: {1, 2, 3, 4}, remove 3
# Output: {1, 2, 4}

set_one.discard(3)

print(set_one)


# #114
# Check if an element exists in a set.
# Input: {1, 2, 3}, check 5
# Output: False

print(5 in set_one)


# #115
# Find the union of two sets.
# Input: {1, 2}, {2, 3}
# Output: {1, 2, 3}

set_two = set([1, 2])
set_three = set([2, 3])

print(set_two | set_three)


# #116
# Find the intersection of two sets.
# Input: {1, 2, 3}, {2, 3, 4}
# Output: {2, 3}

set_four = set([1, 2, 3])
set_five = set([2, 3, 4])

print(set_four & set_five)


# #117
# Find the difference between two sets.
# Input: {1, 2, 3}, {2, 3, 4}
# Output: {1}

set_six = set([1, 2, 3])
set_seven = set([2, 3, 4])

print(set_six - set_seven)


# #118
# Check if one set is a subset of another.
# Input: {1, 2}, {1, 2, 3}
# Output: True

set_eight = set([1, 2])
set_nine = set([1, 2, 3])

print(set_eight <= set_nine)


# #119
# Convert a string into a set of unique characters.
# Input: "hello"
# Output: {'h', 'e', 'l', 'o'}

text = input("Enter a word: ")
set_ch = set(text)
print(set_ch)


# #120
# Get the number of unique items in a list using a set.
# Input: [1, 2, 2, 3, 4, 4]
# Output: 4

nums = [1, 2, 2, 3, 4, 4]
len_set = len(set(nums))
print(len_set)
