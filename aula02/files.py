#with open('/etc/hosts','r') as f:
#        print(f.read())
#        print(f.readline())
#       print(f.readline())
#with open ('arq01','+a') as f2:
#     f2.write('Novo texto\n')      
#     print(f2.read())

nome = input('Digite seu nome>> ')
if len(nome) <6:
    print('Nome invalido')
    exit(0)
email = input('Digite seu email>> ')
cep = input('digite seu cep>> ')
with open('pedido','a') as f:
    f.write('%s ,%s ,%s ,\n ' % (nome,email,cep))
    #f.write('Nome ' + nome + ' ')
    #f.write('Email ' + email + ' ')
    #f.write('Cep ' + cep + ' ')
    #f.write('\n')
    f.close
linha = int(input('Deseja visualizar que linha>> '))
with open('pedido','r') as f2:
    print (f2.readlines()[linha])  
