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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# function to check if there are sufficient resources in the machine
def is_resource_enough(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"there isn't enough {item}")
            is_enough = False
    return is_enough


# function that returns the total calculated from coins inserted
def process_coins():
    print("please insert coins")
    total = int(input('how many quarters? ')) * 0.25
    total += int(input('how many dimes? ')) * 0.1
    total += int(input('how many nickels? ')) * 0.05
    total += int(input('how many pennies? ')) * 0.01
    return total

# function that checks if transaction is successful
def successful_transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("sorry not enough. money refunded.")
        return False

# function to make the coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}. enjoy.")


is_on = True

while is_on:
    user_choice = input("what would you like? (espresso: $1.50/latte: $2.50/cappuccino: $3.00) >>> ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"${profit}")
    else:
        drink = MENU[user_choice]
        if is_resource_enough(drink['ingredients']):
            payment = process_coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])

            








