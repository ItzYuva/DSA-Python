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

# Brute Force Approach: O(n^3) time, O(1) space
# Try every possible subarray, calculate its sum, and keep track of the maximum sum found
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
'''

# Optimized Approach: O(n) time, O(1) space
# Use Kadane's Algorithm

def maxSubArray(nums):
    # Initialize current sum (for tracking ongoing subarray)
    curr_sum = 0
    
    # Get length of the input array
    n = len(nums)
    
    # Initialize max_sum as negative infinity to handle all negative arrays
    max_sum = float('-inf')
    
    # Loop through each element in the array
    for i in range(n):
        # Add current element to curr_sum
        curr_sum += nums[i]
        
        # Update max_sum if current sum is greater
        max_sum = max(curr_sum, max_sum)
        
        # If current sum becomes negative, reset it to 0
        # (because a negative sum will decrease the future total)
        if curr_sum < 0:
            curr_sum = 0
    
    # Return the maximum subarray sum found
    return max_sum
