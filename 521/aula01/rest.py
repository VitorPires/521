import requests
import json
class Rest():
    def listar_usuario(self):
        rest = requests.get("http://127.0.0.1:5000/usuarios/").json()
        print(rest["usuarios"])
        for i in rest["usuarios"]:
            print(i["nome"],i["id"] )
    def add_usuarios(self):
        cabecalho = {"content-type":"application/json"}
        dados = json.dumps({"nome": "mariana", "email": "mariana1@mariana4linux"})
        rest = requests.post("http://127.0.0.1:5000/usuarios/", data=dados, headers=cabecalho)._content
        print(rest)
    def alterar_usuario(self):
        cabecalho = {"content-type": "application/json"}
        dados = json.dumps({"nome": "marianaalbano", "email": "mariana2@mariana4linux"})
        rest = requests.put("http://127.0.0.1:5000/usuarios/9999/", data=dados, headers=cabecalho).status_code
        if rest ==200:
            print("alterado com sucesso")
        else:
            print("Faio")
    def deletar_user(self):
        rest = requests.delete("http://127.0.0.1:5000/usuarios/8/").json()




rest = Rest()
print(rest.listar_usuario())
#rest.add_usuarios()
#rest.alterar_usuario()
rest.deletar_user()


'''
x =  { 'curso': 'python',
       'escola':'4linux',
       'aluno':['Vitor','Cesar','Pires',['teste']]
     }
print (x['aluno'][3])
print (type(x))
print (x.keys())
print (x.values())
x['escola'] = 'microsoft'
print (x)
    '''