import turtle

screen = turtle.Screen()
t = turtle.Turtle()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

image = "map.gif"
screen.addshape(image)
t.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()