# Created by Zoltan Szeman
# Task: Sort an array via bubble and merge sort algorithms.

from random import randint
import time
#time.time()
array = []

while len(array) != 500:
    array.append(randint(1,10000))

print(f'The array to sort is {array}')
sort_type = input('\nWould you like to use bubble or merge sort? [b/m]: ')

start_time = time.time()
swap_no = 0
prev_swap_no = -1
if sort_type == 'b': #implementing bubble sort algorithm
    while swap_no > prev_swap_no:
        prev_swap_no = swap_no
        for i in range(0,len(array)):
            try:
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    swap_no += 1
            except IndexError:
                pass
    print(f'\nSorted array: {array}')
    print(f'\nSorting time: {time.time()-start_time} [sec]')
    
elif sort_type == 'm':
    pass
