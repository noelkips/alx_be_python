from library_management import Book, Library

def enhanced_demo():
    """
    Enhanced demonstration of the library management system.
    Shows additional features and edge cases.
    """
    print("=" * 60)
    print("ENHANCED LIBRARY MANAGEMENT SYSTEM DEMO")
    print("=" * 60)
    
    # Create library and add books
    library = Library()
    
    # Add various books
    books_to_add = [
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("Brave New World", "Aldous Huxley")
    ]
    
    print("📚 Adding books to library...")
    for book in books_to_add:
        library.add_book(book)
        print(f"Added: {book}")
    
    print(f"\n📊 Library Statistics:")
    print(f"Total books: {library.get_book_count()}")
    print(f"Available books: {library.get_available_count()}")
    
    print("\n📋 All books in library:")
    library.list_all_books()
    
    print("\n✅ Available books:")
    library.list_available_books()
    
    # Check out some books
    print("\n📤 Checking out books...")
    books_to_checkout = ["1984", "Pride and Prejudice", "Nonexistent Book"]
    
    for title in books_to_checkout:
        success = library.check_out_book(title)
        if success:
            print(f"✅ Successfully checked out: {title}")
        else:
            print(f"❌ Could not check out: {title}")
    
    print(f"\n📊 Updated Statistics:")
    print(f"Total books: {library.get_book_count()}")
    print(f"Available books: {library.get_available_count()}")
    
    print("\n📋 All books status:")
    library.list_all_books()
    
    print("\n✅ Currently available books:")
    library.list_available_books()
    
    # Return some books
    print("\n📥 Returning books...")
    books_to_return = ["1984", "Nonexistent Book"]
    
    for title in books_to_return:
        success = library.return_book(title)
        if success:
            print(f"✅ Successfully returned: {title}")
        else:
            print(f"❌ Could not return: {title}")
    
    print("\n✅ Final available books:")
    library.list_available_books()
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    enhanced_demo()