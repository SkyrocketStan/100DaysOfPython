from coffee_maker import CoffeeMaker
from menu import *
from money_machine import MoneyMachine


def main():
    machine = CoffeeMaker()
    menu = Menu()
    money_box = MoneyMachine()

    while True:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            machine.report()
            money_box.report()
        else:
            order = menu.find_drink(choice)
            if order is not None and machine.is_resource_sufficient(order):
                if money_box.make_payment(order.cost):
                    machine.make_coffee(order)


if __name__ == '__main__':
    main()
