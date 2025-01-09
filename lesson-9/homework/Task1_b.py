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

    def display_menu(self):
        print("\nLibrary Management System")
        print("1. List all books")
        print("2. List all members")
        print("3. Add a book")
        print("4. Add a member")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Exit")

#the Library Management System
if __name__ == "__main__":
    library = Library()

    # Add initial books and members
    library.add_book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    library.add_member("Alice")
    library.add_member("Bob")

    while True:
        library.display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nBooks in the library:")
            print(library.list_books())

        elif choice == "2":
            print("\nMembers in the library:")
            print(library.list_members())

        elif choice == "3":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
            print(f"Book '{title}' by {author} added to the library.")

        elif choice == "4":
            name = input("Enter member name: ")
            library.add_member(name)
            print(f"Member '{name}' added to the library.")

        elif choice == "5":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            try:
                library.borrow_book(member_name, book_title)
                print(f"Book '{book_title}' borrowed by {member_name}.")
            except Exception as e:
                print(e)

        elif choice == "6":
            member_name = input("Enter member name: ")
            book_title = input("Enter book title: ")
            try:
                library.return_book(member_name, book_title)
                print(f"Book '{book_title}' returned by {member_name}.")
            except Exception as e:
                print(e)

        elif choice == "7":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")