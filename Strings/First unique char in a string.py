'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
'''

def firstUniqChar(s):

    freq = {}  # Dictionary to store how many times each character appears
    for ch in s:
        # freq.get(ch, 0) returns existing count OR 0 if character not present
        # Then we add 1 to update the count
        freq[ch] = freq.get(ch, 0) + 1

    # Find the first character with frequency = 1
    for i, ch in enumerate(s):
        # If the character appears only once, it's the first unique char
        if freq[ch] == 1:
            return i

    # If no unique character exists, return -1
    return -1
