from functools import reduce

def prod(L):
	def fn(x,y):
		return x * y
	return reduce(fn,L)
