#password gen(V1)

"""
Note:
 I will update this pass gen in the future so that it will check if the generated password has been found in a breach.
 It will then regenerate a password if has been breached. But so far i used the most common names and surnames to generate
 a password and it is always secure. This does not mean to use any of these generated passwords for real , this is just a 
 learning experience for string manipulation.

"""
"""
Skills:
 - I started using string methods
 - Used random for the first time
 - Strenghtened my basic pythin skills 
"""




#modules
import time
import os
import random

#functions
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

#welcome
print("Lets create you a strong password!")
time.sleep(2)
clear_terminal()
time.sleep(1)


#variables
name = input("Please enter your name\n")
time.sleep(0.5)
clear_terminal()
time.sleep(0.5)

surname = input("Please enter your surname\n")
time.sleep(0.5)
clear_terminal()
time.sleep(0.5)

year = input("Please enter your birth year\n")
time.sleep(0.5)
clear_terminal()
time.sleep(0.5)

while True: 
    if name == "":
        print("Invalid name please enter your name\n")
        time.sleep(2)
        clear_terminal()
        time.sleep(0.1)
        name = input("Please enter your name\n")
        time.sleep(0.5)
        clear_terminal()
        time.sleep(0.5)
    else:
        break

while True: 
    if surname == "":
        print("Invalid surname please enter your surname\n")
        time.sleep(2)
        clear_terminal()
        time.sleep(0.1)
        surname = input("Please enter your surname\n")
        time.sleep(0.5)
        clear_terminal()
        time.sleep(0.5)
    else:
        break

while True: 
    if year == "":
        print("Invalid birth year please enter your birth year\n")
        time.sleep(2)
        clear_terminal()
        time.sleep(0.1)
        year = input("Please enter your birth year\n")
        time.sleep(0.5)
        clear_terminal()
        time.sleep(0.5)
    elif (len(year) < 4 or len(year) > 4) or not year.isdigit:
        print("Invlalid birth year try again")
        time.sleep(2)
        clear_terminal()
        time.sleep(0.5)
        year = input("Please enter your birth year\n")
        time.sleep(0.5)
        clear_terminal()
        time.sleep(0.5)   
    else:
        break

length_name = len(name)

password = name[0].upper() + surname[-1].upper() + year[2:4] + name[1:length_name] + year[0:2] + str(random.randint(1,1000)) + random.choice("!@#$%^&*") + surname[2:len(surname)]

print(password)
time.sleep(4)
exit

