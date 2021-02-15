import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
score = ScoreBoard()


screen.onkey(fun=player.up, key="Up")

game_is_on = True
i = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i += 1

    if i % 6 == 0:
        cars.create_car()
    cars.move()

    for car in cars.cars:
        if player.distance(car) < 20:
            player.reset_position()
            score.game_over()
            game_is_on = False

    if player.has_won():
        player.reset_position()
        score.increase_score()
        cars.increase_speed()

