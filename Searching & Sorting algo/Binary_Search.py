'''
Binary search can only be applied on sorted arrays.

Steps to implement binary search --

1. Set start = 0, end = len(arr) - 1
2. While start <= end:
        Compute mid
        Compare arr[mid] with target
        Adjust start or end
3. Return index if found, else -1
'''
# Example --
arr = [10, 20, 30, 40, 50]

def binary_search(arr, target):

# Initialize pointers
    start = 0
    end = len(arr) - 1

# Loop while search space is valid
    while start <= end:

    # Find the middle index
        mid = (start + end) // 2

    # Compare middle value with target
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1    # Search in the left half

# If loop ends, target not found
    return -1

print(binary_search(arr, 50)) 
