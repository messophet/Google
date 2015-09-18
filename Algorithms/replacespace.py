def replaceString(st):
	charList = []
	for char in st:
		if char == ' ':
			char = '%20'
		charList.append(char)
	return ''.join(charList)

abc = 'he l l o h o w a re y o u'
print('{}'.format(replaceString(abc)))
