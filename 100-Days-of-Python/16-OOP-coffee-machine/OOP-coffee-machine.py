from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


espresso = MenuItem('espresso', 50, 0, 18, 1.5)
latte = MenuItem('latte', 200, 150, 24, 2.5)
cappuccino = MenuItem('cappuccino', 250, 100, 24, 3.0) 
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    choice = input(f"​What would you like? {menu.get_items()}: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice != 'latte' and choice != 'espresso' and choice != 'cappuccino':
        print("Sorry, I am new to making coffee beverages. I am not familiar with that one...")
        is_on = False
    else:
        selected_drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(selected_drink):
            if money_machine.make_payment(selected_drink.cost):
                    coffee_maker.make_coffee(selected_drink)
    
