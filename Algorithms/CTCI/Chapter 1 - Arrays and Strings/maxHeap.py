#Binary Heap (Max)
#(max) node is at the top (root)
#from __future__ import division

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def insert(self, value):
		if(self.currentSize==0):
			self.heapList[1] = value
		else:
			self.heapList.append(value)
			self.currentSize += 1
			self.percUp(self.currentSize)

	def percUp(self,i):
		while(i/2 > 0):
			if(self.heapList[i/2] < self.heapList[i]):
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[i/2]
				self.heapList[i/2] = self.heapList[i]
			i = i/2

	def percDown(self,i):
		while(i*2<self.currentSize):
			m = self.maxChild(i)
			if(self.heapList[i] <= self.heapList[m]):
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[m]
				self.heapList[m] = tmp
			i = m

	def delMax(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.percDown(1)
		return retval

	def maxChild(self,i):
		if(i*2+1>self.currentSize):
			return i*2
		if(self.heapList[i*2+1] >= self.heapList[i*2]):
			return i*2+1
		else:
			return i*2

	def buildHeap(self,alist):
		l = len(alist)/2
		print(l)
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while(l > 0):
			self.percDown(l)
			l=l-1

maxHeap = BinHeap()
maxHeap.buildHeap([1,2,3,4,5,6,7,8,9,55,12,13,15,19,17])
[maxHeap.delMax() for i in range(6)]
print(maxHeap.heapList)