"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

# using bit manipulation to generate all possible subsets of the given array.
# time complexity will be O(n * 2^n) because we are generating 2^n subsets and for each subset, we are iterating through the array to check which elements are included in the subset.
# space complexity will be O(n * 2^n) because we are storing all the subsets in the result list, and each subset can potentially contain all the elements of the input array in the worst case.
def subsets(nums):
    n = len(nums)
    total_sub = 1 << n # Calculate the total number of subsets, which is 2^n (or 1 shifted left by n)
    result = []
    for num in range(0, total_sub):
        lst = []
        for i in range(0, n):
            if num & (1 << i) != 0: # Check if the i-th bit of num is set (i.e., if the i-th element of nums should be included in the current subset)
                lst.append(nums[i])
        result.append(lst)

    return result

# for better understanding, you can check my notebook.