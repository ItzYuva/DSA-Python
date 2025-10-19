'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false

Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true
'''


def isIsomorphic(s, t):
    # If lengths are different, one-to-one mapping is impossible
    if len(s) != len(t):
        return False

    # map_st: mapping from s → t
    # map_ts: mapping from t → s
    map_st = {}
    map_ts = {}

    # Loop through both strings simultaneously
    for i in range(len(s)):
        ch1 = s[i]  # character from string s
        ch2 = t[i]  # character from string t

        # Check if mapping from s → t is consistent
        if ch1 in map_st:
            # If ch1 already mapped to a different character, return False
            if map_st[ch1] != ch2:
                return False
        else:
            # Otherwise, store new mapping
            map_st[ch1] = ch2

        # Check if mapping from t → s is consistent
        if ch2 in map_ts:
            # If ch2 already mapped to a different character, return False
            if map_ts[ch2] != ch1:
                return False
        else:
            # Otherwise, store new mapping
            map_ts[ch2] = ch1

    # If we reached here, all mappings are consistent → strings are isomorphic
    return True
