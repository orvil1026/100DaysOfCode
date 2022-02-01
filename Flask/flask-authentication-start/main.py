from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['LOGIN_DISABLED'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()

login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

#Line below only required once, when creating DB. 
# db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":

        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")


        if User.query.filter_by(email=email).first():
            error = "Email Id already registered!"
        else:
            new_user = User(
                email=email,
                password=generate_password_hash(password, method='pbkdf2:sha256', salt_length=8),
                name=name,

            )

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('secrets'))

    return render_template("register.html",error=error)


@app.route('/login',methods=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        is_password_correct = check_password_hash(user.password, password)

        if user is not None and is_password_correct:
            login_user(user)
            flash('You were successfully logged in')
            return redirect(url_for('secrets'))

        elif user is None:
            error = "User Not Found!"

        elif is_password_correct == False:
            error = "Wrong Password"
        else :
            error = "Error Occured!"
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():

    return send_from_directory(directory='static/files/', filename='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
