# 🔹 Day 1 (Problems 51–60: String Basics & Indexing)

#1 Print the length of a string.

word = "hello"
print(len(word) == 5)


#2 Get the first and last character of a string.

ch = "awesome"
solution = "ae"
# answer = ch[0] + ch[len(ch) - 1]
answer = ch[0] + ch[-1:]
print(solution == answer)


#3 Slice the first 3 characters of "Python".

print("Python"[:3] == "Pyt")


#4 Reverse a string using slicing.

word = "John"
reverse = "nhoJ"
print(reverse == word[::-1])


#5 Convert "hello" to uppercase.

word = "hello"
print(word.upper() == "HELLO")


#6 Convert "WORLD" to lowercase.

word = "WORLD"
print(word.lower() == "world")


#7 Count how many times 'a' appears in "bananas".

word = "bananas"
print(word.count('a') == 3)


#8 Check if a string starts with 'Py'.

ch = input("Enter a string to check: ")
# print(ch[:2] == "Py")
print(ch.startswith('Py'))


#9 Check if a string ends with 'on'.

ch = input("Enter a string to check: ")
# print(ch[-2:])
print(ch.endswith('on'))

#10 Concatenate two strings with a space in between.

greeting = "Hello,"
name = "John!"
# print(greeting + " " + name) 
print(f"{greeting} {name}")