'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
'''

def maxSubArray(nums):
    n = len(nums)
    max_sum = float('-inf')  # start with very small value (handles all negatives)

    # try every possible starting point
    for i in range(n):
        # try every possible ending point (from i to end)
        for j in range(i, n):
            current_sum = 0
            # add up elements from i to j
            for k in range(i, j+1):
                current_sum += nums[k]
            # update answer if this subarray is better
            max_sum = max(max_sum, current_sum)

    return max_sum

nums = [5,4,-1,7,8]
print(maxSubArray(nums))  # expected 23 (whole array)