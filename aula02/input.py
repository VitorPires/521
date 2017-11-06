animais = []
while True:
    escolha = input('Digite 1 para inserir\n'
                   'Digite 2 para mostrar\n'
		   'Digite 3 para parar\n')
    if escolha == '1':
        nome = input('Digite nome de um animal>> ')
        animais.append(nome)
    elif escolha == '2':
        print(animais)
    else:
        break


