import MySQLdb
#con= MySQLdb.connect(host='127.0.0.1',
#                     user='admin',
#                     passwd='4linux@',
#                     db= 'projetos')
opcao = int(input('Escolha opcao: '))
if opcao ==1:
    nome= input('Digite nome ')
    email= input('Digite email')
    con = MySQLdb.connect(
        host="localhost",
        db="projetos",
        user="admin",
        passwd="4linux@"
    )

    cur = con.cursor()

    ### INSERT
    cur.execute("INSERT INTO clientes(nome,endereco) \
                     VALUES(%s,%s)" %(nome,email)
                )
'''try:
    con = MySQLdb.connect(
         host="localhost",
         db="projetos",
         user="admin",
         passwd="4linux@"
    )

    cur = con.cursor()

    ### INSERT
    cur.execute("INSERT INTO clientes(nome,endereco) \
                 VALUES('mariana', 'mariana@4linux.com.br')"
    )

    ### UPDATE
    cur.execute("UPDATE clientes SET endereco='gabriel@gabriel' \
                WHERE nome='gabriel'")

    ## DELETE
    # cur.execute("DELETE FROM clientes WHERE nome='mariana'")

    con.commit()
except Exception as e:
    con.rollback()
    cur.close()
    con.close()


### SELECT

try:
    con = MySQLdb.connect(
        host="localhost",
        db="projetos",
        user="admin",
        passwd="4linux@"
    )

    cur = con.cursor()

    ### SELECIONA MAIS DE UM
    cur.execute("SELECT * FROM clientes")
    registros = cur.fetchall()
    print(registros)

    ### SELECIONA APENA UM
    cur.execute("SELECT * FROM clientes WHERE nome='gabriel'")
    registro = cur.fetchone()

    print(registros)

except Exception as e:
    print(e)
    con.rollback()
    cur.close()
    con.close()

### MOSTRA TODOS ENCONTRADOS
for r in registros:
    print('Id: ', r[0])
    print('Nome: ', r[1])
    print('Email: ', r[2])

### MOSTRA APENAS O PRIMEIRO
print('Id: ', registros[0])
print('Nome: ', registros[1])
print('Email: ', registros[2])
'''