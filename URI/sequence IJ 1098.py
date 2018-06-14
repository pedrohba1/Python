i = 0.00
x = 0.00
while(i <=1.8):
	for j in range(1,4):	
		
		
		if( i%1 == 0):
			print("I=%d J=%d" %(i,j+x))
			
		else:
			print("I=%.1f J=%.1f" %(i,j+x))
	i+=0.2
	x+=0.2

i+=0.2
for j in range(1,4):
	print("I=%d J=%d" %(i,j+x))

			