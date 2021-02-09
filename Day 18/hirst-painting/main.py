from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)
# import colorgram
#
# colours = colorgram.extract('image.jpg', 20)
#
# rgb_colors = []
#
# for color in colours:
#     new = color.rgb
#     r = new.r
#     g = new.g
#     b = new.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
jim = Turtle()
color_list = [(236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234),
              (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0),
              (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]
jim.penup()
jim.goto(-200, -200)
jim.pendown()


x0, y0 = jim.position()
initial_x = x0
for i in range(10):
    for j in range(10):
        jim.pencolor(random.choice(color_list))
        jim.penup()
        jim.goto(x0, y0)
        jim.pendown()
        x0 += 50
        jim.dot(20)

    x0 = initial_x
    y0 = y0 + 50
jim.hideturtle()
screen = Screen()
screen.exitonclick()
