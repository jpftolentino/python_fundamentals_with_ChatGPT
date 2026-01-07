# 🔹 Week 4 — Day 5: Recursion (Problems 191–200)

# #191
# Write a recursive function that sums all numbers from 1 to n.
# Example: 5 → 15  (1+2+3+4+5)


def sum_nums(n: int) -> int:
    if n == 1:
        return 1

    return n + sum_nums(n - 1)


print(sum_nums(5) == 15)

# #192
# Write a recursive function to compute factorial of n.
# Example: 5 → 120


def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5) == 120)


# #193
# Write a recursive function to reverse a string.
# Example: "python" → "nohtyp"


def reverse_str(text: str) -> str:
    if len(text) == 1:
        return text[0]

    return reverse_str(text[1:]) + text[0]


print(reverse_str("python"))


# #194
# Write a recursive function that counts down from n to 1.
# Example: n=3 → 3 2 1


def count_down(n: int) -> None:
    if n == 1:
        return print(n)

    print(n)

    return count_down(n - 1)


count_down(3)


# #195
# Write a recursive function to compute the nth Fibonacci number.
# Example: n=6 → 8


def find_fibn(n: int) -> int:
    if n <= 1:
        return n

    return find_fibn(n - 1) + find_fibn(n - 2)


print(find_fibn(6))


# #196
# Write a recursive function to find the maximum in a list.
# Example: [3, 1, 4, 2] → 4


def find_max(nums: list[int]) -> int:
    index = len(nums) - 1

    def helper(nums: list[int], index: int) -> int:
        if index == 0:
            return nums[index]

        return max(helper(nums, index - 1), nums[index])

    return helper(nums, index)


print(find_max([3, 1, 4, 2]))


# #197
# Write a recursive function that returns True if a word is a palindrome.
# Example: "level" → True

# reversing the string recursively and then comparing
# def is_palindrome(s: str) -> bool:
#     def helper(s: str, index: int) -> str:
#         if index == len(s) - 1:
#             return s[index]
#
#         return helper(s, index + 1) + s[index]
#
#     reversed_str = helper(s, 0)
#
#     return reversed_str == s


# two pointer recursion -> this is really cool not gonna lie
def is_palindrome(s, left: int = 0, right: int | None = None) -> bool:
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False

    return is_palindrome(s, left + 1, right - 1)


print(is_palindrome("level"))
print(is_palindrome("python"))

# #198
# Write a recursive function that calculates the sum of digits of a number.
# Example: 1234 → 10


def sum_digits(n: int) -> int:
    if n == 0:
        return 0

    return sum_digits(int(n / 10)) + (n % 10)


print(sum_digits(1234))


# #199
# Write a recursive function to count how many times a target appears in a list.
# Example: ([1, 2, 3, 2], 2) → 2


def count_freq(nums: list[int], target: int, index: int = 0) -> int:
    if index == len(nums):
        return 0

    return (1 if nums[index] == target else 0) + count_freq(nums, target, index + 1)


print(count_freq([1, 2, 3, 2], 2))

# #200
# Write a recursive function to flatten a nested list.
# Example: [1, [2, [3, 4]], 5] → [1, 2, 3, 4, 5]
#


def flatten_list(data):
    flat = []
    for item in data:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


print(flatten_list([1, [2, [3, 4]], 5]))
