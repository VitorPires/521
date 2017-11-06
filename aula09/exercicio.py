from pymongo import MongoClient

## CONEXAO
client = MongoClient('localhost')
db = client['dexterops']
while True:
    opcao = int(input("Digite 1 para inserir,2 para buscar,3 para remover,4 para alterar,5 para sair"))
    if opcao == 1:
        nome = input("Digite nome ")
        email = input(("Digite email "))
        ## INSERT
        fila = {"email": email, "nome": nome}
        id = db.fila.insert(fila)
        if id:
            print("Inserido com sucesso")
        elif id:
            print("Inserido com erro")
    elif opcao == 2:
        nome = input("Digite nome ")
        item = db.fila.find({"nome": nome})
        for i in item:
            print(i["email"])
    elif opcao == 3:
        nome = input("Digite nome ")
        if db.fila.remove({"nome": nome}):
            print("Registro removido")
    elif opcao == 4:
        nome = input("Digite nome para alterar ")
        novo_nome = input("Digite novo nome")
        novo_email = input("Digite novo email")
        dados = {
            "$set": {"nome": novo_nome,"email":novo_email}
        }
        result = db.fila.update({"nome": nome}, dados)
    if opcao == 5:
        break
