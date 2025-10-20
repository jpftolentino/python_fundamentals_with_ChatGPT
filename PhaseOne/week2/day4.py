#🔹 Day 4: Loops & List Transformations (Problems 81–90)

#1 Print each element of a list using a for loop.

# list_one = ["apple", 1, "truck", False, -1]

# for i in range(len(list_one)):
#     print(list_one[i])


#2 Square each element of a list and print the new list.

# nums = [1, 2, 3, 4, 5, 6]

# for num in nums:
#     print(num * num)


#3 Filter out even numbers from a list (keep only odd numbers).

# nums_two = [1, 2, 3, 4, 5, 6, 7, 8]

# for num in nums_two:
#     if num % 2 != 0:
#         print(num)


#4 Count how many odd numbers are in a list.

# nums_three = [1, 2, 3, 4, 5, 6, 7, 8]
# count = 0

# for num in nums_three:
#     if num % 2 != 0:
#         count += 1

# print(count)

#5 Double all elements greater than 5 in a list.

# nums_four = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in range(len(nums_four)):
#     if nums_four[i] > 5:
#         nums_four[i] = nums_four[i] * 2

# print(nums_four)


#6 Reverse a list manually (without using .reverse() or slicing [::-1]).

nums = [1, 2, 3, 4, 5]
nums_reversed = []

for i in range(len(nums) - 1, -1, -1):
    nums_reversed.append(nums[i])

print(nums_reversed)

# In place reverse
# for i in range(len(nums) // 2):
#     nums[i], nums[-i - 1] = nums[-i - 1], nums[i]


#7 Check if a list is a palindrome (the same forward and backward).

nums = [1, 2, 3, 2, 1]
is_palindrome = True
l = 0
r = len(nums) - 1

for i in range(len(nums)//2):
    if nums[l] != nums[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1

print(is_palindrome)


#8 Merge two lists into one.

list_a = ["hello", "world", "salutations"]
list_b = [1, 2, 3]
#creates a new list
new_list = list_a + list_b
#in place solution
#list_a.extend(list_b)

print(new_list)


#9 Remove duplicates from a list (keep only unique elements).

list_duplicate_val = [1, 1, 2, 2, 3, 3]
no_duplicates = list(set(list_duplicate_val))
print(no_duplicates)


#10 Find the common elements between two lists.

list_one = [1, 2, 3, 4, 5, 6, 7]
list_two = [3, 4, 5, 6, 7, 8, 9]
common_elements = set()

for num in list_one:
    if num in list_two:
        common_elements.add(num)

print(common_elements)

#set_two = set(list_two)
#common_elements = {num for num in list_one if num in set_two}
