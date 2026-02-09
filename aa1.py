class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added:", book.title)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed:", title)
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned:", title)
                return

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            if book.available:
                print(book.title, "-", book.author)


lib = Library()
b1 = Book("Python", "harsha")
b2 = Book("Java", "tv")

lib.add_book(b1)
lib.add_book(b2)
lib.display_books()
lib.borrow_book("Python")
lib.display_books()
