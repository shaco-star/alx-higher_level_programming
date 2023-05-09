#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number % 10)
string = "Last digit of {} is {} "
if lastD > 5:
    print(string.format(number, lastD) + "and is greater than 5")
elif lastD == 0:
    print(string.format(number, lastD) + "and is 0")
else:
    print(string.format(number, lastD) + "and is less than 6 and not 0")
