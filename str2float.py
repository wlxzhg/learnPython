# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
	if(isinstance(s,str) == False):
		return
	def f1(x,y):
		return x * 10 + y
	def f2(c):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}[c]
	L = list(map(f2,s))
	n = 0
	while n < len(L):
		if(L[n] == '.'):
			break;
		n = n + 1
	L1 = L[0:n]
	L2 = L[n+1:]
	if(L2 == []):
		L2 = [0,0]
	if(L1 == []):
		L1 = [0,0]
	return reduce(f1,L1) + reduce(f1,L2) / pow(10,len(L2))
