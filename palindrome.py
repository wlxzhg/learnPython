# -*- coding: utf-8 -*-
from functools import reduce

def fn(x,y):
	return x * 10 + y
def is_palindrome(n):
	m = n
	L = [0]
	while (n != 0):
		L.append(n % 10)
		n = int(n / 10)
	return reduce(fn,L) == m