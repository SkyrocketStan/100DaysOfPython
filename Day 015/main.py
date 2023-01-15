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
}

money: float = 0.0

BEVERAGES = ["espresso", "latte", "cappuccino"]


def order() -> str:
    """
    Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    :return: <str> beverage name or command in lowercase
    """
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def print_report() -> None:
    """Print coffee machine report"""
    print("Report: ")
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${money:.2f}")


def is_resources_enough(beverage: str) -> bool:
    """Check is there enough resources to make a beverage"""
    for resource, amount in MENU[beverage]['ingredients'].items():
        available_amount: int = int(resources[resource])
        requested_amount: int = int(amount)
        if requested_amount > available_amount:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def process_coins(price: float) -> bool:
    """Processing coins.
    :return: is amount of coins enough"""
    print("Please insert coins.")
    total: float = 0.0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if total >= price:
        change = round(total - price, 2)
        print(f"Here is ${change} in change.")
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


def reduce_resources(beverage: str) -> None:
    """Reduce resources amount depending on beverage name"""
    ingredients: dict = MENU[beverage]['ingredients']
    for res in ingredients:
        current_amount = int(resources[res])
        reducing_amount = int(ingredients[res])
        resources[res] = current_amount - reducing_amount


def make_beverage(beverage: str) -> None:
    if is_resources_enough(beverage):
        price: float = float(MENU[beverage]['cost'])
        if process_coins(price):
            print(f"Here is your {beverage} ☕️. Enjoy!")
            reduce_resources(beverage)
            global money
            money += price


def run():
    machine_is_working = True
    while machine_is_working:
        choice: str = order()
        # Turn off the Coffee Machine by entering “off” to the prompt.
        if choice == "off":
            machine_is_working = False
        elif choice == "report":
            print_report()
        elif choice in BEVERAGES:
            make_beverage(choice)
        else:
            print("Unknown beverage")


run()
