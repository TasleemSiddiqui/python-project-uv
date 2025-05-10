# Book Library Manager 📚

A Python-based command-line application for managing your personal book collection. This application allows you to organize, track, and manage your reading materials efficiently.

## Features

- 📖 Add new books to your collection
- 🗑️ Remove books from your collection
- 🔍 Search for books by title or author
- ✏️ Update book details
- 📋 View all books in your collection
- 📊 Track reading progress
- 💾 Automatic data persistence using JSON storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TasleemSiddiqui/book-library-manager.git
cd book-library-manager
```

2. Make sure you have Python 3.x installed on your system.

## Usage

1. Run the application:
```bash
uv run main.py
```

2. Follow the interactive menu to:
   - Add new books
   - Remove books
   - Search for books
   - Update book details
   - View all books
   - Check reading progress
   - Exit the application

## Project Structure

- `main.py`: Contains the main application logic and `Book_Collection` class
- `book_data.json`: Stores the book collection data

## Features in Detail

### Book Management
- Add books with title, author, publication year, genre, and reading status
- Remove books by title
- Update existing book details
- Search books by title or author

### Data Persistence
- Books are automatically saved to a JSON file
- Data persists between sessions
- Automatic file creation if not exists

### Reading Progress
- Track total number of books
- Calculate reading completion percentage
- View reading status for each book

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

[Your Name]

---

Happy reading! 📚✨
