def create_book(title, author, genre):
    return (title, author, genre)

def add_to_library(book, library, book_set):
    if book not in book_set:
        library.append(book)
        book_set.add(book)
        print(f"Added: {book[0]} by {book[1]}")
    else:
        print(f"Already exists: {book[0]} by {book[1]}")

def remove_from_library(title, library, book_set):
    for book in library:
        if book[0] == title:
            library.remove(book)
            book_set.remove(book)
            print(f"Removed: {title}")
            return
    print(f"Not found: {title}")

def search_books(search_term, library):
    return [book for book in library if search_term.lower() in book[0].lower() or search_term.lower() in book[1].lower()]

def list_books(library):
    if library:
        print("Books in the library:")
        for book in library:
            print(f"{book[0]} by {book[1]} ({book[2]})")
    else:
        print("Library is empty.")

def categorize_books(library):
    genres = {}
    for book in library:
        genres.setdefault(book[2], []).append(book)
    return genres

library = []
book_set = set()

books_to_add = [
    create_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
    create_book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
    create_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),  # Duplicate
]

for book in books_to_add:
    add_to_library(book, library, book_set)

remove_from_library("To Kill a Mockingbird", library, book_set)

search_results = search_books("Great", library)
print("\nSearch results:")
for book in search_results:
    print(f"{book[0]} by {book[1]} ({book[2]})")

print("\nAll books:")
list_books(library)

categorized_books = categorize_books(library)
print("\nBooks by genre:")
for genre, books in categorized_books.items():
    print(f"{genre}:")
    for book in books:
        print(f"  {book[0]} by {book[1]}")
