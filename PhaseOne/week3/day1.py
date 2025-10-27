# Comprehensive review before week 3

# 🔹 #RN1 — Even & Odd Counter
# counts how many even and odd numbers are in a given list.
# Example:
# nums = [1, 2, 3, 4, 5, 6]
# → Evens: 3, Odds: 3


nums = [1, 2, 3, 4, 5, 6]
evens = 0
odds = 0

for num in nums:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Evens: {evens}, Odds: {odds}")

# 🔹 #RN2 — Reverse Words, Not Letters
# Reverse order of words in a sentence, but keep each word’s letters the same.
# Example:
# text = "Python is fun"
# → "fun is Python"

text = "Python is fun"
text = text.split(" ")
result = ""

for word in reversed(text):
    result += word + " "

print(result[:-1])

# 🔹 #RN3 — Remove Vowels and Reverse
# Remove all vowels from a string, then reverse the result.
# Example:
# text = "education"
# → "ntcd"  (since “education” → “dctn” after removing vowels, then reversed)

text = input("Enter a word: ")
vowels = "aeiou"
result = ""

for ch in text:
    if ch not in vowels:
        result += ch

result = result[::-1]
print(result)
