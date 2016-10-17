import math

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

def move(x,y,step,angle=0):
	nx = x + step*math.cos(angle)
	ny = y + step*math.sin(angle)
	return nx,ny

def quadratic(a,b,c):
	if ((not isinstance(a,(int,float))) or (not isinstance(b,(int,float))) or (not isinstance(c,(int,float)))):
		raise TypeError('bad operand type')
	d = b*b-4*a*c
	if d >= 0:
		x1 = (-b + math.sqrt(d)) / (2 * a)
		x2 = (-b - math.sqrt(d)) / (2 * a)
		return x1,x2
	else:
		return

def power(x,n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = x * s
	return s

def enroll(name,gender,age = 6,city = 'Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def movehnt(n,a,b,c):
	if(n == 1):
		print(a + '-' + c)
	else:
		movehnt(n-1,a,c,b)
		print(a + '-' + c)
		movehnt(n-1,b,a,c)

	


		

