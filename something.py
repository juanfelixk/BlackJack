import random
import slot
import numberguess

basic = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
elite = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
premium = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

def intro():
    print('\nWELCOME TO THE AMAZING GAMBLING EXPERIENCE')
    print('CHOOSE YOUR EXPERIENCE')
    print('1. BASIC BOX (COST: 50)')
    print('2. ELITE BOX (COST: 500)')
    print('3. PREMIUM BOX (COST: 5000)')
    print('4. PLAY SLOT MACHINE')
    print('5. PLAY GUESS THE NUMBER')
    print('6. EXIT')

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
                    balance += random.choice(basic)
                    print(f'Your balance is now ${balance:,}.')
                save_balance(balance)
            case 2:
                if balance < 500:
                    print('Insufficient balance.')
                else: 
                    balance -= 500
                    balance += random.choice(elite)
                    print(f'Your balance is now ${balance:,}')
                save_balance(balance)
            case 3:
                if balance < 5000:
                    print('Insufficient balance.')
                else:
                    balance -= 5000
                    balance += random.choice(premium)
                    print(f'Your balance is now ${balance:,}')
                save_balance(balance)
            case 4:
                slot.play_slot_machine()
            case 5:
                numberguess.main()
            case 6:
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