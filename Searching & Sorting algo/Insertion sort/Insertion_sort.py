'''
Insertion Sort works by building a sorted section of the list, one element at a time, by inserting each new element into its proper position within the already sorted section.

Example:
Input: lst = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]
'''
lst = [12, 11, 13, 5, 6]

def insertion_sort(lst):
    # Your code goes here
    n = len(lst)
    
    for i in range(1, n):
        key = lst[i]
        j = i-1
        
        while j>=0 and lst[j]>key:
            lst[j+1] = lst[j]
            j -= 1
            
        lst[j+1] = key
        
    return lst 

print(insertion_sort(lst))
