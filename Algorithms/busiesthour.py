#solves careercup question:http://www.careercup.com/question?id=5093738684612608

def busiestHour(timeList):
	start = [int(x) for x in timeList[::3]]#get all start times from the list
	end = [int(x) for x in timeList[1::3]]#get all the end times by selecting every third element following the second element
	memory = [int(x) for x in timeList[2::3]]#same as above, start at third element
	zipped = zip(start,end,memory)#zip the results together
	abc=[0]*123125 # create array of 0's to store the memory at each possible time
	for i in zipped:
		for j in range(int(i[0]),int(i[1])+1):
			abc[j]=abc[j]+i[2] #add the amount of memory used along the start-end interval
	return abc.index(max(abc))

log = "100207 100208 2\n100305 100307 5\n100207 100209 4\n111515 121212 3".split() #creates a list
print(busiestHour(log))