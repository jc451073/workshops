"""
Name: Moolayil Josmi Anu Jose
Date: 29/01/2017
Brief Project Description:
GitHub URL: https://github.com/jc451073/workshops.gi
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from booklist import *


class ReadingListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.books = BookList()
        self.books.load_books()

    def build(self):
        self.title = "Reading List 2.0"
        self.root = Builder.load_file('app.kv')
        self.required_books()
        return self.root

    def add_book(self, title='', author='', pages=''):
        self.books.add_book(title, author, pages)

    def required_books(self):
        self.root.ids.content_display.clear_widgets()
        count = 0
        num_books = 0
        for book in self.books.book_list:
            if 'r' in book.status:
                temp_button = Button(text=book.title)
                temp_button.bind(on_release=self.mark_book_completed)
                self.root.ids.content_display.add_widget(temp_button)
                num_books += 1
            count += 1
        total = self.books.get_total()
        if num_books > 0:
            print("Total pages for {} books: {}".format(count - 1, total))
            self.root.ids.line_layout.text = "Clicks books to mark them as complete"
            self.root.ids.action_layout.text = "Total pages to read: " + str(total)
        else:
            print("no books")
            self.root.ids.action_layout.text = "Total pages to read: " + str(total)
            self.root.ids.line_layout.text = "All books are completed"

    def mark_book_completed(self, instance):
        title = instance.text
        book = self.books.get_book_title(title)
        book.mark_book_completed()
        self.display_required_books()
        self.root.ids.bottom_layout.text = title + " is marked as completed"
        print(self.books.book_list)

    def completed_books(self):
        self.root.ids.content_display.clear_widgets()
        count = 0
        num_books = 0
        for book in self.books.book_list:
            if 'c' in book.status:
                temp_button = Button(text=book.title)
                temp_button.bind(on_release=self.status_completed_books)
                self.root.ids.content_display.add_widget(temp_button)
                num_books += 1
            count += 1
        total = self.books.get_total('c')
        if num_books > 0:
            self.root.ids.action_layout.text = "Total pages completed: " + str(total)
            self.root.ids.line_layout.text = "Click book to see the details"
        else:
            self.root.ids.line_layout.text = "To display no book is completed"

    def status_completed_books(self, instance):
        title = instance.text
        book = self.books.get_book_title(title)
        self.root.ids.line_layout.text = book.title + " by " + book.author + ", " + book.pages + " (Completed)"

    def main(self):
        self.books.save_books()

    def clear(self):
        self.root.ids.title.text = ''
        self.root.ids.author.text = ''
        self.root.ids.pages.text = ''


obj = ReadingListApp()
obj.run()
obj.main()
