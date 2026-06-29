# Login system(V1)

"""
 this one of my first programs well the first program i add to github

 WHAT I LEARNED:
  - I got better at understanding while loops
  - I learned my first function
  - I Implemented my first counter
"""


#modules
import time
import os

#functions
def clear_terminal():
    print("\033[H\033[2J" , end="")

#Variables
admins = ["Kian" , "Nicole" , "Liam"]
admin_pass = "1234"
attempts = 0

#Code

while True:
    name = input("Welcome\nWhat is your name?\n")
    if name == "":
        print("Please enter your name!")
        time.sleep(2)
        clear_terminal()
        time.sleep(1)
    elif not name[0].isupper():
        print("Please enter your name with a Uppercase first letter.")
        time.sleep(3)
        clear_terminal()
        time.sleep(1)
    else:
        break


time.sleep(0.5)


print("\nProcessing")

time.sleep(3)
clear_terminal()

while True:
    if name in admins:
        if attempts == 3:
            print("Too many incorrect attemps please run the program and try again later")
            exit()
        password = input("\nPlease enter your password:\n")
        if password == admin_pass:
            clear_terminal()
            time.sleep(1)
            print("\nLogged in as: " + name + "(Admin)")
            time.sleep(3)
            break
        elif password != admin_pass:
            attempts += 1
            print("\nPassword is incorrect please retry")
            time.sleep(2)
            clear_terminal()
            time.sleep(1)
    else:
        print("Welcome " + name)
        break 

time.sleep(2)
print("\nExiting program...")
exit()