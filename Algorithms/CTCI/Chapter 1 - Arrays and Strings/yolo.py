def binmatchpattern(pattern):
	result = []1
	for i in pattern:
		if i == '?':
			result = [result[j]+'0' for j in range(len(result))] + \
							 [result[j]+'1' for j in range(len(result))]
		else:
			if(result == []):
				result.append(i)
			else:
				result = [result[j]+i for j in range(len(result))]
	return result

print(binmatchpattern('11???01111'))

