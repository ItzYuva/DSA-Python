'''
You are given a sorted array of characters letters, sorted in non-decreasing order, and a character target. There are at least two different characters in letters. Your task is to return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

Example:

Input:
letters = ['c', 'f', 'j']
target = 'k'
Output: 'c'
 
Input:
letters = ['c', 'f', 'j']
target = 'c'
Output: 'f'
 
Input:
letters = ['c', 'f', 'j']
target = 'a'
Output: 'c'
'''

letters = ['c', 'f', 'j']
target = 'c'

def next_greatest_letter(letters, target):
    """
    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.
    """
    # Implement the function logic
    
    start = 0
    end = len(letters) - 1
    
    while start <= end:
        mid = (start + end)//2

        # As you move right, the letters get bigger and As you move left, the letters get smaller.
  
        if letters[mid] <= target:
            start = mid+1
        else:
            end = mid-1
            
            
    if start < len(letters):
        return letters[start]
    else:
        return letters[0]
        
print(next_greatest_letter(letters, target))
