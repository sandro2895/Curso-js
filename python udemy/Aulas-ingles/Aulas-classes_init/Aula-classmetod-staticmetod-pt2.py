class Book:
    TYPES = ('hardcover', 'paperback', 'capa')
    casa = 'HOUSE'

    def __init__(self, name: str, book_type : str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'Book name: {self.name}, Book Type: {self.book_type}, Book weight: {self.weight}'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    @classmethod
    def paperback(cls, name, page_weigth) -> "Book":
        return cls(name, cls.TYPES[1], page_weigth)

    @classmethod
    def capas(cls, name, page_weigth):
        return cls(name, cls.TYPES[2], page_weigth)

    @classmethod
    def casita(cls, name, page_wigth):
        return cls(name, cls.casa, page_wigth)

book = Book.hardcover("harry potter", 1500)
light = book.paperback('harry', 600)
capa = Book.capas('Miseraveis',1200)
casases = Book.casita('Doca', 300)

print(book)
print(light)
print(capa)
print(casases)