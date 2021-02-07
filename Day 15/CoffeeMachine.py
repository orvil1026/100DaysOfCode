MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}


def choice(user_choice):
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if sufficient_resources(user_choice):
            user_coins = insert_coins()
            if sufficient_coins(user_choice, user_coins):
                if transaction(user_coins, user_choice):
                    make_coffee(user_choice)
            else:
                print("Not sufficient coins!")

        else:
            print("Not enough resources.")
    elif user_choice == 'report':
        report()
    elif user_choice == 'off':
        pass
    else:
        print("Invalid Input")


def report():
    print(f"Water:{resources['water']}ml ")
    print(f"Milk:{resources['milk']}ml ")
    print(f"Coffee:{resources['coffee']}g ")
    print(f"Money:Rs.{resources['money']}  ")


def sufficient_resources(coffee):
    ingredients_for_coffee = MENU[coffee]['ingredients']

    for item in ingredients_for_coffee:
        if resources[item] < ingredients_for_coffee[item]:
            return False
    return True


def insert_coins():
    coins = int(input("Enter the coins:"))
    return coins


def sufficient_coins(coffee, coins):
    if coins > MENU[coffee]['cost']:
        return True
    else:
        return False


def transaction(coins, coffee):
    if sufficient_coins(coffee, coins):
        resources["money"] += MENU[coffee]["cost"]
        change = coins-MENU[coffee]["cost"]
        print(f"Here is {change} in change!")
        return True

    else:
        print("That's not enough money.Money refunded.")
        return False


def make_coffee(coffee):
    for item in MENU[coffee]['ingredients']:
        resources[item] -= MENU[coffee]['ingredients'][item]
    print(f"Here is your {coffee} ☕.Enjoy!")


user_input = ''

while user_input != 'off':

    user_input = input("What would you like?(espresso/latte/cappuccino):").lower()
    choice(user_input)



