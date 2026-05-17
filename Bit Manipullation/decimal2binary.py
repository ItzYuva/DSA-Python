# write the code to convert decimal to binary

def decimal2binary(num:int)->str:
    result = ""
    while num>0:
        if num % 2==0:
            result += "1"
        else:
            result += "0"
        num = num//2
    return result[::1]

#  time complexity will be O(log n) where n is the input number
#  space complexity will be O(log n) where n is the input number
#  How space complexity is O(log n) ?
#  The space complexity is O(log n) because the number of bits required to represent a decimal number in binary is proportional to the logarithm of the number. For example, a decimal number n can be represented in binary using log2(n) bits. Therefore, the space required to store the binary representation of the number grows logarithmically with respect to the input number.