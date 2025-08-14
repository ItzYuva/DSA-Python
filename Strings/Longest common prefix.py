'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def longestCommonPrefix(strs):
    # If the input list is empty, there is no common prefix
    if not strs:
        return ""
    
    # Assume the first string is the initial prefix
    prefix = strs[0]

    # Loop through each word in the list (starting from the second one)
    for word in strs[1:]:

        # Find the smaller length between the current prefix and the current word
        min_len = min(len(prefix), len(word))

        # Compare characters one by one until they differ
        j = 0
        while j < min_len and prefix[j] == word[j]:
            j += 1

        # Cut down the prefix to the matched portion
        prefix = prefix[:j]

        # If prefix becomes empty, no common prefix exists — return immediately
        if prefix == "":
            return ""
        
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
