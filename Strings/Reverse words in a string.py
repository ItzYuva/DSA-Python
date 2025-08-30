'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
# Brute force approach--

def reverseWords(self, s):
    # Step 1: Extract words manually
    words = [] # list to store all words
    word = "" # temporary string to build the current word

    for char in s:                     # loop over every character in the string
        if char != " ":                # if it's not a space, it's part of a word
            word += char
        elif word:                     # if it's a space AND we already built a word
            words.append(word)         # save the completed word into the list
            word = ""                  # reset for the next word

    if word:                           # handle last word (string may not end with space)
        words.append(word)

    # Step 2: Rebuild the string in reverse order
    result = ""                        # final reversed string
    for i in range(len(words)-1, -1, -1):   # loop backwards from last word to first
        result += words[i]             # add the word
        if i != 0:                     # add a space (but not after the last word)
            result += " "

    return result

# Optimal approach (using built-in functions)--
'''
    words = s.split()
    words.reverse()
    return " ".join(words)
'''