"""
Given an array arr, you need to reverse a subarray of that array. The range of this subarray is given by indices l and r (1-based indexing).

Example 1:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
Output: [1, 4, 3, 2, 5, 6, 7]
Explanation: After reversing the elements in range 2 to 4 (2, 3, 4), modified array is 1, 4, 3, 2, 5, 6, 7.

Example 2:

Input: arr[] = [1, 6, 7, 4], l = 1, r = 4
Output: [4, 7, 6, 1]
Explanation: After reversing the elements in range 1 to 4 (1, 6, 7, 4), modified array is 4, 7, 6, 1.
"""

def reverseSubArray(arr, l, r):
    func(arr, l - 1, r - 1)
    return arr

def func(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    func(arr, l + 1, r - 1)

result = reverseSubArray([1, 4, 5, 0, 6, 7], 2, 4)
print(result)  # Output: [1, 0, 5, 4, 6, 7]