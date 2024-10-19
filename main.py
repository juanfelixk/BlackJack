import something as smth
import blackjack as bj

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
inputlist=("1","2","3","4","5","6")

def main():
    while True:
        usrinp = input("Enter your choice: ")
        while usrinp not in inputlist:
            usrinp = input("Invalid choice. Please try again: ")
        match usrinp:
            case "1":bj.blackjack(smth.load_balance())
            case "2":smth.main(smth.load_balance())
            case "3":print(f"Your current balance is ${smth.load_balance():,}.")
            case "4":
                smth.save_balance(smth.load_balance())
                break

main()