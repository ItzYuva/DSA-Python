'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.


Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.
'''


def rearrangeArray(nums):

    # Create a result list with the same length as nums, filled with zeros.
    result = [0] * len(nums)

    # 'pi' (positive index) starts from 0 → even indices (0, 2, 4, ...)
    # 'ni' (negative index) starts from 1 → odd indices (1, 3, 5, ...)
    pi, ni = 0, 1

    # Loop through every element in the input list
    for num in nums:
        # If the number is positive → place it at current even index (pi)
        if num > 0:
            result[pi] = num      # assign the number to that position
            pi += 2               # move to the next even index
        else:
            # If the number is negative → place it at current odd index (ni)
            result[ni] = num      # assign the number to that position
            ni += 2               # move to the next odd index

    # After processing all numbers, result contains alternating +ve and -ve numbers
    return result
