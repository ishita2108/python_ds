#push into stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):     
	    return self.stack[-1]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())

print("---------------------------------------------------------------")

#pop from stack
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())

print("---------------------------------------------------------------------")

#stack using queue
# Python program to
# demonstrate stack implementation
# using queue module
 
 
from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize = 3)
 
# qsize() show the number of elements
# in the stack
print(stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())

print("-----------------------------------------------------------------------")

#Stack using dequeue
# Python program to
# demonstrate stack implementation
# using collections.deque
 
 
from collections import deque
 
stack = deque()
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 
# pop() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop()) 
# will cause an IndexError
# as the stack is now empty