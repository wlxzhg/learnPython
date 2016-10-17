#装饰器学习
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('begin call %s():' % func.__name__)
		func(*args,**kw)
		print('end call %s():' % func.__name__)
	return wrapper

@log
def now():
	print('2016-10-16')

def log1(arg):
	func = arg
	if(isinstance(arg,str)):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (arg,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decorator
	else:
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('begin call %s():' % func.__name__)
			func(*args,**kw)
			print('end call %s():' % func.__name__)
		return wrapper

#now1 = log1(now1)
@log1
def now1():
	print('now1:2016-10-17')

#now2 = log('execute')(now2)
@log1('execute')
def now2():
	print('now2:2016-10-17')