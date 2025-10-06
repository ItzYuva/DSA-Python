'''
Given the head of a singly linked list, find the length of the loop in the linked list if it exists. Return the length of the loop if it exists; otherwise, return 0.

A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos is used to denote the index (0-based) of the node from where the loop starts.

Note that pos is not passed as a parameter.

Example 1:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
Output: 4
Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.

Example 2:
Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
Output: 0
Explanation: No loop is present in the linked list.
'''

def findLengthOfLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # There is a loop, now find its length
            count = 1
            fast = fast.next
            while slow != fast:
                fast = fast.next
                count += 1
            return count
    return 0
