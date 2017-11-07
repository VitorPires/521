import psycopg2
con= psycopg2.connect('host=127.0.0.1 dbname=projeto user=admin password=4linux')
cur = con.cursor()
cur.execute("insert into alunos(nome,email) \
            values('monica','monica@vitor')")
cur.execute("update alunos set email='vitor.pires@aasp.org'\
            where nome= 'monica'")
print(cur.execute('select * from alunos'))
cur.execute("select * from alunos")
registros = cur.fetchall()
print(registros)
con.commit()