#easy way, hash it
def all_unique_set(theString):
	toSet = set(theString)
	if(len(toSet)<len(theString)):
		return False
	return True

someString = 'abbcdef' #False
print(all_unique_set(someString))

#(harder) way, sort then check each element with the next
def pairs_generator(theString):
	for i in range(len(theString)):
		yield theString[i] + theString[(i+1)%len(theString)]

def all_unique_iterator(theString):
	sortedString = sorted(theString)
	for (c1,c2) in pairs_generator(sortedString):
		if(c1==c2):
			return False
	return True

print(all_unique_iterator(someString))

