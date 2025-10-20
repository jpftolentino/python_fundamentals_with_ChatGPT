#🔹 Day 3 (Problems 21–30: If/Else & For Loops)

import math

#Q1 Check if a number is prime. **
n = 29
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")        

#Q2 Check if a character is a vowel. **
vowel = {"a", "e", "i", "o", "u"}
ch = input("Please enter a character: ").lower()

if ch in vowel:
    print("Vowel")
else:
    print("Not a vowel")

#Q3 Check if a character is uppercase or lowercase. **
ch = input("Please enter a character: ")

if len(ch) != 1:
    print("Please enter only 1 character")
elif ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Neither")


#Q4 Check if a number is a palindrome (e.g., 121). **

n = input("Please enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Q5 Case-insensitive string comparison ("python").
s = input("Please enter a string: ")

if s.lower() == "python":
    print("True")
else:
    print("False")

#Q6 Print "Even and Positive" if number is both even and > 0.
num = int(input("Enter a number: "))

if num % 2 == 0 and num > 0:
    print("Even and Positive")
elif num <= 0:
    print("Not Positive")
else:
    print("Not Even")

#Q7 Check if a person can vote (age >= 18).
age = int(input("Enter the person's age: "))

if age >= 18:
    print("True")
else:
    print("False")


#Q8 Print numbers 1–10 using for.
for n in range(1, 11):
    print(n, end=" ")

#Q9 Print even numbers from 1–20.
print()
for n in range(2, 21, 2):
    print(n, end=" ")

#print(*range(2, 21, 2))    

# for n in range(21):
#     if n % 2 == 0 and n > 0:
#         print(n, end=" ")

#Q10 Print squares of numbers 1–10.
print()
for n in range(1,11):
    print(n*n, end=" ")

#print(*[i*i for i in range(1, 11)])
