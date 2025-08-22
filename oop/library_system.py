class Book:
    def __init__(self, title: str, author: str):
        """Base class for all books"""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """EBook class inherits from Book and adds file_size"""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"E-Book: {self.title} by {self.author}, File Size: {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """PrintBook class inherits from Book and adds page_count"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"Print Book: {self.title} by {self.author}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        """Library uses composition to manage a collection of books"""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook to the library"""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added to the library!")

    def list_books(self):
        """Print details of all books in the library"""
        if not self.books:
            print("The library has no books yet.")
        else:
            for book in self.books:
                print(book)
