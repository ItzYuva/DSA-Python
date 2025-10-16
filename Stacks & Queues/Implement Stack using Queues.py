'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
'''

# ---------------------------------------------
# Stack Implementation using Two Queues (deque)
# ---------------------------------------------
# Problem: Implement a Last-In-First-Out (LIFO) stack
#           using only the standard operations of a queue:
#           - enqueue (append)
#           - dequeue (popleft)
#           - size
#           - empty
# ---------------------------------------------

from collections import deque   # Import deque because list.pop(0) is O(n),
                                # while deque.popleft() is O(1) — perfect for queues.

class MyStack(object):

    def __init__(self):
        # Initialize two queues
        # q1 → main queue (acts like our stack)
        # q2 → helper queue (used during push)
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        Steps:
        1. Add the new element to q2.
        2. Move all elements from q1 → q2 (so the new element is at the front).
        3. Swap q1 and q2.
        """
        # Step 1: enqueue x into helper queue q2
        self.q2.append(x)

        # Step 2: move all elements from q1 to q2
        # This ensures the new element (x) comes to the front
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Step 3: swap q1 and q2
        # Now q1 has the correct stack order, and q2 is empty for next use
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        Removes and returns the top element of the stack.
        Since the top element is always at the front of q1,
        just dequeue from q1.
        """
        return self.q1.popleft()

    def top(self):
        """
        Returns the top element of the stack without removing it.
        The top of stack is always the first element (front) of q1.
        """
        return self.q1[0]

    def empty(self):
        """
        Returns True if the stack is empty, otherwise False.
        """
        return len(self.q1) == 0
    


# ------------------------------------------------------------
# Stack Implementation using One Queue (Deque)
# ------------------------------------------------------------
# Problem: Implement a Last-In-First-Out (LIFO) stack
#           using only the standard operations of a queue:
#           - enqueue (append)
#           - dequeue (popleft)
#           - size
#           - empty
#
# Concept:
#   Normally, a queue follows FIFO (First In, First Out)
#   while a stack follows LIFO (Last In, First Out).
#
#   To simulate stack behavior using just one queue:
#   → Each time we push a new element, we enqueue it
#     and then rotate the queue so the new element
#     becomes the FRONT (top) of the stack.
#
#   This way, pop() and top() can just access the front element.
# ------------------------------------------------------------

from collections import deque   # deque gives O(1) append and popleft operations

class MyStack(object):

    def __init__(self):
        # Initialize a single queue (q1)
        self.q1 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        Steps:
        1. Enqueue x into the queue.
        2. Rotate the queue (len(q1)-1) times so that
           the new element moves to the FRONT.
        """
        self.q1.append(x)          # Step 1: enqueue x (add to back)
        n = len(self.q1)           # Current size of the queue

        # Step 2: rotate elements behind x
        # For example:
        # Before rotation: [1, 2, 3]
        # After pushing 3: [1, 2, 3]
        # After rotation:  [3, 1, 2]
        for i in range(0, n-1):
            self.q1.append(self.q1.popleft())

    def pop(self):
        """
        Removes and returns the top element of the stack.
        Since the newest element is always at the front,
        we just dequeue (popleft).
        """
        return self.q1.popleft()

    def top(self):
        """
        Returns the top element of the stack without removing it.
        The top of stack is the front element of the queue.
        """
        return self.q1[0]

    def empty(self):
        """
        Returns True if the stack is empty, otherwise False.
        """
        return len(self.q1) == 0
