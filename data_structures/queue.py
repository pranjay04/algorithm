# Implementation of Queue using lists in python


class Queue(object):
    def __init__(self):
        self.store = []

    def enqueue(self, new_element):
        self.store.insert(0, new_element)

    def peek(self):
        return self.store[-1]

    def dequeue(self):
        return self.store.pop()


# a Queue() instance
queue = Queue()

# test cases
queue.enqueue(45)
queue.enqueue(46)
queue.enqueue(47)



print(queue.peek())
print(queue.dequeue())

queue.enqueue(48)

print(queue.dequeue())
print(queue.peek())
