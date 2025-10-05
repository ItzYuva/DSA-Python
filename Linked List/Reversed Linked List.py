'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
'''
from Common import *


def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    # Step 1: Initialize two pointers
    # 'prev' will keep track of the previous node (starts as None since the new tail's next should be None)
    prev = None
    # 'curr' will traverse through the list, starting from the head
    curr = head

    # Step 2: Traverse the list until we reach the end (curr becomes None)
    while curr is not None:
        # Temporarily store the next node before changing the link
        nxt = curr.next
        
        # Step 3: Reverse the link
        # Instead of pointing to the next node, make 'curr' point to the previous node
        curr.next = prev

        # Step 4: Move the 'prev' and 'curr' pointers one step forward
        prev = curr        # 'prev' now becomes the current node
        curr = nxt         # 'curr' moves ahead to the next node (saved earlier)

    # Step 5: At the end of the loop, 'prev' will point to the new head of the reversed list
    return prev

head = createLLFromList([1,2,3,4,5])
print_LL(reverseList(head))