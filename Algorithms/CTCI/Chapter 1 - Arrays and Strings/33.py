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

class SetOfStacks:
	def __init__(self,stackSize=10):
		self.stacks=[Stack()]
		self.stackSize = stackSize
		self.currStackPointer = 0
	def push(self,item):
		if(self.stacks[self.currStackPointer].size() >= self.stackSize):
			self.stacks.append(Stack())
			self.currStackPointer += 1
		self.stacks[self.currStackPointer].push(item)
	def pop(self):
		if(not self.stacks[self.currStackPointer].isEmpty()):
			return self.stacks[self.currStackPointer].pop()
		else:
			if(self.currStackPointer>0):
				self.currStackPointer -= 1
				return self.stacks[self.currStackPointer].pop()	

setOfStacks = SetOfStacks(2)
setOfStacks.push(2)
setOfStacks.push(3)
setOfStacks.push(4)
setOfStacks.push(5)
setOfStacks.push(6)
print("Popped", setOfStacks.pop())
print("Current Stack", setOfStacks.currStackPointer)
print("Popped", setOfStacks.pop())
print("Current Stack", setOfStacks.currStackPointer)
print("Popped", setOfStacks.pop())
print("Current Stack", setOfStacks.currStackPointer)
print("Popped", setOfStacks.pop())
print("Current Stack", setOfStacks.currStackPointer)
