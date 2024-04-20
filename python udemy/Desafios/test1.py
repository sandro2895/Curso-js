class Store:
    def __init__(self):
        self.name = None
        self.items = []
        carro = {'marca': 'corsa'}
        self.items.append(carro)
    def add_item(self):
        self.name = 'Doca'


    def stock_price(self):
        return f'{self.items}'


user = Store()
print(Store.stock_price(user))

