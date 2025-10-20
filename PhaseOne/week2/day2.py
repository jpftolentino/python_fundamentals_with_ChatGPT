# 🔹 Day 2 (Problems 61–70: String Checks & Transformations)


#1 Check if a string is a palindrome (case-insensitive).

word = input("Check if a string is a palindrome: ")
word = word.lower()
print(word == word[::-1])

# l = 0
# r = len(word) - 1
# isPalindrome = True

# while l < len(word)//2:
#     if word[l] != word[r]:
#         isPalindrome = False
#         break
#     l += 1
#     r -= 1

# print(isPalindrome)


#2 Count vowels and consonants in a string.

word = input("Enter a string: ").lower()

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

v_count = 0
c_count = 0

for ch in word:

    if not ch.isalpha():
        continue

    if ch in vowels:
        v_count += 1
    elif ch in consonants:
        c_count += 1

print(f"vowels: {v_count}  consonants: {c_count}")


#3 Replace all spaces with underscores.

sentence = input("Please enter a sentece: ")
print(sentence.replace(" ", "_"))


#4 Find the index of the first 'e' in a string.

word = input("Enter a string: ").lower()

for i in range(len(word)):
    if word[i] == 'e':
        print(f"{i} index")


#5 Check if a string contains only digits.

word = input("Enter a string: ")

print(word.isdigit())

#6 Remove all vowels from a string.

word = input("Enter a string: ")
vowels = "aeiouAEIOU"
solution = ""

for ch in word:
    if ch not in vowels:
        solution += ch
    
print(solution)

#7 Split a sentence into words.

sentence = input("Enter a sentence: ")
print(sentence.split(" "))

#8 Join a list of words into a sentence.

print("".join(sentence))

#9 Swap the case of all letters in a string.

print(sentence.swapcase())

#10 Check if two strings are anagrams.

word_one = "listen"
word_two = "silent"

word_one = sorted(word_one)
word_two = sorted(word_two)

print(word_one == word_two)