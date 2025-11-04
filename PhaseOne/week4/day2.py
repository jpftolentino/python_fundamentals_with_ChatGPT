# Week 3 — Day 2: Return Values, Scope & Default Parameters
# Mini Lesson

# 111
# Write a function that returns the cube of a number.
# Example: cube(3)
# Output: 27


def cube(num):
    return num * num * num


result = cube(3)
print(result)

# 112
# Create a function that returns True if a number is positive, and False
# otherwise.
# Example: is_positive(-5)
# Output: False


def is_positive(num):
    if num > 0:
        return True
    elif num < 0:
        return False
    else:
        return "Zero"


print(is_positive(-5))

# 113
# Write a function that takes two strings and returns the longer one.
# Example: longer("cat", "elephant")
# Output: elephant


def longer(text_one, text_two):
    if len(text_one) > len(text_two):
        return text_one
    else:
        return text_two


print(longer("cat", "elephant"))

# 114
# Define a function that returns the sum of all even numbers in a list.
# Example: sum_evens([1, 2, 3, 4, 5, 6])
# Output: 12


def sum_evens(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total


print(sum_evens([1, 2, 3, 4, 5, 6]))

# 115
# Write a function that counts how many vowels are in a given string.
# Example: count_vowels("Python is fun")
# Output: 3


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


print(count_vowels("Python is fun"))

# 116
# Create a function that returns True if a word is a palindrome, False
# otherwise.
# Example: is_palindrome("level")
# Output: True


def is_palindrome(text):
    return text == text[::-1]


print(is_palindrome("level"))

# 117
# Write a function that takes a number and a power (default 2) and returns
# the result of the exponent.
# Example 1: power(5)
# Output: 25
# Example 2: power(2, 3)
# Output: 8


def power(num, ex=2):
    return num**ex


print(power(2, 3))
print(power(5))

# 118
# Define a function that takes a list and returns a new list with each
# number doubled.
# Example: double_list([1, 2, 3])
# Output: [2, 4, 6]


def double_list(nums):
    for i in range(0, len(nums)):
        nums[i] = nums[i] * 2
    return nums


print(double_list([1, 2, 3]))

# 119
# Create a function that returns the factorial of a given number using a
# loop.
# Example: factorial(5)
# Output: 120


def factorial(num):
    total = 1
    if num > 1:
        for num in range(2, num + 1):
            total *= num
    else:
        return 1
    return total


print(factorial(5))

# 120
# Write a function that accepts a list and a target value, returning True
# if found, False if not.
# Example: contains([3, 6, 9], 6)
# Output: True


def contains(nums, target):
    for num in nums:
        if num == target:
            return True
    return False


print(contains([3, 6, 9], 6))
print(contains([3, 6, 9], 10))
