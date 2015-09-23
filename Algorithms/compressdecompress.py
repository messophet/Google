#aabcccccaaa would become a2blc5a3.

def simpleCompress(st):
	outstring = []
	lastchar = ""
	charcount = 0
	for char in st:
		if char==lastchar:
			charcount+=1
		else:
			if lastchar != '':
				outstring.append(lastchar + str(charcount))
			charcount=1	
			lastchar=char	
	outstring.append(lastchar + str(charcount))
	outstring= ''.join(outstring)
	if len(outstring) < len(st):
		return outstring
	else:
		return st

compress = "aaabbbccccccccccd"
decompress = simpleCompress(compress)
print('{}'.format(simpleCompress(compress)))

def decompressSimple(st):
	outstring=[]
	lastchar=""
	numList= []
	for i in range(0,len(st)):
		if(st[i].isdigit()):
			for j in range(i,len(st)):
				if(st[j].isdigit()):
					numList.append(st[j])
				else:
					break
			num = int(''.join(numList))
			for j in range(0,num):
				outstring.append(lastchar)
			numList = []
		else:
			lastchar=st[i]
	outstring=''.join(outstring)
	return outstring

print('{}'.format(decompressSimple(decompress)))
