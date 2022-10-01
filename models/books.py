from models.book import *

book1 = Book("Norwegian wood", "Haruki Murakami", "novel")
book2 = Book("Cooking with Nigela", "Nigela Lawson", "cookery")
book3 = Book("Lord of the flies", "William Golding", "young adult")
book4 = Book("The Minpins", "Roald Dahl", "Children")
book5 = Book("Ready player one", "Ernest Cline", "young adult")

books = [book1, book2, book3, book4, book5]

def add_new_book(new_book):
    books.append(new_book)

# def remove_book_by_title(remove_book):
#     for book in books: 
#         if book.title == remove_book.title:
#             books.remove(remove_book)
  


