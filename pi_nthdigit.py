# Created by Zoltan Szeman
# 2020-09-08
# Task: Print pi to the nth digit

from math import pi

while True:
    try:
        nth_digit = int(input('Enter, what digit precision '
            'should pi be printed: '))
        break
    except ValueError:
        print('\nPlease enter a valid whole number!\n')

print(pi)
