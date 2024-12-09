from library_management import Book, Member, Library


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