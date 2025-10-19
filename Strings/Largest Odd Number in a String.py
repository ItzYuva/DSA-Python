'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string. 

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
'''
# Brute force approach: Generate all substrings, check if odd, track largest
# Time complexity: O(n^3) due to substring generation and integer conversion

def largestOddNumber(num):
    largest = ""
    if not num:
        return ""
    for i in range(len(num)):
        for j in range(i+1, len(num)+1):
            substring = num[i:j]
            number = int(substring)
            if number % 2 == 1:
                if largest == "" or number > int(largest):
                    largest = substring
    return largest

# Optimized approach: Scan from the end to find the first odd digit
# Time complexity: O(n)
# A number is odd if its last digit is odd (1, 3, 5, 7, or 9).

def largestOddNumber(num):
    # scan from the end to find the rightmost odd digit
    for i in range(len(num)-1, -1, -1):
        # check if current digit is odd
        if int(num[i]) % 2 == 1:
            # return substring up to and including i
            return num[:i+1]
    return ""