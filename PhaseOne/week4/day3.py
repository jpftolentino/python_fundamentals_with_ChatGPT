# Week 3 — Day 3: Nested Functions & Variable Scope

# 121
# Write a function 'outer' that defines an inner function printing
# "Inner function called!" and then calls it.
# Example:
# outer()
# Output: Inner function called!


def outer():
    def inner():
        print("Inner function called!")

    inner()


outer()

# 122
# Create a function that defines another function to square a number,
# then calls it inside the main function.
# Example:
# outer_square(4)
# Output: 16


def outer_square(num):
    def square(num):
        return num * num

    return square(num)


print(outer_square(4))

# 123
# Write a function that defines an inner function to add two numbers.
# The outer function should return the result of the inner one.
# Example:
# add_outer(3, 7)
# Output: 10


def add_outer(a, b):
    def add(x, y):
        return x + y

    return add(a, b)


print(add_outer(3, 7))

# 124
# Create a function with an inner function that reverses a string.
# The outer function should return the reversed string.
# Example:
# reverse_outer("Python")
# Output: nohtyP


def reverse_outer(text):
    def reverse(text):
        return text[::-1]

    return reverse(text)


print(reverse_outer("Python"))

# 125
# Write a function where an inner function checks if a number is even.
# The outer function should print "Even" or "Odd".
# Example:
# even_check(5)
# Output: Odd


def even_check(num):
    def is_even(num):
        if num % 2 == 0:
            return "Even"
        else:
            return "Odd"

    return is_even(num)


print(even_check(5))

# 126
# Create a function that defines an inner function to count vowels in a
# string, then returns that count from the outer function.
# Example:
# vowel_outer("hello world")
# Output: 3


def vowel_outer(text):
    vowels = "aeiou"

    def count_vowel(text, vowels):
        count = 0
        for ch in text:
            if ch in vowels:
                count += 1
        return count

    return count_vowel(text, vowels)


print(vowel_outer("hello world"))

# 127
# Write a function that defines an inner function for multiplication.
# The outer function should call it with two numbers and return the
# result.
# Example:
# multiply_outer(5, 4)
# Output: 20


def multiply_outer(a, b):
    def multiply(a, b):
        return a * b

    return multiply(a, b)


print(multiply_outer(5, 4))

# 128
# Define a function that uses a global variable 'counter' and increments
# it by one each time the function is called.
# Example:
# counter = 0
# increment_counter()
# increment_counter()
# Output: counter == 2


counter = 0


def increment_counter():
    global counter
    counter += 1


increment_counter()
increment_counter()
print(counter)

# 129
# Write a function that has both local and global variables. Print both
# to show how scope works.
# Example:
# demo_scope()
# Output:
# Local: 10
# Global: 5


global_val = 5


def demo_scope():
    local_val = 10
    print("Local:", local_val)
    print("Global:", global_val)


demo_scope()

# 130
# Create a function with a nested helper function that returns the sum of
# all numbers in a list. The helper should handle the loop.
# Example:
# sum_outer([1, 2, 3, 4])
# Output: 10


def sum_outer(nums):
    def sum_inner(nums):
        total = 0

        for num in nums:
            total += num
        return total

    return sum_inner(nums)


print(sum_outer([1, 2, 3, 4]))
