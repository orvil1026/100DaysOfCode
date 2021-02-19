import turtle
import pandas

screen = turtle.Screen()
t = turtle.Turtle()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.color('blue')
image = "map.gif"
screen.addshape(image)
t.shape(image)

data = pandas.read_csv("states.csv")
states_list = data['states'].tolist()
guessed_states = []
score = 0

while score < len(states_list):

    input_answer = screen.textinput(title=f"Guess the state {score}/{len(states_list)} correct", prompt="Whats another states name?").title()

    if input_answer == 'Exit':
        writer.goto(x=30.0, y=258.0)
        writer.write(f"Score:{score}", font=("Arial", 15, "bold"))

        for state in states_list:
            writer.color('red')
            if state not in guessed_states:
                guessed_state = data[data.states == state]
                x = int(guessed_state.x)
                y = int(guessed_state.y)
                writer.goto(x, y)
                writer.write(state)

        states_to_learn = [state for state in states_list if state not in guessed_states]

        states_to_learn_data = {
            "states": states_to_learn
        }

        data = pandas.DataFrame(states_to_learn_data)

        data.to_csv("states_to_learn.csv")
        break

    if input_answer in states_list:
        guessed_state = data[data.states == input_answer]
        x = int(guessed_state.x)
        y = int(guessed_state.y)
        name = input_answer
        guessed_states.append(name)
        writer.goto(x, y)
        writer.write(name)
        score += 1







screen.exitonclick()