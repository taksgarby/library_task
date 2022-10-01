from flask import render_template, request, redirect
from app import app
from models.book import *
from models.books import books, add_new_book

@app.route("/")
def home():
    return render_template("home.html", title= "Home")


@app.route('/books')
def index():
    return render_template("index.html", title= "Home", books = books )



@app.route('/books/<index>')
def chosen_book(index):
  chosen_book = books[int(index)]
  
  return render_template('book.html', book=chosen_book)


@app.route('/add')
def add_page():
      return render_template("add.html", title="Add")

@app.route('/books', methods=["POST"])
def add_book():
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  new_book = Book(title=title, author= author, genre=genre)
  add_new_book(new_book)

  return redirect("/books")
  # True if 'recurring' in request.form else False
  # roomLocation = request.form['roomLocation']
  # description = request.form['description']
  
@app.route('/remove')
def remove_book():
  return render_template("remove.html", title="Remove", books = books)

# # @app.route('/')
# @app.route('/books', methods=["POST"])
# def remove_book():
#   title = request.form['title']
#   remove_book = Book(title=title)
#   remove_book_by_title(remove_book)

#   return redirect("/books")