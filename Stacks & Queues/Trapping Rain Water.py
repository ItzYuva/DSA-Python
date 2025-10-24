'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''
# Below method computes the trapped rainwater using arrays: {O(n) time, O(n) space}
def trap(height):
    n = len(height)

    # leftMax[i] = tallest bar from index 0 to i
    def getLeftMax(height, n): # Function to compute maximum height to the LEFT of each bar
        leftMax = [0] * n
        leftMax[0] = height[0]  # first element has no left bars
        for i in range(1, n):
            # For each index, store the maximum of previous left max or current height
            leftMax[i] = max(leftMax[i-1], height[i])
        return leftMax

    # rightMax[i] = tallest bar from index i to n-1
    def getRightMax(height, n): # Function to compute maximum height to the RIGHT of each bar
        rightMax = [0] * n
        rightMax[n-1] = height[n-1]  # last element has no right bars
        for i in range(n-2, -1, -1):
            # For each index, store the maximum of next right max or current height
            rightMax[i] = max(rightMax[i+1], height[i])
        return rightMax

    leftMax = getLeftMax(height, n)
    rightMax = getRightMax(height, n)

    # Water trapped at each index i:
    # = min(leftMax[i], rightMax[i]) - height[i]
    trapped_water = 0
    for i in range(n):
        h = min(leftMax[i], rightMax[i]) - height[i]
        trapped_water += h  # accumulate trapped water for each index

    return trapped_water

# We can solve this problem using two pointer approach as well: {O(n) time, O(1) space}
def trap(height):
    left, right = 0, len(height)-1
    leftMax = 0
    rightMax = 0
    trapped_water = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                trapped_water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                trapped_water += rightMax - height[right]
            right -= 1
    return trapped_water
