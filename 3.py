def findFactors(x) :
	prime = 2
	while x % prime != 0 :
		prime += 1
	return [prime, int(x / prime)]

def checkIsFactorPrime(x) : 
	tmp = 2
	while tmp != x :
		if (x % tmp == 0) :
			return False
		tmp += 1
	return True

def checkAreFactorsPrime(list) :
	for item in list :
		if checkIsFactorPrime(item) != 1 : 
			return False
	return True

source = 600851475143

factorsList = findFactors(source)

while checkAreFactorsPrime(factorsList) != 1 :
	for item in factorsList :
		if checkIsFactorPrime(item) != True :
			factorsList.remove(item)
			factorsList.extend(findFactors(item))
print(max(factorsList))