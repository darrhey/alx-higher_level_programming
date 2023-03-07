#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str1 = f'Last digit of {number} is {last_digit}'
if last_digit == 0:
    print(f"{str1} and is 0")
elif last_digit > 5:
    print(f"{str1} and is greater than 5")
else:
    print(f"{str1} and is less 6 and not 0")
