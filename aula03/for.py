listagem_cursos = [
 {
   'nome':'mariana',
    'cursos':['Python']
 },
 { 
   'nome':'Joao',
     'cursos':['Python','InfraAgil']
 }

]
j=0

curso = input('Que curso deseja buscar: ') 
for i in listagem_cursos:
  for k in i['cursos']:
    if curso == k:
      print (i['nome'])



#   print(listagem_cursos[j]['cursos'])
#   if 'python' == listagem_cursos[j]['cursos']:
#     print (listagem_cursos[j]['nome'])
#   j+= 1
#    print(listagem_cursos[i]['nome'])
#    i+=1

#print(listagem_cursos[0]['cursos'])
