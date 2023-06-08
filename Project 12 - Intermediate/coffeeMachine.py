from menu import *

money = 0
espresso = 1.5
latte = 2.5
cappuccino = 3.0


def check_ingredients(drink, menu, resource):
    if drink in menu:
        drink_resources = menu[drink]
        for key in drink_resources:
            ingredients = drink_resources[key]
            for ingredient in ingredients:
                if ingredients[ingredient] > resource[ingredient]:
                    print(f"Sorry, there's no {ingredient} left")
                    return True
                else:
                    resource[ingredient] -= ingredients[ingredient]
            break


while True:
    choice = input("What would you like? (espresso/latte/cappuccino)"
                   " or 'report' to list the resources left: ").lower()

    if choice not in MENU:
        print("Choose a valid drink")
        continue

    if choice == "report":
        for items in resources:
            if items == 'coffee':
                print(f"{items}: {resources[items]}g")
            else:
                print(f"{items}: {resources[items]}ml")
        print(f"Money: ${money}")
        continue

    if check_ingredients(choice, MENU, resources):
        continue

    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    money += quarters * 0.25
    dimes = int(input("How many dimes? "))
    money += dimes * 0.10
    nickels = int(input("How many nickels? "))
    money += nickels * 0.05
    pennies = int(input("How many pennies? "))
    money += pennies * 0.01

    if MENU[choice]['cost'] > money:
        print("Sorry that's not enough money. Money refunded.")
        continue
    else:
        change = round(money - latte)
        print(f"Here is ${change} in change.")
        print("And here is your latte. Enjoy")
        continue
