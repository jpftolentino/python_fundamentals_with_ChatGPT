from typing import List, Dict

# 🔹 Week 3 — Day 5: Dictionaries & Sets (Problems 141–150)

# #141
# Create a dictionary from two lists but skip any None values.
# Input: ['a', 'b', None], [1, 2, 3]
# Output: {'a':1, 'b':2}

list_one, list_two = ["a", "b", None], [1, 2, 3]


def create_dict(l_one, l_two):
    return {k: v for k, v in zip(l_one, l_two) if k is not None}


print(create_dict(list_one, list_two))


# #142
# Given a dictionary, find the average of all its values.
# Input: {'a':4, 'b':6, 'c':8}
# Output: 6.0

grades = {"a": 4, "b": 6, "c": 8}


def average(d):
    return sum(d.values()) / len(d)


print(average(grades))


# #143
# Count how many unique values are in a dictionary.
# Input: {'a':1, 'b':2, 'c':1, 'd':3}
# Output: 3

dict_three = {"a": 1, "b": 2, "c": 1, "d": 3}


def count_unique(d):
    count_set = set(d.values())
    return len(count_set)


print(count_unique(dict_three))

# #144
# Combine two lists into a dictionary, keeping only unique keys.
# Input: ['a','b','a'], [1,2,3]
# Output: {'a':1, 'b':2}

list_three, list_four = ["a", "b", "a"], [1, 2, 3]


def merge_list(l_three: List[str], l_four: List[int]) -> Dict[str, int]:
    merged = {}
    for key, val in zip(l_three, l_four):
        if key not in merged:
            merged[key] = val

    return merged


print(merge_list(list_three, list_four))


# #145
# Create a set of all even numbers from a list.
# Input: [1, 2, 3, 4, 5, 6]
# Output: {2, 4, 6}

nums_five = [1, 2, 3, 4, 5, 6]


def even_set(nums: List[int]) -> set:
    return set(n for n in nums if n % 2 == 0)


print(even_set(nums_five))

# #146
# Given a list of words, create a dictionary mapping the first letter
# to all words starting with that letter.
# Input: ['apple', 'ant', 'bat']
# Output: {'a':['apple','ant'], 'b':['bat']}

words_six = ["apple", "ant", "bat"]


def dict_mapping(words: List[str]) -> Dict[str, List]:
    group_words = {}
    for word in words:
        first = word[0]
        group_words.setdefault(first, []).append(word)
    return group_words


print(dict_mapping(words_six))

# #147
# Remove all keys from a dictionary whose values are duplicates.
# Input: {'a':1, 'b':2, 'c':1}
# Output: {'b':2}

dict_seven = {"a": 1, "b": 2, "c": 1}


def remove_duplicate_keys(d: Dict[str, int]) -> Dict[str, int]:
    group = {}
    for key, val in d.items():
        group.setdefault(val, []).append(key)

    return {v[0]: k for k, v in group.items() if len(v) == 1}


print(remove_duplicate_keys(dict_seven))


# #148
# Given two lists, return a dictionary of items only present in both.
# Input: ['a','b','c'], ['b','c','d']
# Output: {'b':None,'c':None}

list_five, list_six = ["a", "b", "c"], ["b", "c", "d"]


def present_in_both(l_five: List[str], l_six: List[str]) -> Dict[str, None]:
    a, b = set(l_five), set(l_six)
    intersect = a & b
    return {ch: None for ch in intersect}


print(present_in_both(list_five, list_six))

# #149
# Create a dictionary of squares for numbers 1–5,
# but only include odd numbers.
# Input: N/A
# Output: {1:1, 3:9, 5:25}


def dict_squares() -> Dict[int, int]:
    return {n: n**2 for n in range(1, 6) if n % 2 != 0}


print(dict_squares())

# #150
# Given a list of names, count how many start with each letter.
# Input: ['Alice','Bob','Amy','Brian']
# Output: {'A':2, 'B':2}

names = ["Alice", "Bob", "Amy", "Brian"]


def categ_names(names: List[str]) -> Dict[str, int]:
    group = {}
    for name in names:
        first = name[0]
        group.setdefault(first, []).append(name)

    return {k: len(v) for k, v in group.items()}


print(categ_names(names))
