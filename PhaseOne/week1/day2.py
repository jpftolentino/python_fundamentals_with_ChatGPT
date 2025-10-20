#🔹 Day 2 (Problems 11–20: Operators & Conditions)

#Q1 Check if a number is even.

num = [1, 2, 3]
for i in range(len(num)):
    if num[i] % 2 ==0:
        print(f"{num[i]} is even")


#Q2 Check if a number is odd.

num = [1, 2, 3]
for i in range(len(num)):
    if num[i] % 2 != 0:
        print(f"{num[i]} is odd")

#Q3 Find the largest of two numbers. **

a, b = 14, 10
if a > b:
    print(a)
else:
    print(b)
#print(max(a,b))

#Q4 Find the largest of three numbers. **

num = [24, 6, 7]
largest = 0
for i in range(len(num)):
    if num[i] > largest:
        largest = num[i]
print(largest)
#print(max(num))

#Q5 Print "Positive", "Negative", or "Zero".

num = [-4, 8, 0, -6]
for i in range(len(num)):
    if num[i] == 0:
        print("Zero")
    elif num[i] > 0:
        print("Positive")
    else:
        print("Negative")

#Q6 Check if a number is divisible by 5.
num = [12, 10, 45, 64, 122]
for i in range(len(num)):
    if num[i] % 5 == 0:
        print(f"{num[i]} is divisible by 5")
 
#Q7 Check if a number is divisible by both 2 and 3.
num = [6, 12, 13, 11, 36, 18, 45]
for i in range(len(num)):
    if num[i] % 2 == 0 and num[i] % 3 == 0:
        print(f"{num[i]} is divisible by 2 and 3")

#Q8 Print "Teenager" if age is 13–19, else "Not Teenager". **
num = [6, 12, 13, 11, 36, 18, 45]
for i in range(len(num)):
    if 13 <= num <= 19:
        print("Teenager")
    else:
        print("Not Teenager")

#Q9 Grade a score (A/B/C/F).
grade = int(input("Enter a grade score: "))
if grade < 60:
    print("F")
elif grade >= 60 and grade <= 69:
    print("C")
elif grade >= 70 and grade <= 79:
    print("B")
elif grade >= 80 and grade <= 100:
    print("A")
else:
    print("Invalid input")

#Q10 Check if a year is a leap year.

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("Not a leap year")
    else:
        print("It's a leap year")    