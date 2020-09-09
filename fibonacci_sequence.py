# Created by Zoltan Szeman
# 2020-09-09
# Task: Print the fibonacci sequence to the nth digit

while True:
    try:
        seq_no = int(input('Enter the length of the fibonacci sequence '
            'you would like to print: '))
        break
    except ValueError:
        print('\nPlease enter a valid whole number!\n')

count = 2
i = 0
j = 1
fibonacci_list = [i, j]
while count != seq_no:
    k = i + j
    i = j
    j = k
    fibonacci_list.append(k)
    count += 1
    
print(f'Fibonacci sequence of {seq_no} length is:\n{fibonacci_list}')
