"""
(incomplete) Tests for Book class
"""
from book import Book

# test empty book (defaults)
book = Book()
print(book)
assert book.author == ""
assert book.title == ""
assert book.pages == 0

# test initial-value book
book2 = Book("The Memory Code", "Kelly", 842, 'r')
print(book2)
print(book2.is_long_book())

book2.mark_book_completed()
print(book2)
# test mark_completed()
