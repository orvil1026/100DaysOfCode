from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on=True

while is_on:

    order = input("What would you like?(espresso/latte/cappuccino)")

    if order == 'off':
        is_on = False
    elif order == 'report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(order)
        drink_cost=drink.cost
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink_cost):
                coffeemaker.make_coffee(drink)

        else:
            print("Not enough resources!")
