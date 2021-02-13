from turtle import Turtle, Screen
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

screen.listen()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

screen.onkey(fun=paddle_r.up, key="Up")
screen.onkey(fun=paddle_r.down, key="Down")

screen.onkey(fun=paddle_l.up, key="w")
screen.onkey(fun=paddle_l.down, key="s")

game_is_on = True
while game_is_on:

    screen.update()


screen.exitonclick()