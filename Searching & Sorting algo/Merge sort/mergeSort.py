# For reference: https://www.youtube.com/watch?v=_trEkEX_-2Q&ab_channel=Amulya%27sAcademy

def mergeSort(nums):
    """
    Merge Sort Algorithm
    --------------------
    Idea: Divide and Conquer
      1. Divide the list into halves until single elements remain.
      2. Conquer by merging sorted halves back together.
      3. Result: A fully sorted list.
    """

    # Base case: If the list has 1 or 0 elements, it’s already sorted
    if len(nums) > 1:

        # STEP 1: Divide
        mid = len(nums) // 2          # Find the middle index
        left_arr = nums[:mid]         # Left half
        right_arr = nums[mid:]        # Right half

        # Recursively sort each half
        mergeSort(left_arr)           # Sort the left half
        mergeSort(right_arr)          # Sort the right half

        # STEP 2: Conquer (Merge the two halves)
        i = 0   # Pointer for left_arr
        j = 0   # Pointer for right_arr
        k = 0   # Pointer for nums (the main list)

        # Compare elements from both halves, pick the smaller one each time
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                nums[k] = left_arr[i]   # Take from left
                i += 1
            else:
                nums[k] = right_arr[j]  # Take from right
                j += 1
            k += 1  # Move to next slot in nums

        # STEP 3: Handle leftovers
        # Copy remaining elements of left_arr (if any)
        while i < len(left_arr):
            nums[k] = left_arr[i]
            i += 1
            k += 1

        # Copy remaining elements of right_arr (if any)
        while j < len(right_arr):
            nums[k] = right_arr[j]
            j += 1
            k += 1

    # Return the sorted list
    return nums

nums = [-5,3,2,1,-3,-3,7,2,2]
print(mergeSort(nums))
