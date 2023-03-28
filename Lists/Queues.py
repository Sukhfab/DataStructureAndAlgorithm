"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""


class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        '''
        Add a new element at the end of list (end of queue)
        '''
        self.storage.append(new_element)
        return

    def peek(self):
        '''
        look at the first elemene of queue and return it
        '''
        return self.storage[0]
        pass

    def dequeue(self):
        '''
            remove the first element of queue and return it (first in first out like in a coffee shop queue)
        '''
        first_element =self.storage[0]
        self.storage.pop(0)
        return first_element


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())