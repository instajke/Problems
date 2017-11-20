
def findPoly():
	i = 999
	j = 999

	result = []
	while i >= 100 :
		while j >= 100 :
			product = i * j
			try1 = str(product)
			try2 = str(product)[::-1]
			if try1 == try2 :
				result.append(product)
			j -= 1
		i -= 1
		j = 999
	return result

print(max(findPoly()))