alunos=[]
def inserir(nome,email):
  global alunos
  alunos.append(
            {
                "nome": nome,
                "email": email
            }
        )
  print(alunos[:])
  return(alunos[:])

def mostrar(aluno):
  global alunos
  for a in alunos:
    if a['nome'] == aluno:
      return(a['email'])
def entra_sistema(user,senha):
  cad_user=user
  cad_senha=senha 
  cadastro = {'nome':'Vitor','senha':1234567}
  for i in cadastro:
    if i['nome']== cad_user:
      if i['senha']==cad_senha:
        principal()
    else:
      print('Usuario invalido')
def principal():
  while True:
    menu = """
    [MENU]

    1) Inserir
    2) Mostrar
    3) Sair
    Insira uma opção: """
    opcao =int(input(menu))
    if opcao ==1:
      nome = input('Digite nome: ')
      email  = input('Digite email:')
      inserir(nome,email)

    elif opcao==2:
      aluno = input("Informe o nome do aluno: ")
      print(mostrar(aluno))
    else:
      break
user = input('Digite usuario: ')
senha = input('Digite senha: ')
entra_sistema(user,senha)