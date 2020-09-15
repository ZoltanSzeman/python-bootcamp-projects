# Created by Zoltan Szeman
# Task: Implement Sieve of Eratosthenes algorithm for prime numbers.

import math

def print_primes(prime_list):
    '''print each prime with its corresponding sequance number'''
    j = 1
    for i in prime_list:
        print(f'{j}. prime: {i}')
        j += 1

def prime_sieve(n_list):
    '''only check multiples'''
    '''while the multiplicand is below the root of the max of n_list'''
    n_root = int(math.sqrt(n_list[-1]))
    for i in range(2,n_root):
        for j in range(i*2,n+1,i):
            try:
                n_list.remove(j)
            except:
                pass
    print_primes(n_list)
    
def list_maker(n):
    '''create a list to n'''
    n_list = [x for x in range(2,n+1)]
    prime_sieve(n_list)
    
n = pow(10,4)
list_maker(n)
