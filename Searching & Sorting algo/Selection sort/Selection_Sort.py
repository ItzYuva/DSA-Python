'''
You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

Example:
Input: lst = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Input: lst = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]
'''
lst = [64, 25, 12, 22, 11]

def selection_sort(lst):
    n = len(lst)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
    return lst

print(selection_sort(lst))
