'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2,3,4]
Output: false
'''


def isPalindrome(head):
    # Step 1: Use slow and fast pointers to find the middle of the linked list
    slow = head          # slow moves one step at a time
    fast = head          # fast moves two steps at a time
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # When this loop ends:
    #   - 'slow' will point to the middle node (for odd length)
    #   - or to the start of the second half (for even length)

    # Step 2: Reverse the second half of the linked list (starting from 'slow')
    prev = None
    while slow:
        nxt = slow.next       # temporarily store the next node
        slow.next = prev      # reverse the link direction
        prev = slow           # move 'prev' one step forward
        slow = nxt            # move 'slow' one step forward
    # After this loop:
    #   - 'prev' points to the head of the reversed second half

    # Step 3️: Compare the first half and the reversed second half
    left = head               # start from the beginning of the list
    right = prev              # start from the beginning of the reversed half
    while right:              # only need to traverse the reversed (right) half
        if left.val != right.val:
            return False      # mismatch found → not a palindrome
        left = left.next
        right = right.next
    # If the loop completes, all corresponding nodes matched

    return True

