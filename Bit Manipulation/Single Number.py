"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""

# using hash map to count the occurrences of each number in the array and then return the number that appears only once.
# time complexity will be O(n) because we are iterating through the array twice, once to count the occurrences and once to find the single number.
# space complexity will be O(n) because we are using a hash map to store the count of each number in the array, which can potentially store all the numbers in the worst case.
def singleNumber(nums):
    hash_map = {}
    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1 # Count the occurrences of each number in the array
    for key in hash_map:
        if hash_map[key] == 1:
            return key
        

        
# using bit manipulation (XOR operator) to find the single number in the array.
# time complexity will be O(n) because we are iterating through the array once to perform the XOR operation on all the numbers.
# space complexity will be O(1) because we are using a constant amount of space to store the result of the XOR operation.
def singleNumber(nums):
    result = 0
    for num in nums:
        result = result^num # XOR operation on all the numbers in the array
    return result

# NOTE: The XOR operator has a property that it returns 0 when two identical numbers are XORed together, and it returns the number itself when XORed with 0. Therefore, when we XOR all the numbers in the array, the pairs of identical numbers will cancel each other out and we will be left with the single number that appears only once.