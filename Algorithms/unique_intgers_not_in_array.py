#http://www.careercup.com/question?id=5633053969874944
#n unique integers
#0 <= x_i < 2*n
#print all numbers that are not in this array
#findmissing([0,2,4]) --> [1,3,5]
#sum(0+2+4) = 6
#2*n=6 (n=3), and sum (0..5) = 0+1+2+3+4+5 = 15
#15-6=9
#len([0,2,4]) = 3
#2*n = 6
#3 numbers missing
#x+y+z = 9
#1+3+5
#1+2+6

#[0,2,4] -> 0*2*4 ... 2*4 = 8
#2*n = 6 (0->5) .. 0*1*2*3*4*5 = 120
#start with 5... 120/5 = 24
#24 > 8, therefore 5 is not part of the list
#6 < 8, therefore 4 is part of the list
#24/3, 8 = 8, therefore 3 is not part of the list
#12/2 = 6 < 8, therefore 2 is part of the list
#12/1 = 12 > 8, therefore 1 is not part of the list

def findmissing(array):
	#trivial cases
	if(len(array) < 1):
		return []
	if(len(array) == 1):
		if(array[0] == 0):
			return [1]
		else:
			return [0]
	#stores output
	outList = []
	if(array[0]==0):
		#don't want to include 0 in the multiplication
		multArr = reduce(lambda x, y: x*y, array[1:])
	else:
		multArr = reduce(lambda x, y: x*y, array)
		outList.append(0)

	#multiply all numbers from 1 to 2*n
	maxTotal = reduce(lambda x, y: x*y, list(range(1,2*len(array))))

	for i in range(2*len(array)-1,0,-1):
		if(maxTotal/i >= multArr):#keep dividing by the largest factor
			outList.append(i)
			maxTotal = maxTotal/i
	return outList


array = [0,2,4]
array = [1]
array = [0,2]
print(findmissing(array))


