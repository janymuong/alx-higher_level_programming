#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    last_digit = (number * -1 % 10) * -1
else:
    last_digit = number % 10
init_message = 'Last digit of'
spec_msg = ''
if last_digit > 5:
    spec_msg = 'and is greater than 5'
elif last_digit == 0:
    spec_msg = 'and is 0'
elif last_digit < 6:
    if last_digit != 0:
        spec_msg = 'and is less than 6 and not 0'
print(f'{init_message} {number} is {last_digit} {spec_msg}')
