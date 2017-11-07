import csv

with open('alunos.csv','r') as csvfile:
    arquivo=csv.reader(csvfile,delimiter=';')
    for a in arquivo:
        print(a)

with open('alunos.csv', 'a',newline='') as csvfile:
    arquivo=csv.writer(csvfile,delimiter= ';')
    arquivo.writerow(['teste']*5)
    arquivo.writerow(['Vitor']*15)
