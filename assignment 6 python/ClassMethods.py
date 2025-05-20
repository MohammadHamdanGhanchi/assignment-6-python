class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    def __init__(self):
        # Increment the book count when a new book is created
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Increment the total_books class variable
        cls.total_books += 1

    @classmethod
    def display_book_count(cls):
        # Display the current book count
        print(f"Total books: {cls.total_books}")


# Creating instances of the Book class
book1 = Book()
book2 = Book()
book3 = Book()

# Calling the class method to display the book count
Book.display_book_count()  # Output: Total books: 3