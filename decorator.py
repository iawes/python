import functools
import time

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper							 


def log4(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call')
		start = time.clock()
		ret = func(*args, **kw)
		end = time.clock()
		print ret
		print('end call, used: ', end -start)
		return ret
	return wrapper							 

def log2(*text):											 
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper							 
	return decorator												 

def log3(text):											 
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('begin call')
			print('%s %s():' % (text, func.__name__))
			func(*args, **kw)
			print('end call')
		return wrapper							 
	return decorator												 

@log
def now():
	print(u"2015129")

@log2('execute')
def now2():
	print(u"2015122")

@log3('execute')
def now3():
	print(u"2015122")
	
@log4
def now4():
	print(u"2015122")
	ret = "ret is 9."
	return ret

now()
print('%s over\n' %  now.__name__)

now2()
print('%s over\n' %  now2.__name__)

now3()
print('%s over\n' %  now3.__name__)

print 'return value is ' + now4()
print('%s over\n' %  now4.__name__)


s = 0

def f():
	s = 1
	print(s)
	def g():
		s = 2
		print(s)
		return s 
	g()
	print s
	return s + 1

print f()
print s

def log6(args_log):
	if callable(args_log):
		@functools.wraps(args_log)
		def wrapper(*args, **kw):
			print('begin call')
			start = time.clock()
			ret = args_log(*args, **kw)
			end = time.clock()
			print ret
			print('end call, used: ', end -start)
			return ret
		return wrapper							 
	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('%s %s():' % (args_log, func.__name__))
				return func(*args, **kw)
			return wrapper							 
		return decorator												
													
@log6
def now6():
	print(u"2015129")

@log6('execute')
def now7():
	print(u"2015122")

now6()
print('%s over\n' %  now6.__name__)

now7()
print('%s over\n' %  now7.__name__)
