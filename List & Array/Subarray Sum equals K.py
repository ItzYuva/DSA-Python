'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''
# Brute Force

def subarraySum(nums, k):
    n = len(nums)
    sub = []
    count = 0
    for i in range(n):
        for j in range(i, n):
            sub.append(nums[i:j+1])
    for subs in sub:
        if sum(subs) == k:
            count += 1
    return count