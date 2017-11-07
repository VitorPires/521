'''lista = []

while True:
    numeros = int(input("Digite numero "))
    lista.append(numeros)
    if len(lista)==5:
        print(lista)
        break
'''
'''lista = []
while True:
    numeros = int(input("Digite numero "))
    lista.append(numeros)
    if len(lista)==10:
        print(lista[::-1])
        break
'''
'''
notas = []
media = 0
while len(notas)<4:
    nota = int(input("Digite nota "))
    notas.append(nota)
for i in notas:
    print("Nota", i)
    media += (i)/4

print(media)
'''
'''nome2 = "Cesar"
print("%s,%s"% (nome,nome2))'''
'''palavra = input("Digite palavra ")
count = 0
while len(palavra)>10:
    palavra = input("Digite palavra ")
for i in palavra:
  if i !="a" and i !="e" and i != "i" and i != "o" and i != "u":
     count +=1

print(count)'''
'''
lista=[]
lista_par = []
lista_impar = []
while len(lista)<20:
    n=int(input("Digite numero "))
    lista.append(n)
for i in lista:
    if i %2 ==0:
           lista_par.append(i)
    else:
            lista_impar.append(i)
print("Lista completa %s"% lista)
print("Lista impar %s" % lista_impar)
print("lista par %s "% lista_par)
print(len(lista))
print(len(lista_impar))
print(len(lista_par))
'''
'''
import random


def lanca_dado():
    i = 0
    lancamentos = []
    while i < 100:
        lancamentos.append(random.randrange(1, 7))
        i += 1
    return lancamentos

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0

for i in lanca_dado():
    if i == 1:
        count_1+=1

    elif i == 2:
        count_2+=1

    elif i == 3:
        count_3+=1

    elif i == 4:
        count_4+=1

    elif i == 5:
        count_5+=1

    elif i == 6:
        count_6+=1

print("Numero 1 %d" % count_1)
print("Numero 2 %d" % count_2)
print("Numero 3 %d" % count_3)
print("Numero 4 %d" % count_4)
print("Numero 5 %d" % count_5)
print("Numero 6 %d" % count_6)
'''



#while i < n:
  #  print(n*(str(n), ))
    #i +=1
#def imprime(n):
#    return(n * (str(n),))
#print(imprime())'''
'''i=int(0)
def imprime(n):
    global i
    while i < n:
        print(i + 1, end=" ")
        i +=1
imprime(20)
'''
'''
def inverso(n):
    return (n[::-1])


print(inverso(str(8541)))
'''
class Bola():
    def __init__(self):
        def Cor(self,cor):
            self.cor=cor


bola = Bola()
bola.Cor(azul)

