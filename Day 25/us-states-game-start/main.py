from turtle import Turtle,Screen
import pandas

turtle = Turtle()
screen = Screen()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer = screen.textinput(title="Guess the state", prompt="Whats another states name?")


screen.exitonclick()