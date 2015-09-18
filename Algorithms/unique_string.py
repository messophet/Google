import timeit

#using sets
def allunique(s):
	charTables = set()
	for c in s:
		if c in charTables:
			return False
		charTables.add(c)
	return True

#using yield
def pairs(seq):
	n = len(seq)
	for i in range(n):
		yield seq[i], seq[(i+1)%n]

def allunique2(s):
	start = timeit.timeit()
	strStr = quickSort(s)
	end = timeit.timeit()
	print('QuickSort: {}'.format(end - start))

	start = timeit.timeit()
	strStr2 = sorted(s)
	end = timeit.timeit()
	print('Sorted: {}'.format(end - start))

	for (c1,c2) in pairs(strStr):
		if c1==c2:
			return False
		return True

def quickSort(alist=["a","b","a"]):
	if not alist:
		return []

	pivots = [x for x in alist if x == alist[0]]
	lesser = [x for x in alist if x < alist[0]]
	greater = [x for x in alist if x > alist[0]]

	return quickSort(lesser) + pivots + quickSort(greater)

if __name__ == "__main__":
	words = ('','ariadni')
	for w in words:
		#print('allunique({}): {}'.format(w,allunique(w)))
		print('allunique2({}): {}'.format(w,allunique2(w)))
	#print(quickSort())
