from pymongo import MongoClient
client = MongoClient('localhost')
db = client['dexterops']
fila = {"servico2":"Intranet","status":0}


id = db.fila.insert(fila)
print(id)
###buscarvarios
#items = db.fila.find()
#for i in items:
#    print(i['_id'])
###buscarum
item = db.fila.find({"_id":id})
for i in item:
    print(i)
##update
dados ={"$set":{"status":1}}
result =db.fila.update({"_id":id}, dados )
print(result)