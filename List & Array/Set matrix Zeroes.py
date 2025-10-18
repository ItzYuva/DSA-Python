'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
'''

def setZeroes(matrix):
    # Store dimensions
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Flags to remember if first row or first column need to be zeroed
    frz = False  # (frz = first row zero)
    fcz = False  # (fcz = first column zero)

    # Check if there is any zero in the first row
    for j in range(cols):
        if matrix[0][j] == 0:
            frz = True
            break

    # Check if there is any zero in the first column
    for i in range(rows):
        if matrix[i][0] == 0:
            fcz = True
            break

    # Step 2: Use the first row and first column as marker arrays
    # For each zero found (except in first row/col),
    # mark the corresponding first row and first column entry as zero
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0   # mark the row
                matrix[0][j] = 0   # mark the column

    # Step 3: Traverse the matrix again (excluding first row/col)
    # and set cell to 0 if its row or column marker is 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 4: Finally, handle the first row and first column separately
    # If frz is True → zero out the entire first row
    if frz:
        for j in range(cols):
            matrix[0][j] = 0

    # If fcz is True → zero out the entire first column
    if fcz:
        for i in range(rows):
            matrix[i][0] = 0

    # Step 5: No return needed (in-place modification)
    # return matrix would still work for local testing though
    return matrix

# For reference: https://www.youtube.com/watch?v=pKs1dZFk2AU