segundos = int(input())


minutos = segundos/60
horas = minutos/60
minutos = minutos%60
segundos = segundos%60

print("%d:%d:%d" %(horas, minutos,segundos))