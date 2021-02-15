from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()
paddle_r = Paddle((350, 0), "red")
paddle_l = Paddle((-350, 0), "blue")
ball = Ball()
score = ScoreBoard()

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")

screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Collision with upper and lower walls
    if ball.has_collided():
        ball.bounce_y()

    # Collision with the paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball out of bounds

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()