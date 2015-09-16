def reverse_string(s):
	if(len(s) == 0):
		return ""
	#-1: gets the last char, :-1 gets all the letters up to the last char
	return s[-1] + reverse_string(s[:-1])

if __name__ == "__main__":
	print(reverse_string("hello"))