# def square(x):
#     return x*x
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

# numbers = [1,2,3,4,5]
# print(list(map(square, numbers)))

# print()

# numbers1 = [2,4,6]
# numbers2 = [3,5,7]

# added_numbers = list(map(lambda x,y:x+y, numbers1, numbers2))
# print(added_numbers)

# print()


#check if array is sorted using recusrion
def checkSorted(l1):
    if len(l1) == 0 or len(l1) == 1:
        return True
    
    if l1[0] >= l1[1]:
        return False
    
    return checkSorted(l1[1:])

l1 = [2,5,8,3,6]
print(checkSorted(l1))
