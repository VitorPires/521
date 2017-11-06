import csv
alunos=[]
def inserir(nome,email):
    with open('alunos.csv', 'a') as csvfile:
        arquivo = csv.writer(csvfile, delimiter=';')
        arquivo.writerow([nome],[email1])
        arquivo.writerow([email])

    global alunos
    return(alunos[:])

def mostrar(aluno):
  global alunos
  for a in alunos:
    if a['nome'] == aluno:
      return(a['email'])
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

