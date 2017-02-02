"""
(incomplete) Tests for BookList class
"""
from booklist import BookList
from book import Book

books = BookList()

# test empty BookList
print(books)
assert len(books.book_list) == 0

# test loading books
books.load_books()
print(books)
assert len(books.book_list) > 0  # assuming CSV file is not empty

# test adding a new Book
books.add_book('In Search of Lost Time','Marcel Proust',365)
print(books)
assert len(books.book_list) >= 0

# test saving books (check CSV file manually to see results)
books.save_books()
assert len(books.book_list) > 0

# test get book by title function
book = books.get_book_title('The Practice of Computing Using Python')
print(book)

# test total number of pages for required
total_pages = books.get_total()
print(total_pages)