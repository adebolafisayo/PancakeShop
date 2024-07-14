import json

class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year}) - {self.genre}"

class BookCollectionManager:
    def __init__(self):
        self.collection = []

    def add_book(self, book):
        self.collection.append(book)
        print(f"Book added: {book}")

    def remove_book(self, title):
        for book in self.collection:
            if book.title.lower() == title.lower():
                self.collection.remove(book)
                print(f"Book removed: {book}")
                return
        print("Book not found")

    def search_books(self, query, search_type="title"):
        results = []
        for book in self.collection:
            if search_type == "title" and query.lower() in book.title.lower():
                results.append(book)
            elif search_type == "author" and query.lower() in book.author.lower():
                results.append(book)
            elif search_type == "genre" and query.lower() in book.genre.lower():
                results.append(book)
        return results

    