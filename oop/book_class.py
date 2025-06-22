class Book:
    """
    A class representing a book with magic methods for enhanced functionality.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book  
        year (int): The publication year of the book
    """
    
    def __init__(self, title, author, year):
        """
        Constructor: Initialize a Book instance with title, author, and year.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
        
    def __del__(self):
        """
        Destructor: Print a deletion message when the object is destroyed.
        """
        print(f"Deleting {self.title}")
        
    def __str__(self):
        """
        String representation: Return a user-friendly string representation.
        
        Returns:
            str: A formatted string showing the book's details
        """
        return f"{self.title} by {self.author}, published in {self.year}"
        
    def __repr__(self):
        """
        Official representation: Return a string that can recreate the Book instance.
        
        Returns:
            str: A string representation that can be used to recreate the object
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"