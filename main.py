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


turn_off_machine = False
profit = 0
enough_resources = True

# While the machine is on the program will keep opn asking if you'd like a coffee. Until user inputs "off"
while not turn_off_machine:
    users_choice_coffee = str(input("What would you like? (espresso/latte/cappuccino):")).lower()
#    #print_dict(resources)

    if users_choice_coffee == "off":
        turn_off_machine = True
        break
    elif users_choice_coffee == "report":
        print(list(resources.keys())[0], resources["water"], "ml")
        print(list(resources.keys())[1], ":", resources["milk"], "ml")
        print(list(resources.keys())[2], ":", resources["coffee"], "g")
        print(f"money : ${profit}")
    elif users_choice_coffee == "latte" or users_choice_coffee == "cappuccino":
        if resources["water"] - MENU[users_choice_coffee]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            enough_resources = False
        elif resources["milk"] - MENU[users_choice_coffee]["ingredients"]["milk"] < 0:
            print("Sorry there is not enough milk.")
            enough_resources = False
        elif resources["coffee"] - MENU[users_choice_coffee]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            enough_resources = False
    elif users_choice_coffee == "espresso":
        if resources["water"] - MENU[users_choice_coffee]["ingredients"]["water"] < 0:
            print("Sorry there is not enough water.")
            enough_resources = False
        elif resources["coffee"] - MENU[users_choice_coffee]["ingredients"]["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            enough_resources = False

        if enough_resources:

            print("Please insert coins.")
            quarters_inserted = int(input("How many quarters?: ")) * 0.25
            dimes_inserted = int(input("How many dimes?: ")) * 0.10
            nickels_inserted = int(input("How many nickles?: ")) * 0.05
            pennies_inserted = int(input("How many pennies?: ")) * 0.01

            # this variable is a float containing the total amount of money inserted to the machine
            total_money_inserted = quarters_inserted + dimes_inserted + nickels_inserted + pennies_inserted

            # here is where the amount of money inserted is checked
            if total_money_inserted - MENU[users_choice_coffee]["cost"] < 0:
                print("Sorry, not enough money inserted.")
            else:
                profit += MENU[users_choice_coffee]["cost"]
                print("Here is", total_money_inserted - MENU[users_choice_coffee]["cost"], "in change.")
                if users_choice_coffee == "espresso":
                    resources["water"] = resources["water"] - MENU[users_choice_coffee]["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - MENU[users_choice_coffee]["ingredients"]["coffee"]
                else:
                    resources["water"] = resources["water"] - MENU[users_choice_coffee]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU[users_choice_coffee]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU[users_choice_coffee]["ingredients"]["coffee"]

                print(f"Here is your " + users_choice_coffee + " ☕. Enjoy!")

    else:
        print("Please input a proper coffee.")
        # from here the program should ask again to input a coffee, not to input coins...
