from typing import list


class Book:
    pass


class Bookshelf:
    def __init__(self, book: list[Book]):
        self.book = book

    def __str__(self) -> str:
        return f"BookShelf with {len(self.book)} books"
