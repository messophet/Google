class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def enqueue(self, item):
		self.items.append(item) #insert at the back of the list (creates LIFO structure)
	def dequeue(self):
		return self.items.pop() #pop last item of list
	def size(self):
		return len(self.items)
