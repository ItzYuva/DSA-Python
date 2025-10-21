'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''

# Brute Force: O(n^2)

def nextGreaterElement(nums1, nums2):
    nums1Idx = {n:i for i, n in enumerate(nums1)}
    res = [-1] * len(nums1)
    for i in range(len(nums2)):
        if nums2[i] not in nums1Idx:
            continue
        for j in range(i+1, len(nums2)):
            if nums2[j] > nums2[i]:
                idx = nums1Idx[nums2[i]]
                res[idx] = nums2[j]
                break
    return res

# Optimized: O(n)

def nextGreaterElement(nums1, nums2):
    # Create a dictionary to map each element of nums1 to its index
    # This helps us know where to place the next greater element in the result array
    nums1Idx = {n: i for i, n in enumerate(nums1)}

    # Initialize result array with -1 (default value if no greater element is found)
    res = [-1] * len(nums1)

    # Stack to store elements from nums2 for which we are still finding the next greater element
    # The stack will maintain a decreasing order (top is always smallest)
    stack = []

    # Traverse through each element in nums2
    for i in range(len(nums2)):
        curr = nums2[i]  # Current element in nums2

        # If current element is greater than the element on top of the stack,
        # it means 'curr' is the next greater element for the top element of the stack
        while stack and curr > stack[-1]:
            val = stack.pop()  # Pop the smaller element
            idx = nums1Idx[val]  # Get its index in nums1 (using the map)
            res[idx] = curr  # Update the result array with the next greater element

        # If current element is in nums1, push it onto the stack
        # because we need to find its next greater element later
        if curr in nums1Idx:
            stack.append(curr)

    # Return the result list after processing all elements
    return res