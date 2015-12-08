def del_prime(L):
	def is_prime(n):
		if n <= 1:
			return False
		if n == 2:
			return True
		if n % 2 == 0:
			return False

		i = 3

		while i * i <= n:
			if n % i ==0:
				return False
			i += 2
		
		return True
	def not_prime(n):
		return not is_prime(n)

	return filter(not_prime, L )
