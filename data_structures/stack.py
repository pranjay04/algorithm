# stack implementation in python using linked list

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next :
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        deleted_element = self.head
        if self.head:
            self.head = self.head.next
            deleted_element.next = None
        return deleted_element

class Stack(object):
    def __init__(self, top = None):
        self.linked_list = LinkedList(top)
    def push(self, new_element):
        self.linked_list.insert_first(new_element)
    def pop(self):
        return self.linked_list.delete_first()

# some elements
elem1 = Element(46)
elem2 = Element(47)
elem3 = Element(789)

# Stack
stack = Stack(elem1)

# test
stack.push(elem2)
stack.push(elem3)

print(stack.pop().value)
print(stack.pop().value)

stack.push(Element(999))
print(stack.pop().value)
print(stack.pop().value)
