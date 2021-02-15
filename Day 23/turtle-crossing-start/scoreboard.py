from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.write(f"Level {self.level}", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(-10, 0)
        self.write(f"GAME OVER", font=FONT)