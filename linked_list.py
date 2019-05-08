# linked list implementation in python


class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while(current.next):
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def get_position(self, position):
		counter = 1
		current = self.head
		if position < 1:
			return None
		while counter <= position and current:
			if counter == position:
				return current
			current = current.next
			counter += 1
		return None

	def insert(self, new_element, position):
		counter = 1
		current = self.head
		if position > 1:
			while(counter <= position and current):
				if counter == position -1 :
					new_element.next = current.next
					current.next = new_element
					break
				counter += 1
				current = current.next
		elif position == 1:
			new_element.next = self.head
			self.head = new_element
		pass

	def delete(self, value):
		current = self.head
		previous = None
		while current.value != value and current.next:
			previous = current
			current = current.next
		if current.value == value:
			if previous:
				previous.next = current.next
			else:
				self.head = current.next
		pass

# creating four Element() object each having some integer value stored in
elem1 = Element(100)
elem2 = Element(99)
elem3 = Element(98)
elem4 = Element(97)

# Creating LinkedList object and appending some elements
linked_list = LinkedList()
linked_list.append(elem4)
linked_list.append(elem3)
linked_list.append(elem2)
linked_list.append(elem1)

# printing first four elements in linked_list
for i in range(1,5):
	print('Element on position ', i, 'is', linked_list.get_position(i).value)
print('\n')
# inserting 2 elements on position 2 and 5

linked_list.insert(Element(25), 2)
linked_list.insert(Element(75), 5)

# printing first 6 elements in linked_list
for i in range(1,7):
	print('Element on position ', i, 'is', linked_list.get_position(i).value)
print('\n')

# deleting last and first elememt

linked_list.delete(97)
linked_list.delete(100)

# pinting first four elements in linked_list
for i in range(1,5):
	print('Element on position ', i, 'is', linked_list.get_position(i).value)
