'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

def moveZeroes(nums):
    # Pointer that keeps track of where the next non-zero element should go.
    lastNonZeroNum = 0

    # 1st pass: Move all non-zero numbers to the front of the array.
    # Maintain their relative order by placing them one by one in sequence.
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[lastNonZeroNum] = nums[i]   # Place non-zero at the next open spot
            lastNonZeroNum += 1

    # At this point:
    # - All non-zeros are at the front of the array in correct order.
    # - lastNonZeroNum points to the index where the first 0 should go.
    # - The rest of the array still has old "junk" values that need to be cleared.

    # 2nd pass: Fill the rest of the array with zeros.
    for i in range(lastNonZeroNum, len(nums)):
        nums[i] = 0

    return nums

nums = [0,1,0,3,12]
print(moveZeroes(nums))