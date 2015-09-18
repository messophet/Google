import timeit
import inspect

def trace(f):
  def g(x):
    print(f.__name__, x)
    value = f(x)
    print('return', repr(value))
    return value
  return g

def memoize(f):
	cache = {}
	def g(x):
		if x not in cache:
			cache[x] = f(x)
		return cache[x]
	return g

def time(f):
	def g(x):
		start = timeit.timeit()
		end = timeit.timeit()
		print('time', repr(end-start))
	return g

@memoize
@trace
@time
def fib(n):
	if n is 0 or n is 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print(fib(4))
print(inspect.getsource(sorted))
