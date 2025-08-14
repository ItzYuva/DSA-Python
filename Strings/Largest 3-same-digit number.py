'''
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
'''


def largestGoodInteger(num):
    max_good = ""

    # Loop over each starting index for a 3-character substring
    # We stop at len(num)-2 so that i+3 doesn't go out of range
    for i in range(0, len(num)-2):

        # Extract a substring of length 3 starting at position i
        triplet = num[i:i+3]

        # Check if all three characters in the substring are the same
        if triplet[0] == triplet[1] == triplet[2]:

            # If this triplet is greater than the current max_good, update it
            # String comparison works here because all triplets are length 3
            if triplet>max_good:
                max_good = triplet
        
    return max_good

num = "6777133339"
print(largestGoodInteger(num))

