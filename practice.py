def square(x):
    return x*x
#     squares = []
#     for i in numbers:
#         squares.append(i*i)
    # return squares
        
# print(square([1,2,3]))
        
# def square(*args):
#     squares = []
#     for i in args:
#         squares.append(i*i)
#     return squares
        
# print(square(1,2,3))

numbers = [1,2,3,4,5]
print(list(map(square, numbers)))

print()

numbers1 = [2,4,6]
numbers2 = [3,5,7]

added_numbers = list(map(lambda x,y:x+y, numbers1, numbers2))
print(added_numbers)

print()


'''
Count consonants in a string
Problem Description:

You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).


Input:

A single string s, where the length of s is between 1 and 1000.

Output:

An integer representing the total count of consonants in the input string.


Example:

Input: "Hello, World!"
Output: 7
 
Input: "Python Programming"
Output: 13
'''