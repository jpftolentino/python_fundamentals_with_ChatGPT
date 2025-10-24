# 🔹 Basics & Control Flow
# R1. Check if a number is even or odd.
# Example: 7 → odd

# number = int(input("Enter a number: "))
#
# if number % 2 != 0:
#     print("odd")
# else:
#     print("even")

# R2. Print all numbers from 1 to 10 except multiples of 3.
# Example: Output → 1 2 4 5 7 8 10

# for num in range(1, 11):
#     if num % 3 != 0:
#         print(num)

# R3. Given a number, print whether it’s positive, negative, or zero.
# Example: -5 → negative

# number = int(input("Enter a number: "))
#
# if number == 0:
#     print("zero")
# elif number > 0:
#     print("positive")
# else:
#     print("negative")

# R4. Write a loop that sums all numbers from 1 to n.
# Example: n = 5 → 15

# n = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, n + 1):
#     sum += i
#
# print(sum)

# R5. Check if a number is a multiple of 5 and 7.
# Example: 35 → True

# n = int(input("Enter a number: "))
#
# if n % 5 == 0 and n % 7 == 0:
#     print("True")
# else:
#     print("False")

# 🔹 Strings & Lists

# R6. Reverse a string manually (no slicing).
# Example: "Python" → "nohtyP"

# word = "Python"
# text = list(word)
# solution = ""
#
# for ch in range(len(text) - 1, -1, -1):
#     solution += text[ch]
#
# print(solution)

# R7. Count how many vowels are in a given string.
# Example: "education" → 5

# R8. Replace every space in a string with a dash (-).
# Example: "hello world" → "hello-world"

# R9. Find the largest number in a list.
# Example: [5, 9, 2, 8] → 9

# R10. Remove duplicates from a list while keeping order.
# Example: [1, 2, 2, 3, 1] → [1, 2, 3]
