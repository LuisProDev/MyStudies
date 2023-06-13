from menu import *
from coffee_maker import *
from money_machine import *

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    drink = input(f"What would you like? ({options})"
                  " or 'report' to list the resources left: ").lower()

    if drink == 'off':
        exit()

    order = menu.find_drink(drink)

    if drink == 'report':
        coffee_machine.report()
        money_machine.report()
        continue

    if coffee_machine.is_resource_sufficient(order):
        if money_machine.make_payment(order.cost):
            coffee_machine.make_coffee(order)
        else:
            continue













