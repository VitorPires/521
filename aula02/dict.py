x =  { 'curso': 'python',
       'escola':'4linux',
       'aluno':['Vitor','Cesar','Pires',['teste']]
     }


print (x['aluno'][3])
print (type(x))
print (x.keys())
print (x.values())
x['escola'] = 'microsoft'
print (x)
