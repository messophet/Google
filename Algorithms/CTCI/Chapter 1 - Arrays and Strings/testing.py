def testSets():
	c = set()
	'''
	Sets cannot contain mutable elements like lists or dictionaries
	They can contain tuples and immutableset elements
	Membership testing
	Removing Duplicates from a sequence
	Standard math operations
	'''
	c.add(4)
	c.add(5)
	c.remove(5)
	if(4 in c):
		print('4 in c')
	if(5 not in c):
		print('5 not in c')
	t = set()
	t.add(5)
	t.add(6)
	print (c | t) #union: elements from both s and t
	print (c & t) #intersection: elements common in c and t
	print (c - t) #difference: elements in c but not in t
	print (c ^ t) #symmetric difference: elements in either c or t but not both (kind of like xor)

testSets()

def quickSort(arr):
	if(len(arr)<=1):
		return arr

	pivot = [i for i in arr if i == arr[0]]
	lesser = [i for i in arr if i < pivot[0]]
	greater = [i for i in arr if i > pivot[0]]

	return quickSort(lesser) + pivot + quickSort(greater)

print(quickSort([1,3,4,5,9,3,5,7,3]))

a = zip(range(27),range(27,54))
b = zip(*a)
print(b[0][26::-9])

testList = [i for i in range(26)]
for idx,val in enumerate(testList):
	print(idx,val)

for idx,val in enumerate(a):
	print(idx,val)

print(reduce(lambda x, y:x+y, testList))
print(map(lambda x:x*2+10,testList))
print(filter(lambda x:x%2,testList))

def mergeSort(arr):
	if(len(arr)>1):
		mid = len(arr)/2
		lefthalf = arr[:mid]
		righthalf = arr[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k] = lefthalf[i]
				i=i+1
			else:
				arr[k] = righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			arr[k] = lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			arr[k] = righthalf[j]
			j=j+1
			k=k+1
	return arr

print('Merge Sort:', mergeSort([1,3,4,5,9,3,5,7,3]))
print('Quick Sort: ', quickSort([1,3,4,5,9,3,5,7,3]))

def merge_sort(m):
	if len(m) <= 1:
		return m
	middle = len(m)/2
	left = m[:middle]
	right = m[middle:]

	left=merge_sort(left)
	right=merge_sort(right)

	return list(merge(left,right))

def merge(left,right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if(left[left_idx] <= right[right_idx]):
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return result

print('Merge Sort:', merge_sort([1,3,4,5,9,3,5,7,3]))


def merge_sort(m):
	if(len(m)<=1):
		return m
	mid = len(m)/2
	left = m[:mid]
	right = m[mid:]

	left=merge_sort(left)
	right=merge_sort(right)
	return list(merge(left,right))

def merge(left,right):
	result = []
	left_idx, right_idx = 0,0
	while left_idx < len(left) and right_idx < len(right):
		if(left[left_idx]<=right[right_idx]):
			result.append(left[left_idx])
			left_idx+=1
		else:
			result.append(right[right_idx])
			right_idx+=1
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return result

a = 1
















def merge_sort(arr):
	if(len(arr)<2):
		return arr
	middle = len(arr)/2
	left = arr[:middle]
	right = arr[middle:]

	left=merge_sort(left)
	right=`merge_sort(right)

	return list(merge(left,right))

def merge(left,right):
	result=[]
	left_idx, right_idx = 0,0
	while(left_idx < len(left) and right_idx < len(right)):
		if(left[left_idx] <= right[right_idx]):
			result.append(left[left_idx])
			left_idx+=1
		else:
			result.append(right[right_idx])
			right_idx+=1
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return result

print(merge_sort([1,9,7,3,5,7,2,7,3]))
