'''
Same question as 2 Sum but there's some modifications:
1. We do not want to return indices
2. Return all the pairs whose some is equal to the target
3. No duplicates

Example:

nums = [1, 2, 2, 3, 4, 5, 6, 7, 7]
target = 9
output = [[2, 7], [3, 6], [4, 5]]
'''

def two_sum_pairs(nums, target):
    # Step 1: Sort the array
    # Sorting helps to use the two-pointer technique 
    # and makes it easier to skip duplicates.
    nums.sort()  
    
    # Step 2: Initialize two pointers
    left = 0
    right = len(nums)-1  
    result = []  # to store the unique pairs

    # Step 3: Process until pointers meet
    while left < right:
        curr_sum = nums[left] + nums[right]  # sum of the two numbers

        if curr_sum == target:
            # Found a valid pair
            result.append([nums[left], nums[right]])

            # Skip duplicates for the left pointer
            left_val = nums[left]
            while left < right and nums[left] == left_val: 
                # we did "nums[left] == left_val" because When we find a valid pair, say (2,7), we don’t want to add (2,7) again if there are more 2s or more 7s in the array.
                left += 1  # move left forward until different value

            # Skip duplicates for the right pointer
            right_val = nums[right]
            while left < right and nums[right] == right_val:
                right -= 1  # move right backward until different value

        elif curr_sum < target:
            left += 1
        else:
            right -= 1

    return result
