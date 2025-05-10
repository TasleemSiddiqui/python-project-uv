# Import required modules
import json


class Book_Collection:
    """A class to manage a collection of books ,allowing user to store and organize their reading materials"""
    
    
    def __init__(self):
        """ Initialize a new book collection with an empty list and setup file storage."""
        # Initialize empty book list
        self.book_list = []
        # Set JSON file path for storage
        self.storage_file = "book_data.json"
        # Load existing books from file
        self.read_from_file()
    
    
    def read_from_file(self):
        """load saved books from a JSON file into memory.
        if the file doesn't exist or is corrupted , start with an empty collection."""
        
        try:
            # Try to open and read the JSON file
            with open(self.storage_file,"r") as file:
                self.book_list = json.load(file)
        except(FileNotFoundError,json.JSONDecodeError):
            # If file doesn't exist or is corrupted, start with empty list
            self.book_list = []
    
    
    
    def save_to_file(self):
        """store the current book collection to a JSON file for permenant storage."""
        # Open file in write mode and save book list as JSON
        with open(self.storage_file,"w") as file:
            json.dump(self.book_list,file,indent=4)
    
    
    def create_new_book(self):
        """add a new book to the collection by gathering information from the user."""
        # Get book details from user input
        book_title = input("Enter the book title:")
        book_author = input("Enter the Author Name:")
        publication_year =input("Enter Publication Year:")
        book_genre = input("Enter the genre:")
        # Check if book has been read
        is_book_read =(
            input("Have you read this book? (yes/no)").strip().lower() == "yes"
        )
        # Create new book dictionary
        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read" : is_book_read      
        } 
        
        # Add book to collection and save
        self.book_list.append(new_book)
        self.save_to_file()
        print("book added successfully")
        
    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("Enter the title of the book to remove: ")

        # Use a list comprehension to create a new list without the book to delete
        original_length = len(self.book_list)
        self.book_list = [
            book for book in self.book_list 
            if book["title"].lower() != book_title.lower()
        ]
        
        # Check if a book was actually removed by comparing lengths
        if len(self.book_list) < original_length:
            self.save_to_file()
            print("Book removed successfully!\n")
        else:
            print("Book not found!\n")

        
    def find_book(self):
        """Search for book in the collection by title or author name."""
        
        # Get search criteria from user
        search_type = input("Search by:\n1.Title\n2.Author\nEnter your choice")
        search_text= input("Enter search term:").lower()
        # Search for matching books
        found_books=[
             book
             for book in self.book_list
             if search_text in book["title"].lower()
             or search_text in book["author"].lower()
        ]
        
        # Display results
        if found_books:
            print("Matching Books")
            for index,book in enumerate(found_books,1):
                reading_status = "Read" if book["read"] else "Unread"
                print(
                    f"{index}.{book["title"]} by {book["author"]} ({book["year"]} - {book["genre"]} - {reading_status})"
                )
        else:
            print("No Matching found. \n")
    
    
    
    def update_book(self):
        """Modify the details of an existing book in the collection"""
        # Get book to update
        book_title = input("Enter the title of the book you wnat to edit: ")
        
        # Search for book and update if found
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                # Update each field if new value provided
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")
        
    def show_all_books(self):
        """Display all books in the collection with thier details"""
        # Check if collection is empty
        if not self.book_list:
            print("your collection is empty .\n")
            return
        
        
        print("Your Book Collection")
        # Display each book's details
        for index, book in enumerate(self.book_list,1):
            reading_status = "Read " if book["read"] else "unread"
            print(
                f"{index}.{book["title"]} by {book["author"]} ({book["year"]} - {book["genre"]} - {reading_status})"
            )
        print("Empty!")
    
    
    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress."""
        # Calculate total books and completion rate
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )
        print(f"Total books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")
        
        
    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""
        while True:
            # Display menu options
            print("📚 Welcome to Your Book Collection Manager! 📚")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            # Handle user choice
            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_book()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_reading_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    # Create book manager instance and start application
    book_manager = Book_Collection()
    book_manager.start_application()        
