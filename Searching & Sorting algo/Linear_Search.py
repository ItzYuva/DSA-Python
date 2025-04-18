'''
A simple approach is to do a linear search, i.e

1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[].
2. If x matches with an element, return the index.
3. If x doesn’t match with any of the elements, return -1.
'''

# Example
arr = [10, 23, 45, 70, 11, 15]
target = 70

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
