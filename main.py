import something as smth
import blackjack as bj

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
inputlist=("1","2","3","4","5","6")

balance = 10000

def main():
    while True:
        usrinp = input()
        while usrinp not in inputlist:
            usrinp = input()
        match usrinp:
            case "1":bj.blackjack(balance)
            case "2":smth.main(balance)
            case "3":print(balance)
            case "6":break
            case _:print("No")

main()