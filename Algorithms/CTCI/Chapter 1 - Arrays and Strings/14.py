def isAnagram(s1,s2):
	return sorted(s1) == sorted(s2)

print(isAnagram('abc','bac'))