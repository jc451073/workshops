__author__ = 'jc451073'

# Initialize the constants

FILE = "books.csv"
MENU = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    print("Reading List 1.0 - by Moolayil Josmi")
    booklist = []
    load_books(booklist)
    print(booklist)
    display()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required(booklist)
        elif choice.lower() == 'c':
            completed(booklist)
        elif choice.lower() == 'a':
            booklist = add()
        elif choice.lower() == 'm':
            complete_a_book(booklist)
        display()
        choice = input(">>>")
    print("{} books has been saved to {}".format(len(booklist), FILE))
    print("Have a nice day :)")


def display():
    """

"""
    print(MENU)


def load_books(booklist):
    """
if file exists(path_to_file) then :
    open (path_to_file)
    for each line in file  :
    print the line of the file
    split and strip the content of the file
    store the content into list
"""
    book_file = open(FILE, 'r')
    for line in book_file:
        booklist.append(line.strip().split(','))
    book_file.close()


def complete_a_book(booklist):
    """
 call list_required_books(book_list) function
    try
        check for last index in book
         if last index match
            display()
        else
            open file
            create nested list for to identify the contents of the file
            display(the content of the book which matches the previous condition)

        except
        value error
        null value
    close the file
"""
    required(booklist)
    print('Enter the number of book to mark as completed')
    try:
        numofbooks = int(input(">>>"))
        if booklist[numofbooks][3] == 'c':
            print("That book is already completed")
        else:
            booklist[numofbooks][3] = 'c'
            booksfile = open(FILE, 'w')
            for i in booklist:
                for k in i:
                    if k == "r" or k == "c":
                        print(k, end='', file=booksfile)
                    else:
                        print(k, end=',', file=booksfile)
                print(file=booksfile)
            booksfile.close()
            print("{} by {} is completed".format(booklist[numofbooks][0], booklist[numofbooks][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        complete_a_book(booklist)


def required(booklist):
    """

"""
    total = 0
    print('required books:')
    count = 0
    for i in booklist:
        if 'r' in booklist[count][3]:
            print("{}. {:<50s} by {:<20s} {:>15s} pages".format(count, booklist[count][0], booklist[count][1],
                                                                booklist[count][2]))
            total += int(booklist[count][2])
        count += 1
    print('Total pages for {} books: {}'.format(count - 1, total))


def completed(booklist):
    """

"""
    total_pages = 0
    print('required books:')
    count = 0
    for i in booklist:
        if 'c' in booklist[count][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, booklist[count][0], booklist[count][1],
                                                                booklist[count][2]))
            total_pages += int(booklist[count][2])
            count += 1
    print('Total pages for {} books: {}'.format(count + 1, total_pages))


def add():
    """

"""
    title = input('Title:')
    while title == "":
        print('Input cannot be blank')
        title = input('Title:')
    author = input('Author:')
    while author == "":
        print("Input cannot be blank")
        author = input('Author:')
    valueerror = 0
    pages = 0
    while valueerror == 0:
        try:
            pages = int(input('Pages: '))
            while pages <= 0:
                print('Number must be >= 0')
                pages = int(input('Pages: '))
            valueerror = 1
        except ValueError:
            print('Invalid input; enter a valid number')
    print("{} by {}, ({} pages) added to reading list".format(title, author, pages))
    infoofbook = [title, author, str(pages), 'r']
    booklist = []
    load_books(booklist)
    booklist.append(infoofbook)
    print(booklist)
    bookfile = open(FILE, 'w')
    for i in booklist:
        for k in i:
            if k == "r" or k == "c":
                print(k, end='', file=bookfile)
            else:
                print(k, end=',', file=bookfile)
        print(file=bookfile)
    bookfile.close()


main()