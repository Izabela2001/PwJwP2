from typing import Optional


class Book:
    def __init__(self, tytul):
        self.tytul = tytul


class Library:
    books: [str, Book] = {}

    def add_book(self, isbn: str, tytul: str) -> None:
        self.books[isbn] = Book(tytul)

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books[isbn].tytul if isbn in self.books else None

# Przykładowe użycie
library = Library()
library.add_book("978-3-16-148410-0", "Python Basics")
print(library.find_book("978-3-16-148410-0"))  # Python Basics
print(library.find_book("123-4-56-789012-3"))  # None

