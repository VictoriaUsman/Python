coffee_logo = r"""
              _____                               __                 
  ____  _____/ ____\____   ____     _____ _____  |  | __ ___________ 
_/ ___\/  _ \   __\/ __ \_/ __ \   /     \\__  \ |  |/ // __ \_  __ \
\  \__(  <_> )  | \  ___/\  ___/  |  Y Y  \/ __ \|    <\  ___/|  | \/
 \___  >____/|__|  \___  >\___  > |__|_|  (____  /__|_ \\___  >__|   
     \/                \/     \/        \/     \/     \/    \/       """

print(coffee_logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 150,
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
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}

profit = 0


#value for MENU  = MENU["espresso"]["ingredients"]["water"]
#value for cost = MENU["espresso"]["cost"]
#value for resource =  resources["water"]

#MENU value
Reset = True

#resources value
rwater = resources["water"]
rmilk = resources["milk"]
rcoffee = resources["coffee"]
while Reset == True:
    Select = input("What would you like? (espresso/latte/cappucino): ")
    if Select == "espresso":
        vwater = MENU[Select]["ingredients"]["water"]
        vcoffee = MENU[Select]["ingredients"]["coffee"]
        if rwater < vwater:
            print("You don't have enough water!")
            Reset = False
        if rcoffee < vcoffee:
            print("You don't have enough coffee!")
            Reset = False
        else:
            rwater -= vwater
            rcoffee -= vcoffee

    if Select == "latte":
        vwater = MENU[Select]["ingredients"]["water"]
        vcoffee = MENU[Select]["ingredients"]["coffee"]
        vmilk = MENU[Select]["ingredients"]["milk"]
        if rwater < vwater:
            print("You don't have enough water!")
            Reset = False
        if rcoffee < vcoffee:
            print("You don't have enough coffee!")
            Reset = False
        if rmilk < vmilk:
            print("You don't have enough milk!")
            Reset = False
        else:
            rwater -= vwater
            rcoffee -= vcoffee
            rmilk -= vmilk

    if Select == "cappuccino":
        vwater = MENU[Select]["ingredients"]["water"]
        vcoffee = MENU[Select]["ingredients"]["coffee"]
        vmilk = MENU[Select]["ingredients"]["milk"]
        if rwater < vwater:
            print("You don't have enough water!")
            Reset = False
        if rcoffee < vcoffee:
            print("You don't have enough coffee!")
            Reset = False
        if rmilk < vmilk:
            print("You don't have enough milk!")
            Reset = False
        else:
            rwater -= vwater
            rcoffee -= vcoffee
            rmilk -= vmilk

    if Select == "report":
        print("Water: " + str(rwater) + " ml")
        print("Milk: " + str(rmilk) + " ml")
        print("Coffee: " + str(rcoffee) + " mg")
        print("Money: " + "$ " + str(profit))
        Reset = Truer


    if Select == "off":
        print('Goodbye!')

    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))

    c_quarters = quarters * 0.25
    c_dimes = dimes * 0.10
    c_nickles = nickles * 0.05
    c_pennies = pennies * 0.01
    ini_money = c_quarters + c_dimes + c_nickles

    m_cost = MENU[Select]["cost"]
    if ini_money < m_cost:
        print("Sorry, that not enough money!")
        Reset = True
    if ini_money > m_cost:
        change = ini_money - m_cost
        rchange = round(change, 2)
        print(f"Here is your change: ${rchange}")
        profit += m_cost
        print(profit)
        Reset = True