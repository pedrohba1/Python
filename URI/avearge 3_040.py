
x = input()
l = [float(i) for i in x.split()]
lp = [2,3,4,1]
media = 0.0
for i in range(4):
	media += l[i] * lp[i]

media = media/10 

print("Media: %.1f" % media)

if(media>=7.0):
	print("Aluno aprovado.")

if(media<5.0):
	print("Aluno reprovado.")

if(media>=5.0 and media<=6.9):
	print("Aluno em exame.")
	nota = float(input())
	media += nota
	media = media/2
	print("Nota do exame: %.1f" % nota)
	if(media<5.0):
		print("Aluno reprovado.")
		print("Media final: %.1f" % media)
	if(media>= 5.0):
		print("Aluno aprovado.")
		print("Media final: %.1f" % media)




