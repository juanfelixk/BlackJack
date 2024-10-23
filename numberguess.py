import random

def save_balance(balance):
        with open("balance.txt", "w") as file:
            balance = str(balance)
            file.write(balance)  

def load_balance():
        with open("balance.txt", "r") as file:
            bal = file.read().strip()
            return int(bal)

def main():
    print("""
Welcome to the Number Guessing Game. 
Good Luck!
(Please enter a whole number)""")

    while True:
        bankroll = load_balance()
        secret_number = random.randint(1, 3)
        print(f"Your current bankroll is: ${bankroll:,}.")
        bet = int(input("\nEnter your bet amount: "))

        if bet<=0:
            print("Please enter a positive bet number.")
            continue
        
        elif bet > bankroll:
            print("You cannot bet more than your current bankroll.")
            continue
    
        userGuess = int(input("Guess a number between 1 and 3: "))

        if userGuess != secret_number:
            print(f"Oops, you lost! The secret number is {secret_number}. You lose ${bet}.")
            bankroll -= bet
            save_balance(bankroll)
        else:
            print(f"Yay! You got it! The secret number is {secret_number}. You win ${bet}.")
            bankroll += bet 
            save_balance(bankroll)

        if bankroll <= 0:
            print("You have run out of money! Game over.")
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break