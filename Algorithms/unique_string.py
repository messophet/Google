def pairs(s):
	c = len(s)
	for i in range(len(s)):
		yield s[i], s[(i+1)%c]
	
def allunique(s):
	seq = sorted(s)
	for (c1,c2) in pairs(seq):
		if c1==c2:
			return False
	return True

if __name__ == "__main__":
	word = 'abcdefg'
	print('allunique({}): {}'.format(word, allunique(word)))

