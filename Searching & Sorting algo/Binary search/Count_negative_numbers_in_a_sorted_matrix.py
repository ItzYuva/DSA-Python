'''
You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix.

Input: grid = [[4, 3, 2, 1],
               [3, 2, 1, -1],
               [1, 1, -1, -2], 
               [-1, -1, -2, -3]]
Output: 7 
Explanation: There are 7 negative numbers in the matrix.
'''
grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]

def countNegatives(grid):
    # Implement your solution here

    count = 0
    
    for row in grid:
        start = 0
        end = len(grid[0])  # here, end = 4
        
        while start < end:
            mid = (start+end)//2
            if row[mid] < 0:
                end = mid
            else:
                start = mid + 1
        count += len(grid[0])-start
        
    return count

print(countNegatives(grid))
