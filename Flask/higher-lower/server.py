from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 to 9 </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'></img>"


@app.route("/<int:guess>")
def guess_number(guess):

    if guess > random_number:
        return "<h1 style='color:purple'>Number is too high </h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'></img>"

    elif guess < random_number:
        return "<h1 style='color:red'>Number is too low </h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'></img>"

    else:
        return "<h1 style='color:green'> You got it correct!! </h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)