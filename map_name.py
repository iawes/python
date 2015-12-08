def str2people(L):
	def upper2lower(s):
		t = s.lower()
		return t.capitalize()

	return map(upper2lower, L)


print str2people(["HeLO", "LILI"])
