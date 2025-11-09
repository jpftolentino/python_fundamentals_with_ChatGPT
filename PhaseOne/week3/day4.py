# 🔹 Week 3 — Day 4: Dictionaries & Sets (Problems 131–140)

# #131
# Write a function that returns a greeting using a name and an optional
# greeting word (default "Hello").
# Input: greet("Luna"), greet("Luna", "Hi")
# Output: "Hello, Luna!", "Hi, Luna!"


def greet(name, greet="Hello"):
    return print(f"{greet}, {name}!")


greet("Luna")
greet("Luna", "Hi")


# #132
# Merge two dictionaries using a function and return the result.
# Input: {'a':1, 'b':2}, {'b':3, 'c':4}
# Output: {'a':1, 'b':3, 'c':4}

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}


def merge_dict(a, b):
    return a | b


print(merge_dict(dict_a, dict_b))


# #133
# Create a function that inverts a dictionary (values become keys).
# Input: {'a':1, 'b':2, 'c':3}
# Output: {1:'a', 2:'b', 3:'c'}

dict_three = {"a": 1, "b": 2, "c": 3}
swapped = {}


def invert_dict(dict):
    return {v: k for k, v in dict.items()}


swapped = invert_dict(dict_three)
print(swapped)


# #134
# Return the intersection of keys between two dictionaries.
# Input: {'x':1,'y':2}, {'y':3,'z':4}
# Output: {'y'}

dict_c = {"x": 1, "y": 2}
dict_d = {"y": 3, "z": 4}


def dict_intersect(c, d):
    return c.keys() & d.keys()


print(dict_intersect(dict_c, dict_d))


# #135
# Return the union of keys between two dictionaries.
# Input: {'x':1,'y':2}, {'y':3,'z':4}
# Output: {'x','y','z'}

dict_e, dict_f = {"x": 1, "y": 2}, {"y": 3, "z": 4}


def union_dict(e, f):
    return e.keys() | f.keys()


print(union_dict(dict_e, dict_f))


# #136
# Given a dictionary, remove keys with values less than 10.
# Input: {'a':5, 'b':12, 'c':8, 'd':15}
# Output: {'b':12, 'd':15}

dict_g = {"a": 5, "b": 12, "c": 8, "d": 15}
removed = {}


def remove_keys(dict):
    return {k: v for k, v in dict.items() if v >= 10}


removed = remove_keys(dict_g)

print(removed)

# #137
# Create a dictionary mapping words to their lengths.
# Input: ['hi', 'there', 'you']
# Output: {'hi':2, 'there':5, 'you':3}

words = ["hi", "there", "you"]
words_length = {}


def ch_count(words):
    return {word: len(word) for word in words}


words_length = ch_count(words)

print(words_length)


# #138
# Combine two lists into a dictionary but ignore duplicate keys.
# Input: ['a','b','b'], [1,2,3]
# Output: {'a':1, 'b':2}

key_l, val_l = ["a", "b", "b"], [1, 2, 3]


def combine(keys, vals):
    new_dict = {}
    for key, value in zip(keys, vals):
        if key not in new_dict:
            new_dict[key] = value

    return new_dict


print(combine(key_l, val_l))

# #139
# Count how many keys in a dictionary have even values.
# Input: {'a':2, 'b':3, 'c':6}
# Output: 2

dict_i = {"a": 2, "b": 3, "c": 6}


def count_even(dict):
    # count = 0
    # for val in dict.values():
    #     if val % 2 == 0:
    #         count += 1
    # return count

    return sum(1 for val in dict.values() if val % 2 == 0)


print(count_even(dict_i))


# #140
# Create a set containing all unique characters from a list of strings.
# Input: ['hi','hello']
# Output: {'h','i','e','l','o'}

text_two = ["hi", "hello"]


def unique_chars(text):
    return set("".join(text))


print(unique_chars(text_two))
