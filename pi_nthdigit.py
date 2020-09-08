# Created by Zoltan Szeman
# 2020-09-08
# Task: Print pi to the nth digit

from mpmath import mp
from math import pi

while True:
    try:
        digit_no = int(input('Enter, how many digits of '
            'should pi be printed: '))
        break
    except ValueError:
        print('\nPlease enter a valid whole number!\n')

mp.dps = digit_no    # set number of digits
print(f'Pi to the {digit_no}th digit is {mp.pi}')
