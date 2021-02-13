from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(coordinates)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)