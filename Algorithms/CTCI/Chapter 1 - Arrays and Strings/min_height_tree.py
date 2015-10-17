class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self,i):
		while i//2 > 0:
			if(self.heapList[i//2]>self.heapList[i]):
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[i//2]
				self.heapList[i//2] = tmp
			i=i//2
	def insert(self,k):
		self.heapList.append(k)
		self.currentSize += 1
		self.percUp(self.currentSize)
	def percDown(self,i):
		while(i*2<self.currentSize):
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc
	def minChild(self,i):
		if i*2+1>self.currentSize:
			return i*2
		else:
			if self.heapList[i*2+1] < self.heapList[i*2]:
				return self.heapList[i*2+1]
			else:
				return self.heapList[i*2]
	def delMin(self,i):
		retVal = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.percDown(1)
	def buildHeap(self,alist):
		i = len(alist)//2
		print(i)
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while(i>0):
			self.percDown(i)
			i=i-1


tree = BinHeap()
tree.buildHeap([1,2,3,5,6,7,8])

tree.insert(4)
print(tree.heapList)