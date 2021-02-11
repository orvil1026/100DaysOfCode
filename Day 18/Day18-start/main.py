from turtle import Turtle, Screen
import random
import turtle

jim = Turtle()
turtle.colormode(255)

jim.shape("turtle")
jim.color("red", "green")

# Rectangle
# for i in range(4):
#     jim.forward(100)
#     jim.right(90)

# Dashed line
# for i in range(100):
#     if i % 2 == 0:
#         jim.penup()
#     else:
#         jim.pendown()
#     jim.forward(3)

colours = ['green yellow', 'firebrick', 'medium slate blue', 'deep sky blue',
           'medium spring green', 'powder blue', 'dark red', 'pale violet red', 'purple',
           'orange', 'yellow', 'teal', 'blue', 'deep pink']
jim.speed('fastest')
jim.width(8)

# Triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
for i in range(3, 11):
    jim.pencolor(random.choice(colours))
    sides = i
    angle = 360 / sides
    for side in range(sides):
        jim.forward(100)
        jim.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Random Walk
# direction = [0, 90, 180, 270]
# for i in range(200):
#     jim.pencolor(random_color())
#     jim.forward(30)
#     jim.setheading(random.choice(direction))



# Spirograph
# for i in range(36):
#     jim.pencolor(random_color())
#     jim.circle(100)
#     jim.left(10)


screen = Screen()
screen.exitonclick()