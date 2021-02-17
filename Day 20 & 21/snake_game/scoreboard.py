from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 15, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score  = {self.score} | HighScore = {self.highscore}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.clear()
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def write_highscore(self):
        with open('data.txt',mode='w') as file:
            file.write(str(self.highscore))
