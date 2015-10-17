class Hash:
	def __init__(self):
		self.hashTable = [None for x in range(19)]
		self.listPrimes = [11,19,41,97,149,373]
		self.currentPrimePointer = 0
		self.inserts = 0
	def resize(self):
		self.hashTable.extend([None for x in range(self.ListPrimes[currentPointer+1])-range(len(self.hashTable))])
		self.currentPrimePointer += 1
	def insert(self,item):
		if(self.inserts==len(self.hashTable)/2):
			self.resize()
		idx = int(item)%len(self.hashTable)
		if(self.hashTable[idx]==None):
			self.hashTable[idx]=item
		else:
			#conflict resolution
			while(1):
				idx = (idx+3)%len(self.hashTable)
				if(self.hashTable==None):
					self.hashTable[idx]=item
		self.inserts+=1
	def get(self,item):
		idx = int(item)%len(self.hashTable)
		if(self.hashTable[idx]==item):
			return idx
		else:
			while(1):
				idx = (idx+3)%len(self.hashTable)
				if(self.hashTable==item):
					return idx

hashSet = Hash()
hashSet.insert(1)
hashSet.insert(14)
hashSet.insert(144)
hashSet.insert(149)
hashSet.insert(140)
hashSet.insert(141)
hashSet.insert(17)
hashSet.insert(2)
print(hashSet.get(1))
print(hashSet.get(14))
print(hashSet.get(149))
print(hashSet.get(144))
print(hashSet.get(140))
print(hashSet.get(17))
print(hashSet.hashTable)

