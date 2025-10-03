from Common import *

def mergeTwoLists(list1, list2):
    # If the first list is empty, return the second
    if list1 is None:
        return list2
    # If the second list is empty, return the first
    if list2 is None:
        return list1

    # These will be the head and tail of the new merged list
    finalHead = None  
    finalTail = None  

    # Traverse both lists while neither is exhausted
    while list1 is not None and list2 is not None:
        # Compare values of the current nodes in both lists
        if list1.data < list2.data:
            # If merged list is empty, initialize it with list1's node
            if finalHead is None:
                finalHead = list1
                finalTail = list1
            else:
                # Otherwise, attach list1's node to the tail of merged list
                finalTail.next = list1
                finalTail = list1
            # Move list1 forward
            list1 = list1.next
        else:
            # If merged list is empty, initialize it with list2's node
            if finalHead is None:
                finalHead = list2
                finalTail = list2
            else:
                # Otherwise, attach list2's node to the tail of merged list
                finalTail.next = list2
                finalTail = list2
            # Move list2 forward
            list2 = list2.next
    
    # At this point, one list is exhausted.
    # Attach the remaining nodes of the other list.
    if list1 is not None:
        finalTail.next = list1
    if list2 is not None:
        finalTail.next = list2
    
    # Return the head of the merged list
    return finalHead


list1 = createLLFromList([2,5,9,10,17])
list2 = createLLFromList([3,6,7])

print_LL(list1)
print_LL(list2)

finalHead = mergeTwoLists(list1,list2)

print_LL(finalHead)

# https://leetcode.com/problems/merge-two-sorted-lists/description/