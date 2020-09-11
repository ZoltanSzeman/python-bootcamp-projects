# Created by Zoltan Szeman
# Task: Print the next prime number if the user wants it.

import math

def prime_check(n, prime_factors):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            break
    else:
        prime_factors.append(n)
    
n = 2
prime_factors = [n]
print(f'The first prime number is {n}')
while True:
    prev_len = len(prime_factors)
    n += 1
    prime_check(n, prime_factors)
    if prev_len < len(prime_factors):
        if input('\nPress {Enter} for next prime or {q} '
                    'to quit: ').lower() == '':
            print(f'\n{n}')
        else:
            break
    
print('\nEnd of program')
