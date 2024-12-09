class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed {book.title}.")

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member Name: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed book: {book.title}")
        else:
            print(f"Book {book.title} not found in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
        print("-" * 30)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member)
        print("-" * 30)

'''
# Example Usage
if __name__ == "__main__":
    # Create a library
    library = Library()

    # Add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    library.register_member(member1)
    library.register_member(member2)

    # Display library books and members
    library.display_books()
    library.display_members()

    # Borrow and return books
    member1.borrow_book(book1)
    member2.borrow_book(book1)  # Trying to borrow an already borrowed book
    member2.borrow_book(book2)

    library.display_books()  # Check book availability after borrowing

    member1.return_book(book1)
    member2.return_book(book2)

    library.display_books()  # Check book availability after returning

'''