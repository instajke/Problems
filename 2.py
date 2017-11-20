def calcFibNum(x, y) :
	return x + y;

x = 1

y = 1

total = 0

while calcFibNum(x, y) <= 4000000 :
	
	temp = calcFibNum(x, y);

	if temp % 2 == 0 :
		total += temp;

	x, y = y, x
	y = temp
	print(x, y)

print(total);
