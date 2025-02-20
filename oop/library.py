class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = '대출중' if self.is_borrowed else '대기'
        return f'{self.title} / {self.author} [{status}]'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find(self, keyword):
        return [b for b in self.books if keyword in b.title]

    def borrow(self, title):
        for b in self.books:
            if b.title == title and not b.is_borrowed:
                b.is_borrowed = True
                return True
        return False
