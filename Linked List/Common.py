class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data,end="->")
        temp = temp.next

def take_input_better():
    value = int(input("Enter the value of Node :- "))
    head = None
    tail = None
    
    while(value != -1):
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        
        value = int(input("Enter the value of Node :- "))
    
    return head

def createLLFromList(l1):
    head = None
    tail = None
