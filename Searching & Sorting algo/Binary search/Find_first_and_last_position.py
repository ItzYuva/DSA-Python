'''
Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1].


Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
Explanation: The target 8 appears from index 3 to index 4.
 
Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
Output: [-1, -1] 
Explanation: The target 6 is not found in the array.

Use binary search twice:
1. To find the first occurrence of the target.
2. To find the last occurrence of the target.
'''
nums = [5, 7, 7, 8, 8, 10]
target = 6 

def searchRange(nums, target):
    # Implement your solution here

    # Below is the brute force approach --
     
    # start = -1
    # end = -1

    # for i in range(len(nums)):
    #     if nums[i] == target:
    #         if start == -1:
    #             start = i
    #         end = i       

    # return [start, end]

    
    def first_element(nums, target):
        
        first = -1
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] < target:
                start=mid + 1
            elif nums[mid]>target:
                end = mid - 1
            else:
                first = mid
                end = mid-1
                
        return first
        
    
    def last_element(nums, target):
        
        last = -1
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end)//2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                last = mid
                start = mid+1 
            
        return last
        
    first = first_element(nums, target)
    last = last_element(nums, target)    
    return [first, last]
                
    
print(searchRange(nums, target))
