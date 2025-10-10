'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]

Input: head = [1,2,3,4]
Output: [1,2,4]
'''


def deleteMiddle(self, head):
    # If the list is empty or has only one node,
    # there is no "middle" — so return None (empty list)
    if head is None or head.next is None:
        return None

    # Initialize slow and fast pointers
    slow = head         # moves 1 step at a time
    fast = head         # moves 2 steps at a time
    prev = None         # will keep track of node before slow

    # The fast pointer moves twice as fast as slow.
    # When fast reaches the end, slow will be at the middle node.
    while fast and fast.next:
        prev = slow          # store the node before slow
        slow = slow.next     # move slow by 1
        fast = fast.next.next  # move fast by 2

    # Now 'slow' points to the middle node.
    # To delete it, link the previous node to slow's next node.
    prev.next = slow.next

    return head
