#Online-Barista(v1)


#Modules
import time
import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

total = 0


small = 25.00

medium = 32.00

large = 38.00

latte = 34.00

cappuccino = 32.00

americano = 26.00

flat_white = 34.00

filter_coffee = 22.00

caramel_cap = 38.00

hazelnut_cap = 38.00

clear_terminal()

print("Before we start please to be carefull what you enter and make sure of spelling.\nLimited input validation.\nWill update it in the future")
input("\n\nPress ENTER to continue...\n")
clear_terminal()

print("Welcome to NK CAFE")
time.sleep(2)
clear_terminal()
time.sleep(1)

name = input("May I get your name please\nName: ")
name = name.title()
time.sleep(1)
clear_terminal()
time.sleep(1)

while True:
    order_menu = input(f"{"Well hello there"} {name} {"do you already know what you would like to order\nor would you like the menu?"}\n{"Request: "}")
    order_menu = order_menu.upper()
    clear_terminal()
    if "MENU" in order_menu:
        clear_terminal()
        print("\n╔══════════════════════════════════╗")
        print("║          ☕ COFFEE MENU ☕         ║")
        print("╚══════════════════════════════════╝")

        print("\n-- SIZES --")
        print(f"  Small                 R{small:,.2f}")
        print(f"  Medium                R{medium:,.2f}")
        print(f"  Large                 R{large:,.2f}")

        print("\n-- COFFEES --")
        print(f"  Latte                 R{latte:,.2f}")
        print(f"  Cappuccino            R{cappuccino:,.2f}")
        print(f"  Americano             R{americano:,.2f}")
        print(f"  Flat White            R{flat_white:,.2f}")
        print(f"  Filter Coffee         R{filter_coffee:,.2f}")
        print(f"  Caramel Cappuccino    R{caramel_cap:,.2f}")
        print(f"  Hazelnut Cappuccino   R{hazelnut_cap:,.2f}")

        print("\n════════════════════════════════════")
        input("\n\nPress ENTER whe you would like to proceed...\n")
        order_size = input("What size would you like(small,medium,large)\nSize: ")
        time.sleep(1)
        order_coffee = input("\nWhat coffee would you like?\nCoffee: ")
        time.sleep(1)
        clear_terminal()
        break
    elif not "MENU" in order_menu and "ORDER" in order_menu:
        order_size = input("What size would you like(small,medium,large)\nSize: ")
        time.sleep(1)
        clear_terminal()
        order_coffee = input("What coffee would you like?\n(Latte,Cappuccino,Americano,Flat White,Filter Coffee,Caramel Cappuccino,Hazelnut Cuppacino)\nCoffee: ")
        time.sleep(1)
        clear_terminal() 
        break
    else:
        print("Sprry i dont understand your request let us start again shall we.")
        input("Press ENTER to continue...\n")
        clear_terminal()
        
order_size = order_size.lower()
order_coffee = order_coffee.lower()

ordercoffee = {"latte" : latte ,
               "cappuccino" : cappuccino ,
               "americano" : americano , 
               "flat white" : flat_white ,
               "filter coffee" : filter_coffee ,
               "caramel cappuccino" : caramel_cap ,
               "hazelnut cappucino" : hazelnut_cap}
ordersize = {"small" : small ,
             "medium" : medium ,
             "large" : large}

total += ordercoffee.get(order_coffee)
total += ordersize.get(order_size)

time.sleep(2)
clear_terminal()

while True:
    fullorder = input(f"{"Okay"} {name} {"let me just make sure i have the correct order"} {order_size} {order_coffee}?\n{"yes/no: "}")
    fullorder = fullorder.lower()

    if fullorder == "yes":
        clear_terminal()
        time.sleep(1)
        print("\nYour total is " + f"R{total:,.2f}")
        time.sleep(1)
        while True:
            ammount_payed = float(input("PLease enter the amount you have to pay , you could add a tip if you would like\nAmount: "))
            clear_terminal()
            print("Processing payment...")
            time.sleep(3)
            clear_terminal()
            if ammount_payed >= total:
                print("Payment successfull")
                time.sleep(1)
                clear_terminal()
                print("Preparing Portafilter...")
                time.sleep(10)
                clear_terminal()
                print("Pulling the shot...")
                time.sleep(10)
                clear_terminal()
                print("Steaming the milk...")
                time.sleep(10)
                clear_terminal()
                time.sleep(10)
                print("Mixing...")
                time.sleep(15)
                clear_terminal()
                print("READY!")
                time.sleep(1)
                clear_terminal()
                print(f"{"Here is your"} {order_size} {order_coffee} {name}\n{"Have a nice day!!"}")
                input("\nPress ENTER to exit NK Cafe...\n")
                clear_terminal()
                print("Exiting...")
                time.sleep(2)
                exit()
            else:
                print("Insufficient try again")
                time.sleep(2)
                clear_terminal()    
    elif fullorder == "no":
        print("please rerun and lets try again")
        time.sleep(2)
        exit()
    else:
        print("Something went wrong")
        time.sleep(2)
        exit()


