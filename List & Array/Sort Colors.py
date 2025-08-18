'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
'''

# Brute force approach (insertion sort with O(n^2) time complexity)
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n < 1:
        return nums
    for i in range(n):
        j = i
        while ( j > 0) and (nums[j] < nums[j-1]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -=1


# Optimal approach is by using Dutch national flag algorithm (its not binary search)

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    # Three pointers:
    # low   -> boundary for 0s (everything left of low is 0)
    # mid   -> current element under examination
    # high  -> boundary for 2s (everything right of high is 2)
    low = 0
    mid = 0
    high = len(nums) - 1

    # Loop until mid crosses high
    while mid <= high:
        # Case 1: nums[mid] == 0 → put it at the front
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]  # swap current with low
            low += 1   # expand 0s boundary
            mid += 1   # move to next element

        # Case 2: nums[mid] == 1 → correct place, just move on
        elif nums[mid] == 1:
            mid += 1

        # Case 3: nums[mid] == 2 → put it at the end
        else:
            nums[mid], nums[high] = nums[high], nums[mid]  # swap current with high
            high -= 1  # shrink 2s boundary
            # Note: mid is NOT incremented here, 
            # because the swapped element at nums[mid] needs to be checked again

nums = [2,0,2,1,1,0]
print(sortColors(nums))