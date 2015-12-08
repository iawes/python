def prod(L):
	def multi(x, y):
		return x * y

	return reduce(multi, L) 

print prod([1, 2, 3, 4])
