from flask import Flask, request

app = Flask(__name__)

lista = [
  {
    "name":"My Store",
    "items":[
      {
        "name": "Chair",
        "price": "15,99"
      }
    ]
  }
]

@app.get("/loja")
def loja():
  return {"lista": lista}

@app.post("/loja")
def criar_loja():
  request_data = request.get_json()
  nova_loja = {"name": request_data["name"], "items":[]}
  lista.append(nova_loja)
  return nova_loja, 201


app.post("/store/<string:name>/item")
def create_item(name):
    request_data2 = request.get_json()
    for loja in lista:
      if loja["name"] == name:
        novo_item = {"name": request_data2["name"], "price": request_data2["price"]}
        loja["item"].append(novo_item)
        return novo_item, 201
    return {"Message": "Store not found"}, 404