

sum_ = 0
i = 0
for i in range(0,2):
	code, units, price = map(float, input().split())
	sum_ += + (units *price)



print("VALOR A PAGAR: R$ %.2f" %(sum_))