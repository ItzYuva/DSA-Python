'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3
'''

# 1st approach: O(n log n) time
'''
def longestConsecutive(nums):
    if not nums:
        return 0
    nums = sorted(nums)
    longest = 1
    curr_streak = 1
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i-1]
        if diff == 1:
            curr_streak += 1
        elif diff == 0:
            continue
        else:
            longest = max(longest, curr_streak)
            curr_streak = 1
    longest = max(longest, curr_streak)

    return longest
'''

# 2nd approach: O(n) time using set

def longestConsecutive(nums):
    # Convert the list to a set for O(1) lookups and to remove duplicates
    nums_set = set(nums)

    # Variable to keep track of the longest consecutive sequence length
    longest = 0

    # Loop through each unique number in the set
    for num in nums_set:

        # Check if the current number is the start of a sequence
        # (i.e., the previous number num-1 doesn't exist in the set)
        if num - 1 not in nums_set:

            # Start counting from this number
            curr_num = num
            curr_streak = 1  # initial length is 1 (the current number itself)

            # Continue checking for the next consecutive numbers
            while curr_num + 1 in nums_set:
                curr_num += 1          # move to the next consecutive number
                curr_streak += 1       # increment streak length

            # Update the longest streak found so far
            longest = max(longest, curr_streak)

    # Return the maximum length of consecutive sequence found
    return longest
