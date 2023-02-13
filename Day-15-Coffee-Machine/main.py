import machine


def print_report():
    print(f"Water: {machine.resources['water']}ml")
    print(f"Milk: {machine.resources['milk']}ml")
    print(f"Coffee: {machine.resources['coffee']}g")
    print(f"Money: ${machine.resources['money']}")


def is_enough_resources(choice):
    message = "Sorry there is not enough"
    for ingredient in machine.MENU[choice]["ingredients"]:
        if machine.MENU[choice]["ingredients"][ingredient] > machine.resources[ingredient]:
            print(f"{message} {ingredient}.")
            return False
    return True


def make_a_drink(choice):
    for ingredient in machine.MENU[choice]["ingredients"]:
        machine.resources[ingredient] -= machine.MENU[choice]["ingredients"][ingredient]
    machine.resources["money"] += machine.MENU[choice]["cost"]
    print(f"Here is your {choice} ☕️. Enjoy!")


def process_coins(choice):
    print("Please insert coins.")
    inserted_money = int(input("how many quarters? ")) * 0.25
    inserted_money += int(input("how many dimes? ")) * 0.1
    inserted_money += int(input("how many nickles? ")) * 0.05
    inserted_money += int(input("how many pennies? ")) * 0.01
    if machine.MENU[choice]["cost"] > inserted_money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        calculated_change = round(inserted_money - machine.MENU[choice]["cost"], 2)
        if calculated_change != 0:
            print(f"Here is ${calculated_change} in change.")
        make_a_drink(choice)


is_machine_on = True
while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        is_machine_on = False
    elif user_choice == "report":
        print_report()
    elif user_choice in machine.MENU:
        if is_enough_resources(user_choice):
            process_coins(user_choice)
