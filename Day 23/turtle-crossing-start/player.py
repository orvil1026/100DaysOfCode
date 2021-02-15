from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def has_won(self):
        return self.ycor() == FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)
