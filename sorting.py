# Created by Zoltan Szeman
# Task: Sort an array via bubble and merge sort algorithms.

from random import randint
import time
array = []

def merge_sort(array):
    if len(array) > 1:
    #Keep dividing till the array is sorted, has only 1 element
        m = len(array)//2
        left = array[:m]
        right = array[m:]
        left = merge_sort(left)
        right = merge_sort(right)
        array = [] #create a third array
        while len(left) > 0 and len(right) > 0:
        #compare left and right arrays
            if left[0] > right[0]:
                array.append(right[0])
                right.pop(0)
            else:
                array.append(left[0])
                left.pop(0)
        #add left out items either from left or right arrays
        for i in left:
            array.append(i)
        for i in right:
            array.append(i)
    return array
        
while len(array) != 500:
    array.append(randint(1,10000)) #create a large array with random numbers

print(f'The array to sort is {array}')
sort_type = input('\nWould you like to use bubble or merge sort? [b/m]: ')

start_time = time.time()
if sort_type == 'b': #implementing bubble sort algorithm
    swap_no = 0
    prev_swap_no = -1
    while swap_no > prev_swap_no: #stop sorting if the swaps stop
        prev_swap_no = swap_no
        for i in range(0,len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swap_no += 1
    print(f'\nSorted array: {array}')
    print(f'\nSorting time: {time.time()-start_time} [sec]')
        
elif sort_type == 'm':
    array = merge_sort(array) #calling merge_sort function
    print(f'\nSorted array: {array}')
    print(f'\nSorting time: {time.time()-start_time} [sec]')
