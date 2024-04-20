class store:
    def __init__(self, name):
        self.name = name
        self.list = []

    def add_item(self):
        item = {'nome': '', 'price': ''}
        self.item.append(item)

    def stock_price(self):
        total = 0
        for item in self.item:
            total += item['price']
        return total
