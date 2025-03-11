class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, author, title, genre, year, publisher):
        self.books[book_id] = {
            "author": author,
            "title": title,
            "genre": genre,
            "year": year,
            "publisher": publisher
        }
        print(f"Book '{title}' added.")

    def delete_book(self, book_id):
        if book_id in self.books:
            removed_book = self.books.pop(book_id)
            print(f"Book '{removed_book['title']}' deleted.")
        else:
            print("Book ID not found.")

    def search_book(self, search_term):
        found_books = [book for book in self.books.values() if search_term.lower() in book["title"].lower()]
        return found_books if found_books else "No books found."

    def replace_book(self, book_id, author, title, genre, year, publisher):
        if book_id in self.books:
            self.books[book_id] = {
                "author": author,
                "title": title,
                "genre": genre,
                "year": year,
                "publisher": publisher
            }
            print(f"Book '{title}' updated.")
        else:
            print("Book ID not found.")

    def display_books(self):
        if self.books:
            for book_id, book_info in self.books.items():
                print(
                    f"ID: {book_id} - Title: {book_info['title']}, Author: {book_info['author']}, Genre: {book_info['genre']}, Year: {book_info['year']}, Publisher: {book_info['publisher']}")
        else:
            print("No books in the collection.")

