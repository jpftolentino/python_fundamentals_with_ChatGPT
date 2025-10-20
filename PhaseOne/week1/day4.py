# 🔹 Day 4 (Problems 31–40: While Loops & Number Properties)

#Q1 Print numbers 1–10 using while.

n = 1

while n < 11:
    print(n, end=" ")
    n += 1

#Q2 Sum numbers 1–100 using while.
print()
sum = 0
n = 1

while n < 101:
    sum += n
    n += 1
print(sum)

#Q3 Factorial of a number using while.

num = int(input("Enter the factorial digit: "))
i = 1
total = 1

while i <= num:
    total *= i
    i += 1
print(total)

#Q4 Reverse digits of a number using while.

num = int(input("Please enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

# print(reverse)

#Q5 Count digits in a number.
num = int(input("Please enter a number: "))

count = 0

while num > 0:
    num //= 10
    count += 1

print(count)

#Q6 Print Fibonacci sequence (10 terms).
count = 1
terms = 10
a,b = 0, 1

while count <= 10:
    print(a)
    a,b = b, a + b
    count += 1
    

#Q7 Keep taking input until "stop". **

while True:
    user_input = input("Type 'stop' to end: ")
    if user_input == 'stop':
        print("Stopped")
        break
    else:
        print("You entered", user_input)

#Q8 Guess the number until user enters 7.

while True:
    user_input = int(input("Enter a number: "))
    if user_input == 7:
        print("You guessed the correct number!")
        break
    else:
        print("Guess again!")

#Q9 Sum of digits of a number.

number = int(input("Please enter a number: "))
sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print(sum)

#Q10 Product of digits of a number.

number = int(input("Please enter a number: "))
product = 1

while number > 0:
    digit = number % 10
    product *= digit 
    number //= 10
print(product)