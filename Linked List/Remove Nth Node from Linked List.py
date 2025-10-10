'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []
'''

def removeNthFromEnd(head, n):
    if not head:
        return None

    temp = head
    # Move temp n steps ahead
    for i in range(n):
        temp = temp.next

    # If temp becomes None, that means we have to remove the head node
    if not temp:
        return head.next

    prev = head
    # Move both pointers until temp reaches the last node
    while temp.next:
        prev = prev.next
        temp = temp.next

    # Skip the target node
    prev.next = prev.next.next

    return head

