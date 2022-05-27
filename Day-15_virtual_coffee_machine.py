# dime = 10
# quarter = 25
# nickel = 5
# penny = 1
coffee_menu = {
    "expresso": {
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
    },
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(c_type):
    if resources["water"] < coffee_menu[c_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return -1
    elif resources["coffee"] < coffee_menu[c_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return -1
    if c_type != "expresso":
        if resources["milk"] < coffee_menu[c_type]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return -1
    return 0


def report():
    print(f"""Water : {resources["water"]}""")
    print(f"""Milk : {resources["milk"]}""")
    print(f"""Coffee : {resources["coffee"]}""")


def order():
    c_type = input("What would you like ? (expresso/latte/cappuccino): ")
    if c_type == "report":
        report()
        return
    elif c_type == "off":
        return "off"
    v = check_resources(c_type)
    if(v==-1):
        return

    s = 0
    print("please insert coins")
    n_q = int(input("how many quarters?: "))
    s += n_q * 0.25

    n_dimes = int(input("how many dimes?: "))
    s += n_dimes * 0.1

    n_nic = int(input("how many nickles?: "))
    s += n_nic * 0.05
    n_p = int(input("how many pennies?: "))
    s += n_p * 0.01
    if s < coffee_menu[c_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return
    else:
        resources["water"] -= coffee_menu[c_type]["ingredients"]["water"]
        resources["coffee"] -= coffee_menu[c_type]["ingredients"]["coffee"]
        if c_type != "expresso":
            resources["milk"] -= coffee_menu[c_type]["ingredients"]["milk"]
        change = s-coffee_menu[c_type]["cost"]
        print(f"Here is ${round(change,2)} in change.")
        print(f"Here is your {c_type} Enjoy!")

k = "on"
while k!="off":
    k= order()
