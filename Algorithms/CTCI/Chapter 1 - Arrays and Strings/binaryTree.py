class BinaryTree:
	def __init__(self,root=None):
		self.root = root
		self.left = None
		self.right = None
	def insertLeft(self,value):
		if(self.left == None):
			self.left = BinaryTree(value)
		else:
			t = BinaryTree(value)
			t.left = self.left
			self.left = t
	def insertRight(self,value):
		if(self.right==None):
			self.right = BinaryTree(value)
		else:
			t = BinaryTree(value)
			t.right = self.right
			self.right = t
	def getRightChild(self,node):
		return self.right
	def getLeftChild(self,node):
		return self.left
	def setRootValue(self,obj):
		self.root = obj
	def getRootValue(self):
		return self.root

tree = BinaryTree('a')
b = tree.insertRight('b')
c = tree.getRightChild(tree).insertRight('c')
root = tree
while(root.getRightChild(root) != None):
	print(root.getRootValue())
	root = root.getRightChild(root)
print(root.getRootValue())

