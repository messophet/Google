class Stack:
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def isEmpty(self):
		return self.items==[]

class MyQueue:
	def __init__(self):
		self.queue = []


#3 2 1 -stack-> 3 2 1 (LIFO) -stack-> 1 2 3 | push 4 onto s1 -> 4, s2 = 1 2 3 | s1 = 4 3 2 1... now pop and it's in FIFO
#3 2 1 -queue-> 1 2 3 (FIFO)