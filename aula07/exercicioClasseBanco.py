import MySQLdb
class Banco:

    def __init__(self):
        self.con = MySQLdb.connect(
            host="localhost",
            db="projetos",
            user="admin",
            passwd="4linux@"
        )
        self.cur = self.con.cursor()

    def inserir(self,nome,email):

        self.cur.execute("INSERT INTO clientes(nome,endereco) \
                             VALUES('%s','%s')" % (nome, email)
                    )
        self.con.commit()
        self.cur.close()
        self.con.close()
    def alterar(self,nome,email,alterar):
         self.cur.execute("UPDATE clientes SET nome='%s', endereco='%s' \
                                    WHERE nome='%s'" % (nome,email,alterar))

         self.con.commit()
         self.cur.close()
         self.con.close()
    def remover(self,nome):
        self.cur.execute("DELETE FROM clientes WHERE nome='%s'"% nome)
        self.con.commit()
        self.cur.close()
        self.con.close()




banco = Banco()
#banco.inserir('felipe','w@w')
#banco.alterar('carlos','w@w','felipe')
banco.remover('joao')