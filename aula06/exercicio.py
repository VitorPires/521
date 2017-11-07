# trocar para csv
import json,csv
alunos = [

]

# trocar para json

logado = False


menu = """
[MENU]

1) Login
2) Inserir
3) Mostrar
4) Sair
Insira uma opção: """

def is_logged(*args):
    def func():
        if logado:
            return args[0]()
        else:
            return print('Permissao negada')

    return func

#@is_logged
def inserir_aluno():
    nome = input("Insira o nome: ")
    email = input("Insira o email: ")
    with open('alunos.csv','a') as csvfile:
        arquivo = csv.writer(csvfile,delimiter= ';')
        arquivo.writerow([nome,email])


#@is_logged
def mostrar_aluno():
    global alunos

    aluno = input("Informe o nome do aluno: ")
    with open('alunos.csv','r') as csvfile:
        arquivo= csv.reader(csvfile,delimiter= ';')
        for a in arquivo:
         if a[0] == aluno:
            return a[1]

def login():
    global logado
    with open('banco.json', 'r')as file:
        banco = json.loads(file.read())

    login = input("Insira o login:")
    senha = input("Insira a senha:")

    for b in banco:
        if login == b["login"] and senha == b["senha"]:
            logado = True
            return True
        else:
            return False



while True:
    opcao = int(input(menu))

    if opcao == 1:
        if login():
            print("Login realizado com sucesso!")
        else:
            print("Usuario e/ou senha invalido")
    elif opcao == 2:
        inserir_aluno()
    elif opcao == 3:
        print(mostrar_aluno())
    elif opcao == 4:
        break
    else:
        print("Nenhuma opção válida")
