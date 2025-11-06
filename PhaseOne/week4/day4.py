# Week 4 — Day 4: Params, *args, **kwargs

# 131
# Write a function that returns a greeting using a name and an optional
# greeting word (default "Hello").
# Example:
# greet("Luna")
# Output: Hello, Luna!
# Example:
# greet("Luna", greeting="Hi")
# Output: Hi, Luna!


def greet(name, greeting="Salutations"):
    return f"{greeting}, {name}!"


print(greet("John"))
print(greet("Paul", "Hello"))

# 132
# Write a function that computes area = width * height, with height
# defaulting to 1.
# Example:
# area(5)
# Output: 5
# Example:
# area(5, 3)
# Output: 15


def area(width, height=1):
    return width * height


print(area(5))
print(area(5, 3))


# 133
# Write a function that takes any number of words via *args and returns
# them joined by a hyphen.
# Example:
# join_words("red", "green", "blue")
# Output: red-green-blue

# 134
# Write a function that returns the product of any count of numbers
# passed via *args. If no numbers are given, return 1.
# Example:
# product(2, 3, 4)
# Output: 24
# Example:
# product()
# Output: 1

# 135
# Write a function that accepts name and age via **kwargs and returns
# "name: <name>, age: <age>".
# Example:
# format_user(name="Mina", age=21)
# Output: name: Mina, age: 21

# 136
# Write a function that accepts a pet name, any number of traits via
# *args, and an optional color via **kwargs (key "color"). Return
# "pet: <pet>, traits: <count>, color: <color_or_unknown>".
# Example:
# describe_pet("buddy", "playful", "small", color="brown")
# Output: pet: buddy, traits: 2, color: brown

# 137
# Write a function that returns a tuple of the first and last items from
# *args. If only one item is given, both elements are that item.
# Example:
# first_last(1, 2, 3, 4)
# Output: (1, 4)
# Example:
# first_last(9)
# Output: (9, 9)

# 138
# Write a function that merges a defaults dict with overrides provided
# via **kwargs. Return the merged dict (kwargs take precedence).
# Example:
# get_config({"a": 1, "b": 2}, b=9, c=7)
# Output: {"a": 1, "b": 9, "c": 7}

# 139
# Write a function that accepts only keyword arguments x and y (y
# defaults to 0) and returns x + y.
# Example:
# add_kw(x=5)
# Output: 5
# Example:
# add_kw(x=5, y=3)
# Output: 8

# 140
# Write a function that returns the number of keyword pairs passed via
# **kwargs.
# Example:
# kwargs_count(a=1, b=2, c=3)
# Output: 3
