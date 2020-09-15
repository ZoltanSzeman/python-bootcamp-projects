# Created by Zoltan Szeman
# Task: Implement Collatz conjecture for n>1.

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
    
n = 9780657630
print(f'Steps required to reach 1 via Collatz conjecture from {n} is '
        f'{collatz_steps(n)}')
