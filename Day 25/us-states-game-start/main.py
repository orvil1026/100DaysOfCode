from turtle import Turtle,Screen
import pandas

turtle = Turtle()
screen = Screen()
writer = Turtle()
writer.hideturtle()
writer.penup()

score = 0

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data['state'].tolist()
guessed_states = []

while score < 51:

    input_answer = screen.textinput(title=f"Guess the state {score}/50 correct", prompt="Whats another states name?").title()

    if input_answer == 'Exit':
        break
    if input_answer in states_list:
        guessed_state = data[data.state == input_answer]
        x = int(guessed_state.x)
        y = int(guessed_state.y)
        name = input_answer
        guessed_states.append(name)
        writer.goto(x, y)
        writer.write(name)


states_to_learn = []
for state in states_list:
    if state not in guessed_states:
        states_to_learn.append(state)

states_to_learn_data ={
    "state":states_to_learn
}

data = pandas.DataFrame(states_to_learn_data)

data.to_csv("states_to_learn.csv")

print(states_to_learn)