'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

def frequencySort(s):

    # Step 1: Count frequencies of each character
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    # "tree" -> {'t':1, 'r':1, 'e':2}

    # Step 2: Sort characters by frequency
    # count.items() gives list of tuples (char, freq)
    # key=lambda x:x[1] -> sort by freq (the second element)
    # reverse=True -> highest frequency comes first
    sorted_chars = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # [('e', 2), ('t', 1), ('r', 1)]

    # Step 3: Build result string
    # For each (char, freq) in sorted order,
    # repeat the char 'freq' times and add it to result
    result = ""
    for char, freq in sorted_chars:
        result += char * freq

    return result

s = "tree"
print(frequencySort(s))