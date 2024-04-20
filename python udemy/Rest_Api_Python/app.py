from flask import Flask

app = Flask(__name__)

stores = [
  {
    "name": "My store",
    "items":
      [
        {
          "name": "Chair",
          "price": 15.99
        }
      ]
  }
]

@app.get("/store")
def get_store():
  return {"stores": stores}
  

nome = 'casa'
@app.get("/casas")
def get_casa():
  return nome