# 🔹 Day 3 (Problems 71–80: Lists Basics & Operations).

#1 Create a list of 5 numbers and print it.

numbers = [1, 2, 3, 4, 5]
print(numbers)


#2 Access the first, middle, and last element of a list.

numbers = [1, 2, 3, 4, 5]
#hard coded print(numbers[0], numbers[2], numbers[4])
mid = len(numbers) // 2
print(numbers[0], numbers[mid], numbers[-1])


#3 Append a number to a list.

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)


#4 Insert an element at index 2.

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 6)
print(numbers)


#5 Remove the last element from a list.

numbers = [1, 2, 3, 4, 5, 6]
numbers.pop()
print(numbers);


#6 Remove a specific element from a list.

fruits = ["apple", "banana", "orange", "grape", "lemon"]
fruits.remove("orange")
print(fruits)


#7 Sort a list in ascending order.

numbers = [3, 5, 6, 8, 0, 2, 7]
numbers.sort()
print(numbers)


#8 Sort a list in descending order.

numbers = [3, 5, 6, 8, 0, 2, 7]
numbers.sort(reverse=True)
print(numbers)


#9 Find the maximum and minimum value in a list.

list_one = [-1, 5, 6, 8, 12, 2, 7]
print(max(list_one))
print(min(list_one))


#10 Find the sum and average of list elements.

list_one = [-1, 5, 6, 8, 12, 2, 7]
print(sum(list_one))
avg = sum(list_one) / len(list_one)
print(avg)


