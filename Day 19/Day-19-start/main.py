from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def forward():
    jim.forward(10)


def backward():
    jim.backward(10)


screen.listen()
screen.onkey(fun=forward, key='space')

screen.onkey(fun=backward, key='a')

screen.exitonclick()