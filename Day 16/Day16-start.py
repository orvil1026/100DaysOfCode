from turtle import Turtle, Screen

# jimmy = Turtle()
# my_screen = Screen()
#
# jimmy.shape("turtle")
# jimmy.color("blue1", "DarkOrchid")
# jimmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
table.align = "l"
print(table)

