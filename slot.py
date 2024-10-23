import random
import time
import os

symbols = ["🍎", "💎", "🍇", "⭐️", "💰"]

def save_balance(balance):
        with open("balance.txt", "w") as file:
            balance = str(balance)
            file.write(balance)  

def load_balance():
        with open("balance.txt", "r") as file:
            bal = file.read().strip()
            return int(bal)

def add_balance(amount):
    balance = load_balance()
    balance += amount
    save_balance(balance)
    time.sleep(1)
    print(f"Your current balance is ${balance:,}.")
    input("Press Enter to continue...")
    os.system("clear") #FIXME: Change to "cls" for Windows

def spin_wheels():
    wheel1 = symbols[random.randint(0, 4)]
    wheel2 = symbols[random.randint(0, 4)]
    wheel3 = symbols[random.randint(0, 4)]
    return wheel1, wheel2, wheel3

def print_wheels(wheels):
    print(f"{wheels[0]} | {wheels[1]} | {wheels[2]}")

def check_result(wheels):
    if wheels[0] == wheels[1] == wheels[2]:
        print("JACKPOT! All symbols match!")
        print("Adding $1,000 to balance...")
        add_balance(1000)
    elif wheels[0] == wheels[1] or wheels[0] == wheels[2] or wheels[1] == wheels[2]:
        print("Two symbols match!")
        print("Adding $500 to balance...")
        add_balance(500)
    else:
        print("Better luck next time!")
        input("Press Enter to continue...")
        os.system("clear") #FIXME: Change to "cls" for Windows

def play_slot_machine():
    input("\nPress Enter to spin the slot machine...")
    print("Spinning...")
    time.sleep(1.5)
    wheels = spin_wheels()
    print_wheels(wheels)
    check_result(wheels)
    save_balance(load_balance())
