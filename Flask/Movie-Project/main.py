from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

TMDB_API_KEY = '570ac04528cca97eebe735e85c7dc68a'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)

# db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# db.session.add(new_movie)
# db.session.commit()


class EditForm(FlaskForm):
    rating = FloatField('Your rating out of 10',validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating.desc())
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id):
    form = EditForm()

    if form.validate_on_submit():
        movie_by_id = Movie.query.get(id)
        movie_by_id.rating = form.rating.data
        movie_by_id.review = form.review.data

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', form=form)


@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id):
    movie_by_id = Movie.query.get(id)
    db.session.delete(movie_by_id)
    db.session.commit()

    return redirect(url_for('home'))

@app.route("/add",methods=["GET","POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        params = {
            'query': movie_title,
            'language': 'en-US',

        }
        request = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}", params=params)
        data = request.json()['results']
        print(data)

        return render_template('select.html', movies=data)

    return render_template('add.html', form=form)


@app.route('/find/<int:id>',methods=["GET","POST"])
def find(id):
    request = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}")
    data = request.json()
    print(data)
    title = data['original_title']
    img_url = data['poster_path']
    year = data['release_date'][:5]
    description = data['overview']

    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=7.3,
        ranking=10,
        review=" ",
        img_url= f"https://image.tmdb.org/t/p/w500{img_url}"
    )

    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.filter_by(title=title).first()
    id = movie.id
    return redirect(url_for('edit', id=id))

if __name__ == '__main__':
    app.run(debug=True)
