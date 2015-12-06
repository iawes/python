def triangles():
	L = [1]
	yield L
	L = [1, 1]
	yield L
	while True:
		L1 = L[:-1]
		L2 = L[1:]
#		L.append(1)
#		for i,value in enumerate(L[1:-1]):
#		for i in L1:
#			L3 = [L1[i]+ L2[i]]
		L3 = [L1[i] + L2[i] for i in range(len(L1))]
#		for i in range(len(L1)):
#			L3[i] = L2[i] + L1[i]

		L = [1] +  L3 + [1]
		yield L

#	return 'done' 

n = 0
for t in triangles():
	print(t)
	n = n + 1
	if n == 10:
		break
