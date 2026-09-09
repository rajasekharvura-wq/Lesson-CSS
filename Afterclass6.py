books = [
    "Harry Potter",
    "The Hobbit",
    "Pride and Prejudice",
    "The Great Gatsby",
    "To Kill a Mockingbird"
]

print("MY LIBRARY BOOK ORGANISER")
print("-------------------------")

print("\nOriginal books:")
print(books)

print("\nNumber of books:", len(books))

books.append("The Lion, the Witch and the Wardrobe")
print("\nAfter adding a book:")
print(books)

books.remove("The Great Gatsby")
print("\nAfter removing a book:")
print(books)

print("\nFirst book:", books[0])
print("Second book:", books[1])

print("\nFirst three books:")
print(books[:3])

books.sort()
print("\nBooks sorted alphabetically:")
print(books)

books.reverse()
print("\nBooks in reverse order:")
print(books)

librarian = {
    "name": "Alex Smith",
    "library": "Central Library",
    "email": "alex@library.com",
    "books_managed": len(books)
}

print("\nLibrarian information:")
print(librarian)

print("\nLibrarian name:", librarian["name"])
print("Library:", librarian["library"])

librarian["email"] = "alex.smith@library.com"

librarian["phone"] = "555-1234"

del librarian["phone"]

print("\nUpdated librarian information:")
print(librarian)

book_titles = [
    "Harry Potter",
    "The Hobbit",
    "Pride and Prejudice",
    "To Kill a Mockingbird"
]

book_authors = [
    "J.K. Rowling",
    "J.R.R. Tolkien",
    "Jane Austen",
    "Harper Lee"
]

book_directory = dict(zip(book_titles, book_authors))

print("\nBook directory:")
print(book_directory)

print("\nFINAL LIBRARY SUMMARY")
print("---------------------")
print("Total books:", len(books))
print("Books:", books)
print("Librarian:", librarian["name"])
print("Library:", librarian["library"])
print("Email:", librarian["email"])
print("Book directory:", book_directory)