l =[]
var1, var2, var3 = map(int, input().split())
l.append(var1)
l.append(var2)
l.append(var3)

#buuble sort menor para maior:

def bubblesort_low(list):
	for i in range(len(list)):
		for j in range(1, len(list) -i):
			if (l[j] < l[j-1]):
				l[j-1] , l[j] = l[j], l[j-1]

#bubble sort maior para menor:	
bubblesort_low(l)
print(*l, sep = '\n')
print('')

def bubblesort_high(list):
	for i in range(len(list)):
		for j in range(1, len(list)-1):
			if (l[j]> l[j-1]):
				l[j-1] , l[j] = l[j], l[j-1]

print(var1,var2,var3, sep = '\n')
