''' 
Gacha Balance Box Mechanism
1. If you choose gacha basic it costs 50
2. If you choose gacha elite it costs 500
3. If you choose gacha premium it costs 5000






'''
import random

basic = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
elite = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
premium = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
items = ["Blue Fish🐟", "Magic Eggplant🍆", "Shiny Crown👑"]
def intro():
    print('\nWELCOME TO THE AMAZING GAMBLING EXPERIENCE')
    print('CHOOSE YOUR GAMBLING BOX')
    print('1. BASIC BOX (COST: 50)')
    print('2. ELITE BOX (COST: 500)')
    print('3. PREMIUM BOX (COST: 5000)')
    print('4. EXIT')

def save_balance(balance):
        with open("balance.txt", "w") as file:
            balance = str(balance)
            file.write(balance)  

def load_balance():
        with open("balance.txt", "r") as file:
            bal = file.read().strip()
            return int(bal)

def main(blnc: int):
    balance = blnc
    
    while True:
        intro()
        choice = eval(input('Enter your choice: '))
        match(choice):
            case 1:
                if balance < 50:
                    print('Insufficient balance.')
                else:
                    balance -= 50
                    basic_choice = random.choice(basic)
                    if random.choice(basic) >= 90:
                        print(f"Congratulations! You have gained a {items[0]}! (worth ${basic_choice})")
                        balance += basic_choice
                    else:
                        balance += basic_choice
                    print(f'Your balance is now ${balance:,}.')
            case 2:
                if balance < 500:
                    print('Insufficient balance.')
                else: 
                    balance -= 500
                    elite_choice = random.choice(elite)
                    if random.choice(elite) >= 900:
                        print(f"Congratulations! You have gained a {items[1]}! (worth ${elite_choice})")
                        balance += elite_choice
                    else:
                        balance += elite_choice
                    print(f'Your balance is now ${balance:,}')
            case 3:
                if balance < 5000:
                    print('Insufficient balance.')
                else:
                    balance -= 5000
                    premium_choice = random.choice(premium)
                    if random.choice(premium) >= 9000:
                        print(f"Congratulations! You have gained a {items[2]}! (worth ${premium_choice})")
                        balance += premium_choice
                    else:
                        balance += premium_choice
                    print(f'Your balance is now ${balance:,}')
            case 4:
                save_balance(balance)
                print('GOODBYE!! SEE YOU SOON!')
                print(
    '''
    Welcome to ___
    =======
    1) Blackjack
    2) Gacha
    3) Check balance
    4) Quit
    '''
    )
                break
            

if __name__ == '__main__':
    main()
