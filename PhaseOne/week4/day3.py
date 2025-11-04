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


# 123
# Write a function that defines an inner function to add two numbers.
# The outer function should return the result of the inner one.
# Example:
# add_outer(3, 7)
# Output: 10


# 124
# Create a function with an inner function that reverses a string.
# The outer function should return the reversed string.
# Example:
# reverse_outer("Python")
# Output: nohtyP


# 125
# Write a function where an inner function checks if a number is even.
# The outer function should print "Even" or "Odd".
# Example:
# even_check(5)
# Output: Odd


# 126
# Create a function that defines an inner function to count vowels in a
# string, then returns that count from the outer function.
# Example:
# vowel_outer("hello world")
# Output: 3


# 127
# Write a function that defines an inner function for multiplication.
# The outer function should call it with two numbers and return the
# result.
# Example:
# multiply_outer(5, 4)
# Output: 20


# 128
# Define a function that uses a global variable 'counter' and increments
# it by one each time the function is called.
# Example:
# counter = 0
# increment_counter()
# increment_counter()
# Output: counter == 2


# 129
# Write a function that has both local and global variables. Print both
# to show how scope works.
# Example:
# demo_scope()
# Output:
# Local: 10
# Global: 5


# 130
# Create a function with a nested helper function that returns the sum of
# all numbers in a list. The helper should handle the loop.
# Example:
# sum_outer([1, 2, 3, 4])
# Output: 10
