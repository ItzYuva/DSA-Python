'''
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

Example 1:
Input: start = 10, goal = 7
Output: 3
Explanation: The binary representation of 10 and 7 are 1010 and 0111 respectively. We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011.
- Flip the third bit from the right: 1011 -> 1111.
- Flip the fourth bit from the right: 1111 -> 0111.
It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we return 3.


Example 2:
Input: start = 3, goal = 4
Output: 3
Explanation: The binary representation of 3 and 4 are 011 and 100 respectively. We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010.
- Flip the second bit from the right: 010 -> 000.
- Flip the third bit from the right: 000 -> 100.
It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we return 3.
'''

def minBitFlips(start: int, goal: int) -> int:
    ans = start ^ goal
    count = 0
    for i in range(0, 32): # we are assuming that the input numbers are 32-bit integers, so we check each bit from 0 to 31
        if ans & (1<<i) != 0: # if the ith bit is set in ans, then we need to flip that bit
            count += 1
    return count

print(minBitFlips(10, 7))

#  time complexity will be O(1) because we are performing a constant number of operations regardless of the input size.
#  space complexity will be O(1) because we are using a constant amount of space