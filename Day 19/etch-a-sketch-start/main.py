from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_drawing():
    tim.reset()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=move_counter_clockwise, key="a")
screen.onkey(fun=move_clockwise, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()
