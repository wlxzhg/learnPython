# -*- coding: utf-8 -*-
names = ['Michael','Bob','Tracy']
for name in names:
	print("hello,",name)

sum = 0;
for x in[1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x;
print(sum)

sum = 0;
num = list(range(101))
for x in num:
	sum = sum + x;
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

sum = 0
n = 100
while n >= 0:
	sum = sum + n
	n = n - 2
print(sum)