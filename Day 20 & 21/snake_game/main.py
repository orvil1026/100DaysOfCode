from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
sleep_timer = 0.1

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(sleep_timer)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    if scoreboard.score > 5:
        sleep_timer = 0.08

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:

            scoreboard.reset_score()
            snake.reset_snake()













screen.exitonclick()