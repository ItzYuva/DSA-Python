'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''

class MyQueue(object):

    def __init__(self):
        # Initialize two stacks:
        # in_stack → used for enqueue (push)
        # out_stack → used for dequeue (pop, peek)
        self.in_stack = []
        self.out_stack = []
    
    def _transfer(self):
        """
        Helper function (internal use only)
        Moves all elements from in_stack to out_stack,
        but only if out_stack is empty.
        This reversal ensures FIFO (queue) order.
        """
        if not self.out_stack:  # Only transfer when out_stack is empty
            while self.in_stack:
                # Pop from in_stack (LIFO order)
                # Push to out_stack (reversed order)
                self.out_stack.append(self.in_stack.pop())
        
    def push(self, x):
        """
        Push element x to the back of the queue.
        Time Complexity: O(1)
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        If out_stack is empty, transfer elements first.
        Time Complexity: Amortized O(1)
        """
        self._transfer()
        return self.out_stack.pop()

    def peek(self):
        """
        Returns the element at the front of the queue without removing it.
        If out_stack is empty, transfer elements first.
        Time Complexity: Amortized O(1)
        """
        self._transfer()
        return self.out_stack[-1]

    def empty(self):
        """
        Returns True if the queue is empty, False otherwise.
        Queue is empty only if both stacks are empty.
        Time Complexity: O(1)
        """
        return not self.in_stack and not self.out_stack
