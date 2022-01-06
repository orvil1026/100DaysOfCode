from flask import Flask
app = Flask(__name__)


def make_bold(function):

    def wrap_func():

        return '<b>' + function() + '</b>'

    return wrap_func


def emphasis(function):

    def wrap_func():

        return '<i>' + function() + '</i>'
    return wrap_func

@app.route('/')
def hello_world():
    return '<h1 align="center">Hello, World!</h1>' \
           '<p>Welcome to Manchester United</p>' \
           '<img src="https://media.giphy.com/media/hryis7A55UXZNCUTNA/giphy.gif" width="300">'


@app.route('/username/<name>/<int:age>')
def greet(name, age):
    return f'Hello World {name} , my age is {age}'


@app.route('/bye')
@make_bold
@emphasis
def bye():
    return "bye"

if __name__ == "__main__":
    app.run(debug=True)