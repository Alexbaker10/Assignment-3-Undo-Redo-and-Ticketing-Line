class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
'''
1. The stack is the best choice for the use of undo and redo because stack use a Last-in, First-Out data structure. 
So the last thing added to the stack is the first one taken away when an item is removed. So the undo method will take the top item off the stack
and the redo method will add it back to the top of the stack.
2. A queue is better for a help desk application because of its First-In, First Out data structure. If help desk used
a stack to organize tech support requests the newest requests would be at the front of the list leaving older request
to be forgotten and not prioritized. With a queue however the oldest requests would be serviced first.
3. My implementations differ from Pythons built in list because my implementations it built like a linked lsit while 
pythons built in lists use a dynamic array.
'''
