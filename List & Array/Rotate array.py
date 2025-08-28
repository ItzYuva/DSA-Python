'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

# My brute force approach--
'''
def rotate(nums, k):
    if not nums:
        return []
    for i in range(k):
        last = nums.pop()
        nums.insert(0, last)
    return nums
'''

# Optimal approach--
def rotate(nums, k):
    n = len(nums)
    # Normalize k: if k >= n, rotating n times brings us back to the same array.
    # So we only need to rotate by (k % n).
    k %= n
    
    # Helper function to reverse elements in nums between indices start and end (inclusive).
    # It swaps elements from both ends moving towards the middle.
    def reverse(start, end):
        while start < end:
            # Swap the elements at the two pointers
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(0, n-1)
    # Step 2: Reverse first k elements
    # After step 1: [7,6,5,4,3,2,1]
    # Reverse first k=3 -> [5,6,7,4,3,2,1]
    reverse(0, k-1)
    # Step 3: Reverse last n-k elements
    # Reverse from index k=3 to end -> [5,6,7,1,2,3,4]
    # Final rotated array
    reverse(k, n-1)

    return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))
