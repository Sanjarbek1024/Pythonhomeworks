class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Exception raised when a book is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Exception raised when a member tries to borrow more than the allowed limit."""
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} has already borrowed the maximum limit of {Member.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed by someone else.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = ', '.join(book.title for book in self.borrowed_books) or 'No books'
        return f"{self.name} (Borrowed books: {borrowed_titles})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"The book '{title}' was not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise Exception(f"Member '{member_name}' is not registered in the library.")

        book = self.find_book(book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise Exception(f"Member '{member_name}' is not registered in the library.")

        book = self.find_book(book_title)
        member.return_book(book)

    def list_books(self):
        return '\n'.join(str(book) for book in self.books) or 'No books in the library.'

    def list_members(self):
        return '\n'.join(str(member) for member in self.members) or 'No members in the library.'

# the Library Management System
if __name__ == "__main__":
    library = Library()

    # Add books
    library.add_book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # Add members
    library.add_member("Alice")
    library.add_member("Bob")

    print("Initial list of books:")
    print(library.list_books())
    print()

    print("Initial list of members:")
    print(library.list_members())
    print()

    # Borrow books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Bob", "To Kill a Mockingbird")
    except Exception as e:
        print(e)

    print("List of books after borrowing:")
    print(library.list_books())
    print()

    print("List of members after borrowing:")
    print(library.list_members())
    print()

    # Attempt to borrow an already borrowed book
    try:
        library.borrow_book("Alice", "To Kill a Mockingbird")
    except Exception as e:
        print(e)
    print()

    # Return books
    try:
        library.return_book("Alice", "1984")
    except Exception as e:
        print(e)

    print("List of books after returning:")
    print(library.list_books())
    print()

    print("List of members after returning:")
    print(library.list_members())
    print()

    # Attempt to exceed borrow limit
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "To Kill a Mockingbird")
        library.borrow_book("Alice", "The Catcher in the Rye")
        library.borrow_book("Alice", "Extra Book")
    except Exception as e:
        print(e)
