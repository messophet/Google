a = [i for i in range(1,27)]
b = [chr(i) for i in range(97,123)]
code = dict(zip(b,a))

targetStr = 'abc def ghi thestring'
sourceStr = 'thestr'

#sourceHash = Hash.getValue(sourceStr)

class Hash:
	def __init__(self):
		self.container = [None]*17
		self.appends = 0
	#def insert(self,key,val):

	#def get(self,key):

	def hash(self,key):
		i = reduce(lambda x, y:x+y, [code[x] for x in key])
		return i

	def __getValue__(self,value):
		return self.hash(value)

a = Hash()
print(a.hash('doe'))