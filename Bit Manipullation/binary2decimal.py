#  write a code to convert binary to decimal

def binary2decimal(num:str)-> int:
    decimal_num = 0
    power = 0
    idx = len(num) - 1  # Start from the last index of the binary string
    while idx>= 0:
        num = int(num[idx])*(2**power) # Convert the character to an integer and calculate its decimal value
        decimal_num += num # Add the decimal value to the total
        idx -= 1
        power += 1
    return decimal_num

#  time complexity will be O(n) where n is the number of bits in the binary number
#  space complexity will be O(1) because we are using a constant amount of space to store the decimal number and the power variable, regardless of the size of the input binary number. The space required does not grow with the size of the input, hence it is O(1).