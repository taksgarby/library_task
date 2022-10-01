from models.book import *
import datetime

book1 = Book("Norwegian wood", "Haruki Murakami", "novel", True, datetime.date(2022, 10, 10))
book2 = Book("Cooking with Nigela", "Nigela Lawson", "cookery", False, datetime.date(2022, 10, 1))
book3 = Book("Lord of the flies", "William Golding", "young adult", False, datetime.date(2022, 10, 10))
book4 = Book("The Minpins", "Roald Dahl", "Children", True,  datetime.date(2022, 10, 20))
book5 = Book("Ready player one", "Ernest Cline", "young adult",  False, datetime.date(2022, 10, 10))
# book1 = Book("Norwegian wood", "Haruki Murakami", "novel", True)
# book2 = Book("Cooking with Nigela", "Nigela Lawson", "cookery", False)
# book3 = Book("Lord of the flies", "William Golding", "young adult", False)
# book4 = Book("The Minpins", "Roald Dahl", "Children", True)
# book5 = Book("Ready player one", "Ernest Cline", "young adult", False)


books = [book1, book2, book3, book4, book5]

def add_new_book(new_book):
    books.append(new_book)

def remove_book(title):
    book_to_remove = None
    for book in books:
        if book.title == title:
            book_to_remove = book
            break

    books.remove(book_to_remove)

