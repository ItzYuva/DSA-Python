'''
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
'''

def check(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    # Get the length of the array
    n = len(nums)
    
    # count will keep track of how many times the order is broken
    # (i.e., when nums[i] > nums[i+1])
    count = 0
    
    # Loop through the array
    # Note: we use range(n) instead of range(n-1) because we also want to check
    # the last element against the first element (circular/rotation check).
    for i in range(n):
        
        # Compare current element with the next element
        # (i+1) % n ensures we wrap around at the end.
        # Example: if i = n-1 (last index), (i+1) % n = 0 (first index).
        if nums[i] > nums[(i+1) % n]:
            count += 1   # order breaks → increase the count
    
    # After checking all pairs:
    # - If count == 0 → array is already sorted (not rotated) → True
    # - If count == 1 → array is sorted & rotated → True
    # - If count > 1 → array is neither sorted nor properly rotated → False
    return count <= 1

nums = [1,2,3]
print(check(nums))
