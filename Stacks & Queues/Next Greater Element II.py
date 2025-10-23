'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
'''

def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n      # Initialize result array with -1 (default if no next greater exists)
    stack = []          # Monotonic decreasing stack (stores indices)

    # Loop twice through the array to simulate the circular behavior
    for j in range(2 * n):
        i = j % n       # Use modulo to wrap around (circular traversal)
        
        # While current number is greater than the number at index on top of stack
        # -> current number is the "next greater element" for that index
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()   # Pop the index whose next greater is found
            res[idx] = nums[i]  # Update result for that index
        
        # Only push indices during first pass (j < n)
        # because pushing in second pass would duplicate work
        if j < n:
            stack.append(i)     # Add current index to stack for future comparison
    
    # Return the filled result array
    return res
