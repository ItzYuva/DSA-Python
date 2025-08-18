'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

# Brute force approach -- O(n^3) time complexity
'''
def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:
                        result.append(triplet)
    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
'''

# Optimal solution below:

def threeSum(nums):

    # Step 1: Sort the array
    # Sorting helps with two-pointer technique and makes it easier to skip duplicates
    nums.sort()
    result = []

    # Step 2: Iterate through the array, fixing one number at a time
    for i in range(len(nums)):
        # Skip duplicate fixed numbers (to avoid repeated triplets)
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # The new target is the negative of the fixed number
        target = -nums[i]
        # Step 3: Initialize two pointers
        left = i + 1               # start just after the fixed number
        right = len(nums) - 1      # start from the last element

        # FROM HERE IT'S a 2 Sum problem
        # Step 4: Two-pointer search
        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum == target:
                # Found a triplet → add fixed number + two-pointer numbers
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for left pointer
                left_val = nums[left]
                while left < right and nums[left] == left_val:
                    left += 1

                # Skip duplicates for right pointer
                right_val = nums[right]
                while left < right and nums[right] == right_val:
                    right -= 1

            # If sum too small, move left pointer forward to increase it
            elif curr_sum < target:
                left += 1
            # If sum too big, move right pointer backward to decrease it
            else:
                right -= 1

    # Step 5: Return all unique triplets
    return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))