''' 
Gacha Balance Box Mechanism
1. if you gacha basic it costs 50
2. if you gacha elite it costs 500






'''
import random

basic = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
elite = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
premium = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]


def intro():
    print('WELCOME TO THE AMAZING GAMBLING EXPERIENCE')
    print('CHOOSE YOUR GAMBLING BOX')
    print('1. BASIC BOX (COST: 50)')
    print('2. ELITE BOX (COST: 500)')
    print('3. PREMIUM BOX (COST: 5000)')
    print('4. EXIT')

def main(blnc: int):
    balance = blnc
    
    while True:
        intro()
        choice = eval(input('Enter your choice --> '))
        match(choice):
            case 1:
                if balance < 50:
                    print('Insufficient Balance')
                else:
                    balance -= 50
                    balance += random.choice(basic)
                    print(f'Your balance is now {balance}')
            case 2:
                if balance < 500:
                    print('Insufficient Balance')
                else: 
                    balance -= 500
                    balance += random.choice(elite)
                    print(f'Your balance is now {balance}')
            case 3:
                if balance < 5000:
                    print('Insufficient Balance')
                else:
                    balance -= 5000
                    balance += random.choice(premium)
                    print(f'Your balance is now {balance}')
            case 4:
                print('GOODBYE!! SEE YOU SOON!')
                print(
    '''
    Welcome to ___
    =======
    1) Blackjack
    2) Gacha
    3) Check balance
    4) Save
    5) Load
    6) Quit
    '''
    )
                break
            

if __name__ == '__main__':
    main()
