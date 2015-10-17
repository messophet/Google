class Stack:
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def size(self):
		return len(self.items)
	def peek(self):
		return self.items[-1]
	def isEmpty(self):
		return self.items==[]

def sortStack(stack):
	tempStack = Stack()
	while(not stack.isEmpty()):
		temp = stack.pop()
		while(not tempStack.isEmpty() and tempStack.peek() > temp):
			stack.push(tempStack.pop())
		tempStack.push(temp)
	return tempStack

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(17)
stack.push(3)
stack.push(9)
stack.push(21)
print(stack.items)

sortedStack = sortStack(stack)
print(sortedStack.items) #sorted






