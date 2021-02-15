from turtle import Turtle
ALIGN = 'center'
FONT = ("Arial", 40, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_paddle_score = 0
        self.l_paddle_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 240)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"{self.l_paddle_score}  |  {self.r_paddle_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_paddle_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_paddle_score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        if self.r_paddle_score == 10 or self.l_paddle_score == 10:
            self.goto(0, 0)
            if self.r_paddle_score == 10:
                self.write(f"GAME OVER Right Paddle WON", align=ALIGN, font=FONT)
            else:
                self.write(f"GAME OVER Left Paddle WON", align=ALIGN, font=FONT)