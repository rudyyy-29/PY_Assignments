class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def display(self):
        books = ", ".join(book.title for book in self.borrowed)
        if books == "":
            books = "No books borrowed"
        print(f"Patron: {self.name}, Borrowed Books: {books}")



class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add Book
    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f'"{title}" added successfully.')

    # Register Patron
    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print(f'Patron "{name}" registered successfully.')

    # Find Book
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    # Find Patron
    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name.lower() == name.lower():
                return patron
        return None

    # Borrow Book
    def borrow_book(self, patron_name, title):
        patron = self.find_patron(patron_name)
        book = self.find_book(title)

        if patron is None:
            print("Patron not found.")
            return

        if book is None:
            print("Book not found.")
            return

        if book.available:
            book.available = False
            patron.borrowed.append(book)
            print(f'{patron.name} borrowed "{book.title}".')
        else:
            print("Book Not Available.")

    # Return Book
    def return_book(self, patron_name, title):
        patron = self.find_patron(patron_name)

        if patron is None:
            print("Patron not found.")
            return

        for book in patron.borrowed:
            if book.title.lower() == title.lower():
                book.available = True
                patron.borrowed.remove(book)
                print(f'{patron.name} returned "{book.title}".')
                return

        print("Book not borrowed by this patron.")

    # Show Books
    def show_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\n--- Books ---")
            for book in self.books:
                book.display()

    # Show Patrons
    def show_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
        else:
            print("\n--- Patrons ---")
            for patron in self.patrons:
                patron.display()


# -----------------------------
# Main Program (Menu)
# -----------------------------
library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. View Books & Patrons")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library.add_book(title, author)

    elif choice == "2":
        name = input("Enter Patron Name: ")
        library.register_patron(name)

    elif choice == "3":
        library.show_books()
        library.show_patrons()

    elif choice == "4":
        name = input("Enter Patron Name: ")
        title = input("Enter Book Title: ")
        library.borrow_book(name, title)

    elif choice == "5":
        name = input("Enter Patron Name: ")
        title = input("Enter Book Title: ")
        library.return_book(name, title)

    elif choice == "6":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice! Please try again.")