'''
1. The largest element will always end up at the rightmost position.
2. We need len(arr)-1 passes to do that.
'''
# Example:
lst = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(lst):
    # Your code goes here
    for passes in range(len(lst)):
        for j in range(0, len(lst)-1-passes):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
    return lst

print(bubble_sort(lst))

# you can optimize it a little more by not doing all this thing if the list is already sorted.