def remove_duplicates(s):
	s = sorted(s)
	n = len(s)
	if(n<1):
		return s
	c1 = s[0]
	curr_pointer = 0
	for i in range(1,n):
		if(s[i]==c1): #if the current element is equal to the stored element
			continue
		else:
			s[curr_pointer] = c1
			curr_pointer+=1
			c1=s[i]
	if(s[-1]==c1):
		s[curr_pointer] = c1
		curr_pointer += 1
	s[curr_pointer] = '\0'
	return s

print(remove_duplicates('aabbcdef'))

str = 'aabbcdef'
a = set(str)
print(a)

