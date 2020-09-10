# Created by Zoltan Szeman
# Task: Check whether a number has prime factors

import math

def prime_check(n, prime_factors):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            break
    else:
        prime_factors.append(n)
        
input_no = int(input('Enter a positive integer to check for prime factors: '))
prime_factors = []

for n in range(2, (input_no // 2) + 1):
    if input_no % n == 0:
        prime_check(n, prime_factors)
    
if len(prime_factors) == 0:
    print(f"{input_no} is a prime. It doesn't have prime factors")
else:
    print(f'The prime factors of {input_no} are: {prime_factors}')
