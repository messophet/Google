#terribly inefficient solution
#needs some work
def print_consecutive(items):
	temp = items[0]
	outstring = []
	for i in range(1,len(items)):
		#if the current number is not consecutive of the previous
		if(items[i]!=items[i-1]+1):
			if(items[i-1]!=temp):
				if(outstring!=[]):
					outstring.append(',')
				outstring.append(str(temp) + '-' + str(items[i-1]))
			else:
				outstring.append(','+str(temp))
			temp = items[i]
	if(items[-1]!=items[-2]+1):
		outstring.append(',' + str(items[-1]))
	else:
		outstring.append(',' + str(temp) + '-' + str(items[-1]))		

	return ''.join(outstring)

print(print_consecutive([1,2,3,5,6,7,8,9,11,15,24,25]))

