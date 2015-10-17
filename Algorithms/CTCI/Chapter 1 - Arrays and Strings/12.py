cStyleString = "abcd\0"

def reverse_cStyleString(s):
	return s[-2::-1] + '\0' #begin:end:step so begin at d, end at the beginning, and go back 1 step each time

print(reverse_cStyleString(cStyleString))