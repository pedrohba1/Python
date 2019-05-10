import sys


#instruções mais simples primiero:
#1- guardar os argumentos:
print ("This is the name of the script: ", sys.argv[0])
print ("Number of arguments: ", len(sys.argv))
print ("The arguments are: " , str(sys.argv))


#2- executar os argumentos no terminal
#para isso eu preciso desse módulo subprocess e dessa função chamada call

from subprocess import call
for x in range (1, len(sys.argv)):
	call(sys.argv[x])
