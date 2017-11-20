import operator
import functools
import math

def primeFactors(n):
    
	factors_list = []
    # Print the number of two's that divide n
	while n % 2 == 0:
		factors_list.append(2),
		n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
	for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
		while n % i== 0:
			factors_list.append(i),
			n = n / i
             
    # Condition if n is a prime
    # number greater than 2
	if n > 2:
		factors_list.append(n)

	return factors_list

def callitwhatyouwant(list1, list2) :
	list11 = list(list1)
	list22 = list(list2)

	for i in list1 :
		for j in list2 :
			if i == j and list22.__contains__(j) :
				list22.remove(j)
				break;
	list11.extend(list22)
	return list11

list1 = [1]

list2 = list(range(2, 21))

for item in list2 :
	tmplist = list(list1)
	value_factors = primeFactors(item)
	list1 = callitwhatyouwant(tmplist, value_factors)
	print(list1)

print(functools.reduce(operator.mul, list1, 1))
