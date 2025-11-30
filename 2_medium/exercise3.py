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

class Book():
    def __init__(self,title,author,year,is_checked_out=False):
        self.title=title
        self.author=author
        self.year=year
        self.is_checked_out=is_checked_out
    def checkout(self):
        self.is_checked_out=True
    def return_book(self):
        self.is_checked_out=False
    def __str__(self):
        return f"{self.title} by {self.author} (Checked Out:{self.is_checked_out})"
    
class Library():
    def __init__(self):
        self.collection=[]
    def add_book(self, book:Book):
        self.collection.append(book)
    def list_books(self):
        for book in self.collection:
            print(str(book) +"\n")
    def find_book(self,title):
        title=title.lower()
        for book in self.collection:
            if book.title.lower()==title:
                return book
        return
    def available_books(self):
        books=[]
        for book in self.collection:
            if not book.is_checked_out:
                books.append(book)
        return books


    

if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("The Alchemist", "Paulo Coelho", 1988)

    lib = Library()
    lib.add_book(b1)
    lib.add_book(b2)

    print("List1:")
    lib.list_books()

    b1.checkout()
    print("List2:")
    lib.list_books()

    print("Available Books:")
    books=lib.available_books()
    for book in books:
        print(str(book))

    found = lib.find_book("1984")
    print(f"Found:\n{found}")


        