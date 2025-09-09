'''
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
'''

def singleNumber(nums):
    # Step 1: Sort the array so duplicates come next to each other
    nums.sort()

    # Step 2: Use index pointer i to scan through the array
    i = 0

    # Step 3: Loop through pairs while i is within the second last element
    while i < len(nums) - 1:
        # If current element doesn't match the next element,
        # this is the single unique element
        if nums[i] != nums[i+1]:
            return nums[i]

        # Otherwise, skip this pair (since they are duplicates)
        i += 2

    # Step 4: If no mismatch found inside loop,
    # the last element must be the unique one
    return nums[-1]

nums = [2,2,1]
print(singleNumber(nums))
