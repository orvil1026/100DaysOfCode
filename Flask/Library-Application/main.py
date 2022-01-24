from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)


# db.create_all()

# book = Book(id=2, title='Harry Putter', author='J. K. howling', rating=9.3)
# db.session.add(book)
# db.session.commit()

# all_books = db.session.query(Book).all()
# print(all_books)
#
#
# book_by_id = Book.query.get(2)
# print(book_by_id.title)
# db.session.delete(book_by_id)
# db.session.commit()


# db = sqlite3.connect('books-collection.db')
#
# all_books = []
#
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

@app.route('/')
def home():
    all_books = db.session.query(Book).all()

    return render_template('index.html', all_books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    else:
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        book = Book(title=name, author=author, rating=rating)

        db.session.add(book)
        db.session.commit()


        return redirect(url_for('home'))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_rating(id):

    if request.method == "GET":
        book_by_id = Book.query.get(id)

        return render_template('edit.html', book=book_by_id)
    else:

        book_by_id = Book.query.get(id)

        book_by_id.rating = request.form['rating']
        db.session.commit()

        return redirect(url_for('home'))


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    book_by_id = Book.query.get(id)

    db.session.delete(book_by_id)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

