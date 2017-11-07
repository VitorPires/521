boletim = [
           {'nome':'Gabriel','notas':[1,4,5,6]},

       {'nome':'Joao','notas':[3,5,7,7]}

]
media = 0
aluno = input('Digite nome do aluno: ')
for i in boletim:
  if i['nome']==aluno:
    print(i['notas'])
    for j in i['notas']:
       media +=j
       media_final = media/len(i['notas'])
print(media)
print(media_final)


