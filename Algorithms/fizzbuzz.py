#FizzBuzz without modulo

def fizzbuzz(fizz,buzz,iters,upperlimit):
	if(iters==upperlimit):
		return
	if(fizz==3 and buzz==5):
		print('FizzBuzz')
		fizz=0
		buzz=0
	elif(fizz==3):
		print('Fizz')
		fizz=0
	elif(buzz==5):
		print('Buzz')
		buzz=0
	else:
		print(iters)
	fizzbuzz(fizz+1,buzz+1,iters+1,upperlimit)

fizzbuzz(0,0,0,100)
