# Created by Zoltan Szeman
# 2020-09-09
# Task: Print e to the nth digit

from mpmath import mp
from math import e

while True:
    try:
        digit_no = int(input('Enter, how many digits of '
            'e should be printed: '))
        break
    except ValueError:
        print('\nPlease enter a valid whole number!\n')

mp.dps = digit_no    # set number of digits
print(f'e to the {digit_no}th digit is {mp.e}')
