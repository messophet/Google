targetString = "banana"
sourceArray = ["bana","apple","banaba","bonanza","banamf"]

def isDiffByOneChar(sourceArray,targetString):
	for strin in sourceArray:
		if(abs(len(strin)-len(targetString))>1):
			continue
		strinSorted = sorted(strin)
		offByOne = True

		if(len(strinSorted)>len(targetString)):
			length = len(targetString)
		else:
			length = len(strinSorted)

		for i in range(length):
			if(strinSorted[i]==targetString[i]):
				if(i==length-1):
					offByOne = True
			else:
				if(offByOne): offByOne = False
				else:
					if(not offByOne):
						break
		if(offByOne): return True
	return False

print(isDiffByOneChar(sourceArray,sorted(targetString)))

