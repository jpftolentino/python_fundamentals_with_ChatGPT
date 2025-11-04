# 101
# Create a function that prints "Hello, World!" when called.
# Example: hello()
# Output: Hello, World!


def hello():
    print("Hello, World!")


hello()

# 102
# Write a function that takes a name and prints a personalized greeting.
# Example: greet("Luna")
# Output: Hello, Luna!


def greet(name="Luna"):
    print("Hello,", name)


greet()

# 103
# Write a function that adds two numbers and returns the result.
# Example: add(4, 7)
# Output: 11


def add(x, y):
    return x + y


result = add(4, 7)
print(result)

# 104
# Create a function that takes a number and returns its square.
# Example: square(6)
# Output: 36


def square(s):
    return s * s


resultOne = square(6)
print(resultOne)

# 105
# Write a function that returns the larger of two numbers.
# Example: bigger(10, 25)
# Output: 25


def bigger(a, b):
    return max(a, b)


resultTwo = bigger(10, 25)
print(resultTwo)

# 106
# Write a function that checks if a number is even or odd.
# Example: check_even(7)
# Output: Odd


def check_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


check_even(7)
check_even(8)

# 107
# Define a function that returns the length of a string.
# Example: str_length("Python")
# Output: 6


def str_length(text):
    return len(text)


resultThree = str_length("Python")
print(resultThree)

# 108
# Write a function that takes a list of numbers and returns their sum.
# Example: sum_list([2, 4, 6])
# Output: 12


def sum_list(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


resultFour = sum_list([2, 4, 6])
print(resultFour)

# 109
# Create a function that takes a string and returns it in uppercase.
# Example: to_upper("hello")
# Output: HELLO


def to_upper(word):
    return word.upper()


resultFive = to_upper("hello")
print(resultFive)

# 110
# Function that returns the first and last elements of a list as a tuple.
# Example: ends([10, 20, 30, 40])
# Output: (10, 40)


def ends(nums):
    return (nums[0], nums[-1])


resultSix = ends([10, 20, 30, 40])
print(resultSix)
