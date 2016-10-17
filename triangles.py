def triangles():
	L = [1]
	length = 1
	while(True):
		yield L		
		n = 1
		tempL = [1]
		while n < length:
			tempL.append(L[n-1]+L[n])
			n = n + 1
		tempL.append(1)
		L = tempL
		length = length + 1
		

