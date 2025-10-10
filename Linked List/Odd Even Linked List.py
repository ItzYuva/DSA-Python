'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
'''


def oddEvenList(head):
    # if the list is empty or has only one node, return as is
    if not head or not head.next:
        return head

    # Initialize pointers:
    # odd -> first node
    # even -> second node
    # evenStart -> store the head of even list to connect later
    odd = head
    even = head.next
    evenStart = even

    # Traverse the list while there are available even and odd nodes
    while even and even.next:
        # Connect current odd node to the next odd node
        odd.next = even.next
        odd = odd.next  # Move odd pointer to next odd node

        # Connect current even node to the next even node
        even.next = odd.next
        even = even.next  # Move even pointer to next even node

    # After the loop, connect the last odd node to the first even node
    odd.next = evenStart

    # Return the head of the rearranged list
    return head
