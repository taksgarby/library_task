from flask import render_template, request, redirect
from app import app
from models.book import *
from models.books import books, add_new_book, remove_book
import datetime

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
  return_by = request.form['return_by']
  new_book = Book(title=title, author= author, genre=genre, checked_out = False,  return_by= return_by)

  # Split the date into a list
  split_date = return_by.split('-')
  # create a new date object
  return_by = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
  add_new_book(new_book)

  return redirect("/books")
  # True if 'recurring' in request.form else False
  # roomLocation = request.form['roomLocation']
  # description = request.form['description']
  
@app.route('/remove')
def remove_page():
  return render_template("remove.html", title="Remove", books = books)

@app.route('/remove/<title>', methods=['POST'])
def remove(title):
  remove_book(title)
  return redirect('/remove')