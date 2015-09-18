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

compress = "aaabbbcccccccd"
decompress = simpleCompress(compress)
print('{}'.format(simpleCompress(compress)))

def decompressSimple(st):
	outstring=[]
	lastchar=""
	for char in st:
		if(char.isdigit()):
			for i in range(0,int(char)):
				outstring.append(lastchar)
		else:
			lastchar=char
	outstring=''.join(outstring)
	return outstring

print('{}'.format(decompressSimple(decompress)))
