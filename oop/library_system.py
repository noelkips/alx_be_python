class Book:
    """
    Base class representing a book with basic attributes.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """Return string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    EBook class that inherits from Book and adds file size attribute.
    
    Additional Attributes:
        file_size (int): The file size of the ebook in KB
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """Return string representation of the ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    PrintBook class that inherits from Book and adds page count attribute.
    
    Additional Attributes:
        page_count (int): The number of pages in the book
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """Return string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Library class that demonstrates composition by managing a collection of books.
    
    Attributes:
        books (list): A list to store instances of Book, EBook, and PrintBook
    """
    
    def __init__(self):
        """Initialize a Library instance with an empty list of books."""
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book: An instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)