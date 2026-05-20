# Write the code to swap numbers using bit manipulation (XOR operator)

def swap_numbers(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

a = 3
b = 5
print(f"Before swapping: a = {a}, b = {b}")
a, b = swap_numbers(a, b)
print(f"After swapping: a = {a}, b = {b}")
#  time complexity will be O(1) because we are performing a constant number of operations regardless of the input size.
#  space complexity will be O(1) because we are using a constant amount of space