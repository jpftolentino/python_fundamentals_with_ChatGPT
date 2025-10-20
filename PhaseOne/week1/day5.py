#🔹 Day 5 (Problems 41–50: Mixed Challenges)

import math

#Q1 Sum of even numbers 1–100.

total = 0

for n in range(1,101):
    if n % 2 == 0:
        print(n)
        total += n

print(total)

#Q2 Sum of odd numbers 1–100.

total = 0

for n in range(1, 101, 2):
    total += n
    
print(total)

#Q3 Count how many numbers 1–100 are divisible by 3.

count = 0

for n in range(1,101):
    if n % 3 == 0:
        count += 1

print(count)

#Q4 Print first n multiples of 7.

term = int(input("Enter n: "))

for n in range(1, term + 1):
    print(n * 7)

#Q5 Print all numbers 1–n that are multiples of 2 or 5.

n = int(input("Enter n where 1-n shows only multiples of 2 or 5: "))

for i in range(1, n + 1):
    if i % 2 == 0 or i % 5 == 0:
        print(i)

#Q6 Print powers of 2 up to 1000. **

powers = 2

while powers <= 1000:
    powers *= 2
    if powers <= 1000:
        print(powers)

#Q7 Print multiplication table of 5.

for n in range(1, 11):
    print(f"{n} X 5 = {n * 5}")

#Q8 FizzBuzz from 1–30.

for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)   

#Q9 Collatz sequence starting from n.

n = int(input("Enter n: "))

while n != 1:
    if n % 2 == 0:
        n /= 2
        print(n)
    else:
        n = (n * 3) + 1
        print(n)
print(n)


#Q10 Check if a number is a perfect number. **

n  = int(input("Enter a number to check if it's a perfect number: "))

total = 0
root = math.sqrt(n)
i = 1

while i <= root:
    place_holder = n
    if i == 1:
        total += 1
    elif n % i == 0:
        total += (place_holder / i)
        total += i
    i += 1

if int(total) == n:
    print("Perfect number!")
else:
    print("Not Perfect!")

# from math import isqrt

# n = int(input("Enter a number: "))

# if n <= 1:
#     print("Not Perfect!")  # by definition, proper divisors sum < n
# else:
#     total = 1  # 1 is a proper divisor of every n > 1
#     root = isqrt(n)

#     for i in range(2, root + 1):
#         if n % i == 0:
#             total += i
#             pair = n // i
#             if pair != i:      # avoid double-counting squares
#                 total += pair

#     print("Perfect number!" if total == n else "Not Perfect!")