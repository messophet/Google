def f(n, d):
  x = n * 9
  z = x
  k = 1
  f = float(n)/d
  while z % d:
      z = z * 10 + x
      k += 1
      if(k>100):
      	if abs(int(f)-f) < 0.00000001:
      	    return f
      	else:
      	    return n
  return ('{}.({})'.format(n/d,str(z/d).rjust(k,'0')))

print(f(1,2))
