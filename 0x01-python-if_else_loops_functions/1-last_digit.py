#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    d = (-number) % 10
    d *= -1
else:
    d = number % 10
print(f"Last digit of {number} is {d} and is", end=' ')
if d > 5:
    print("greater than 5")
elif d == 0:
    print("0")
else:
    print("less than 6 and not 0")
