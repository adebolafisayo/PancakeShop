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

    def list_books(self):
        if not self.collection:
            print("No books in the collection")
        for book in self.collection:
            print(book)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in self.collection], file)
        print(f"Collection saved to {filename}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                book_list = json.load(file)
                self.collection = [Book(**book) for book in book_list]
            print(f"Collection loaded from {filename}")
        except FileNotFoundError:
            print(f"No file found with the name {filename}")

def main():
    manager = BookCollectionManager()
    while True:
        print("\nBook Collection Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for Books")
        print("4. List All Books")
        print("5. Save Collection")
        print("6. Load Collection")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            year = input("Enter year: ")
            manager.add_book(Book(title, author, genre, year))
        elif choice == '2':
            title = input("Enter title of the book to remove: ")
            manager.remove_book(title)
        elif choice == '3':
            query = input("Enter search query: ")
            search_type = input("Search by (title/author/genre): ")
            results = manager.search_books(query, search_type)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found")
        elif choice == '4':
            manager.list_books()
        elif choice == '5':
            filename = input("Enter filename to save to: ")
            manager.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load from: ")
            manager.load_from_file(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
