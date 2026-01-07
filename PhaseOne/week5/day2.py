# 🔹 #211
# Merge two dictionaries into one.
# Example: {'a':1,'b':2}, {'b':3,'c':4} → {'a':1,'b':3,'c':4}

dict_a, dict_b = {"a": 1, "b": 2}, {"a": 1, "b": 3, "c": 4}


def merge_dict(dict_a: dict[str, int], dict_b: dict[str, int]):
    return dict_a | dict_b


print(merge_dict(dict_a, dict_b))

# 🔹 #212
# Return list of words that start with a vowel.
# Example: ["apple","tree","orange"] → ["apple","orange"]


def vowel_start(words: list[str]) -> list[str]:
    vowel = "aeiou"
    vowel = set(vowel)

    return [word for word in words if word[0] in vowel]


print(vowel_start(["apple", "tree", "orange"]))


# 🔹 #213
# Given a list of strings, return total number of characters across all strings.
# Example: ["hi","there"] → 7


def ch_count(words: list[str]) -> int:
    return sum([len(word) for word in words])


print(ch_count(["hi", "there"]))

# 🔹 #214
# Check if two strings are anagrams.
# Example: "listen","silent" → True


def is_anagram(word_one: str, word_two: str) -> bool:
    wone_count, wtwo_count = {}, {}
    for ch in word_one:
        wone_count[ch] = wone_count.get(ch, 0) + 1

    for ch in word_two:
        wtwo_count[ch] = wtwo_count.get(ch, 0) + 1

    return wone_count == wtwo_count


print(is_anagram("listen", "silent"))


# 🔹 #215
# Create a dict mapping numbers to their cubes for 1–n.
# Example: n=3 → {1:1,2:8,3:27}


def map_cubes(n: int) -> dict[int, int]:
    return {i: i**3 for i in range(1, n + 1)}


print(map_cubes(3))

# 🔹 #216
# Given a sentence, return the word that appears most often.
# Example: "one fish two fish red fish blue fish" → "fish"


def most_freq_word(sentence: str) -> str:
    sent_arr = sentence.split(" ")
    word_map = {}
    highest = float("-inf")
    most_freq = ""

    for word in sent_arr:
        word_map[word] = word_map.get(word, 0) + 1
        if word_map[word] > highest:
            highest = word_map[word]
            most_freq = word

    return most_freq


print(most_freq_word("one fish two fish red fish blue fish blue blue blue blue blue"))

# 🔹 #217
# Replace all vowels in a string with "*".
# Example: "hello" → "h*ll*"


def replace_vowel(s: str) -> str:
    vowel = set("aeiou")
    s_arr = list(s)

    for i in range(len(s_arr)):
        if s_arr[i] in vowel:
            s_arr[i] = "*"

    return "".join(s_arr)


print(replace_vowel("hello"))

# 🔹 #218
# Sort a list of tuples by their second element.
# Example: [(1,3),(2,2),(3,1)] → [(3,1),(2,2),(1,3)]


def sort_tuple(tuples: list) -> list:
    return sorted(tuples, key=lambda x: x[1])


print(sort_tuple([(1, 3), (2, 2), (3, 1)]))

# 🔹 #219
# Given a list of integers, return True if list is strictly increasing.
# Example: [1,2,3,4] → True


def strictly_inc(nums: list[int]) -> bool:
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


print(strictly_inc([1, 2, 3, 4]))
print(strictly_inc([1, 2, 4, 3]))

# 🔹 #220
# Combine two lists elementwise into a list of tuples.
# Example: [1,2,3],["a","b","c"] → [(1,"a"),(2,"b"),(3,"c")]


def combine_list(arr_n: list[int], arr_s: list[str]) -> list:
    return [(k, v) for k, v in zip(arr_n, arr_s)]


print(combine_list([1, 2, 3], ["a", "b", "c"]))
