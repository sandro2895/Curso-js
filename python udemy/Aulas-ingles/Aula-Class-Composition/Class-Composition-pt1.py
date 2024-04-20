class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"




class Books():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book name: {self.name}'


book1 = Books("Harry potter")
book2 = Books("Python 101")
shelf = BookShelf(book1, book2)
print(shelf)
