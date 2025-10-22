#🔹 Week 2 — Day 5: Mixed String–List Challenges (Problems 91–100)

# #91
# Convert a string into a list of characters.
# Example: "Python" → ['P', 'y', 't', 'h', 'o', 'n']

text = "Python"
chars = list(text)
print(chars)

# #92
# Convert a list of characters back into a string.
# Example: ['h', 'e', 'l', 'l', 'o'] → "hello"

ch_two = ['h', 'e', 'l', 'l', 'o']
text_two = "".join(ch_two)
print(text_two)

# #93
# Find the longest word in a list of words.
# Example: ["apple", "banana", "cherry"] → "banana"

words = ["apple", "banana", "cherry"]
longest_word = ""

for word in words:
    if len(longest_word) < len(word):
        longest_word = word

print(longest_word)


# #94
# Count how many words in a list start with the letter 'a' (case-insensitive).
# Example: ["apple", "Avocado", "banana", "apricot"] → 3

words_two = ["apple", "Avocado", "banana", "apricot"]
a_count = 0

for word in words_two:
    if 'a' in word.lower()[0]:
        a_count += 1

print(a_count)


# #95
# Sort a list of strings alphabetically.
# Example: ["pear", "apple", "banana"] → ["apple", "banana", "pear"]

words_three = ["pear", "apple", "banana"]
words_three.sort()
print(words_three)

# #96
# Find all words longer than 4 letters in a list.
# Example: ["dog", "tiger", "lion", "cheetah"] → ["tiger", "cheetah"]

words_four = ["dog", "tiger", "lion", "cheetah"]
longer_than_four = []

for word in words_four:
    if len(word) > 4:
        longer_than_four.append(word)

print(longer_than_four)

# #97
# Flatten a 2D list (nested list) into a 1D list.
# Example: [[1, 2], [3, 4]] → [1, 2, 3, 4]

matrix = [[1, 2], [3, 4]]
flatten = []

for sublist in matrix:
    for num in sublist:
        flatten.append(num)

print(flatten)

# #98
# Split a string by commas and trim whitespace from each word.
# Example: "apple, banana , cherry , date" → ["apple", "banana", "cherry", "date"]

text_five = "apple, banana , cherry , date"
words_five = text_five.split(",")

for i in range(len(words_five)):
    words_five[i] = words_five[i].strip()

print(words_five)

# #99
# Join list elements with a hyphen (-) separator.
# Example: ["2025", "10", "14"] → "2025-10-14"

words_six = ["2025", "10", "14"]
text_six = "-".join(words_six)
print(text_six)

# #100
# Remove all empty strings from a list.
# Example: ["apple", "", "banana", "", "cherry"] → ["apple", 
