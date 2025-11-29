"""
Exercise 3
| Practice object-oriented programming, attributes, and methods. Build a basic system to manage books in a library.

🧠 Requirements:

Create a Book class with:
Attributes: title, author, year, is_checked_out (default = False)
Method: checkout() → sets is_checked_out = True
Method: return_book() → sets is_checked_out = False
Method: str() → returns a string like: "1984 by George Orwell (Checked out: False)"
Create a Library class with:
Attribute: a list called collection to store books
Method: add_book(book) → adds to collection
Method: list_books() → prints all book titles and status
Method: find_book(title) → returns a matching book (case-insensitive)
Example Usage

b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.checkout()
lib.list_books()

found = lib.find_book("1984")
print(found)
🚀 Bonus Challenge:

Add a method available_books() in the Library class to list only books that are not checked out.
"""