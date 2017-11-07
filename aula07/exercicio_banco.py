import MySQLdb

menu = """
[MENU]

1) Login
2) Inserir
3) Atualizar
4) Deletar
5) Mostrar
6) Parar
Insira uma opção: """
con = MySQLdb.connect(
        host="localhost",
        db="projetos",
        user="admin",
        passwd="4linux@"
    )

cur = con.cursor()
while True:
    opcao = int(input(menu))
    if opcao ==2:
        nome= input('Digite nome ')
        email= input('Digite email')


    ### INSERT
        cur.execute("INSERT INTO clientes(nome,endereco) \
                     VALUES('%s','%s')" %(nome,email)
                )
    cur.execute("SELECT * FROM clientes")
    registros = cur.fetchall()

    ###UPDATE
    if opcao == 3:
        alterar = input('Digite nome para alterar')
        nome = input('Digite novo nome')
        email = input('Digite novo email')
        cur.execute("UPDATE clientes SET nome='%s', endereco='%s' \
                                    WHERE nome='%s'" % (nome,email,alterar))
    ###DELETE
    if opcao == 4:
         nome = input('Quem deseja deletar: ')
         cur.execute("DELETE FROM clientes WHERE nome='%s'"% nome)
    elif opcao ==6:
        break
con.commit()
cur.close()
con.close()

