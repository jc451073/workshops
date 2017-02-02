# create your simple Book class in this file

class Book(object):
    def __init__(self, title='', author='', pages=0, required_status='r'):
        self.title = title
        self.author = author
        self.pages = pages
        self.required_status = status

    def __str__(self):
        return self.title + ',' + self.author + ',' + str(self.pages) + ',' + self.required_status

    def mark_book_completed(self):
        self.required_status = 'c'

    def is_long_book(self):
        return int(self.pages) >= 500
