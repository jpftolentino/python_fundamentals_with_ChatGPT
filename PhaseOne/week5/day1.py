# 🔹 #201
# Count how many elements in a list are greater than the average.
# Example: [2, 4, 6, 8] → 2


def count_num(nums: list) -> int:
    average = sum([num for num in nums]) / len(nums)

    return sum([1 for num in nums if num > average])


print(count_num([2, 4, 6, 8]))

# 🔹 #202
# Return list of squares for even numbers only.
# Example: [1, 2, 3, 4] → [4, 16]


def square_even(nums: list) -> list:
    return [num * num for num in nums if num % 2 == 0]


print(square_even([1, 2, 3, 4]))


# 🔹 #203
# Make a dict mapping each word to its length.
# Example: "we love python" → {'we':2,'love':4,'python':6}


def word_map(words: str) -> dict[str, int]:
    words_arr = words.split()
    return {k: len(k) for k in words_arr}


print(word_map("we love python"))


# 🔹 #204
# Flatten a 2D list into 1D.
# Example: [[1,2],[3,4]] → [1,2,3,4]


def flatten(data: list[list]) -> list:
    flat = []
    for item in data:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


print(flatten([[1, 2], [3, 4]]))

# 🔹 #205
# Return all numbers that appear exactly once.
# Example: [1,2,2,3,4,4] → [1,3]


def unique_num(nums: list) -> list:
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1
    return [k for k, v in num_map.items() if v == 1]


print(unique_num([1, 2, 2, 3, 4, 4]))

# 🔹 #206
# Remove duplicates and sort list descending.
# Example: [3,1,3,2,2] → [3,2,1]


def dedupe_sort(nums: list) -> list:
    return sorted(set(nums), reverse=True)


print(dedupe_sort([3, 1, 3, 2, 2]))

# 🔹 #207
# Combine two lists into dict of index:value pairs.
# Example: ['a','b'],[1,2] → {'a':1,'b':2}


def create_dict(arr_str: list[str], arr_num: list[int]) -> dict:
    return {k: v for k, v in zip(arr_str, arr_num)}


print(create_dict(["a", "b"], [1, 2]))

# 🔹 #208
# Reverse each string in list.
# Example: ["hi","bye"] → ["ih","eyb"]


def reverse_words(words: list[str]) -> list[str]:
    reverse_arr = []
    for word in words:
        reverse_arr.append(word[::-1])

    return reverse_arr


print(reverse_words(["hi", "bye"]))


# 🔹 #209
# Create dict counting how many times each char appears.
# Example: "banana" → {'b':1,'a':3,'n':2}


def char_count(word: str) -> dict[str, int]:
    ch_count = {}
    for ch in word:
        ch_count[ch] = ch_count.get(ch, 0) + 1
    return ch_count


print(char_count("banana"))


# 🔹 #210
# Filter out all falsy values from list.
# Example: [0,1,"",None,5] → [1,5]
#


def remove_falsy(data: list):
    return [x for x in data if x]


print(remove_falsy([0, 1, "", None, 5]))
