from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(canvheight=400, canvwidth=500)
bid = screen.textinput(title='Make a bid', prompt='Enter the colour of the turtle:')
colour_list = ['blue', 'red', 'yellow', 'green', 'orange', 'black']
x0 = -350
y0 = -200
game_on = False
race_turtles = []
for color in colour_list:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    y0 = y0 + 60
    new_turtle.goto(x=x0, y=y0)
    race_turtles.append(new_turtle)
if bid:
    game_on = True

while game_on:

    for r_turtle in race_turtles:
        if r_turtle.xcor() >= 300:
            game_on = False
            winning_color = r_turtle.pencolor()

            if winning_color == bid:
                print(f"You have won the bid ! {winning_color} won the race.")
            else:
                print(f"You have lost the bid ! {winning_color} won the race.")

        random_distance = random.randint(1, 10)
        r_turtle.forward(random_distance)
screen.exitonclick()
