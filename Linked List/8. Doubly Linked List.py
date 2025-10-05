class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

def createDLLFromList(l1):
    head = None
    tail = None

    for value in l1:
        newNode = Node(value)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            newNode.prev = tail
            tail = newNode

    return head, tail


def insert_at_beginning(head, tail, value):
    newNode = Node(value)
    if head is None:
        head = tail = newNode
    else:
        newNode.next = head
        head.prev = newNode
        head = newNode

    return head, tail

def insert_at_end(head, tail, value):
    newNode = Node(value)
    if head is None:
        head = newNode
        tail = newNode
    else:
        newNode.prev = tail
        tail.next = newNode
        tail = newNode

    return head, tail

def print_forward(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

def print_backward(tail):
    temp = tail
    while temp is not None:
        print(temp.data, end=" <-> ")
        temp = temp.prev
    print("None")



l1 = [1,2,3,4,5]
head, tail = createDLLFromList(l1)
print_forward(head)
print_backward(tail)

# head, tail = insert_at_beginning(head, tail, 0)
# head, tail = insert_at_beginning(head, tail, 1)
# head, tail = insert_at_beginning(head, tail, 2)
# print_forward(head)
# print_backward(tail)
# head, tail = insert_at_end(head, tail, 3)
# head, tail = insert_at_end(head, tail, 4)
# print_forward(head)
# print_backward(tail)