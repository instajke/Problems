
def checkIsFactorPrime(x) : 
	tmp = 2
	while tmp < x :
		if (x % tmp == 0) :
			return False
		tmp += 1
	return True

i = 0;
j = 2;
prime = 1;

while True :
	if checkIsFactorPrime(j) :
		i += 1
		if i == 10001 :
			print(j)
			break
	j += 1
