from random import randint
import os 
cards=[
    [1,2,3,4,5,6,7,8,9,"J","Q","K","A"], #heart
    [1,2,3,4,5,6,7,8,9,"J","Q","K","A"], #diamond
    [1,2,3,4,5,6,7,8,9,"J","Q","K","A"], #clover
    [1,2,3,4,5,6,7,8,9,"J","Q","K","A"] #spade
]
running=True
totalavailablecards=[12,12,12,12] # Theres a random bug relating to this idk how it happens or how to fix it

def getcard():
    global suite
    global value
    suite=randint(0,3)
    value=randint(0,totalavailablecards[suite])
    totalavailablecards[suite]-=1

def userace():
    for i in knownplayercard:
        if i[0]=="A" and i not in useraceoccurence:
            print("You got an ace, would you like to make the value 1 or 11?")
            useraceoccurence.append(i)
            aceinput=input()
            while aceinput != "1" and aceinput != "11":
                aceinput=input().lower()
            aceinput=int(aceinput)
            match aceinput:
                case 1:
                    choices.append(1)
                case 11:
                    choices.append(11)

suitedict={
    "0":"Heart",
    "1":"Diamond",
    "2":"Clover",
    "3":"Spade"
}

special={"J":10,"Q":10,"K":10}

def totalfunc(a,b=0):
    for i in range(len(a)):
        if a[i][0] in special:
            b+=special[a[i][0]]
        elif type(a[i][0]) != str:
            b+=a[i][0]
    if len(choices)!=0:
        for i in choices:
            b+=i
    return b

def storecard(name,l):
    global cards
    for i in range(l):
        getcard()
        name.append((cards[suite][value],suitedict[str(suite)]))
        cards[suite].pop(value)
    
def dealerchoice():
    cardstring=""
    for i in knowndealercard:
        cardstring+=str(i[0])+" "+i[1]+", "
    print(f"Dealer has the following cards: {cardstring[:len(cardstring)-1]}")
    global totaldealervalue
    dealerhit=True
    while dealerhit:
        if totaldealervalue < 17:
            print("Dealer hit")
            storecard(knowndealercard,1)
            print(f"Dealer got {knowndealercard[len(knowndealercard)-1][0]} {knowndealercard[len(knowndealercard)-1][1]}")
            totaldealervalue=totalfunc(knowndealercard)
        else:
            dealerhit=False
        for i in knowndealercard:
            if i[0]=="A":
                if totaldealervalue<=10:
                    dealerace.append(1)
                else:
                    dealerace.append(11)
    checkwin()

def checkwin():
    print(f"Total user {totalplayervalue} Total dealer {totaldealervalue}")
    if (totaldealervalue > totalplayervalue or  totalplayervalue>21 or (totaldealervalue==21 and totalplayervalue!=21)) and totaldealervalue  <= 21:
        print(f"You lost, the dealer had {totaldealervalue}")
        input("Input anything to continue")
        # TODO Reduce balance
        os.system("cls")
    if totalplayervalue>totaldealervalue or totaldealervalue>21 or (totalplayervalue==21 and totaldealervalue!=21) and totalplayervalue  <= 21:
        print(f"You won, the dealer had {totaldealervalue}")
        input("Input anything to continue")
        # TODO Increase balance
        os.system("cls")
    if (totalplayervalue>=21 and totaldealervalue>=21):
        print("Draw")
        input("Input anything to continue")
        os.system("cls")

def checkautowin():
    if totaldealervalue==21 or totalplayervalue>21:
        print(f"You lost, the dealer had {totaldealervalue}")
        input("Input anything to continue")
        # TODO Reduce balance
        os.system("cls")
        return False
    if totalplayervalue==21 or totaldealervalue>21:
        print(f"You won, the dealer had {totaldealervalue}")
        input("Input anything to continue")
        # TODO Increase balance
        os.system("cls")
        return False
    if totalplayervalue>=21 and totaldealervalue>=21:
        print("Draw")
        input("Input anything to continue")
        os.system("cls")
        return False
    return True
    
while running:
    print('''
=============================================================================================================
WELCOME TO BLACK JACK!
HOW TO PLAY:
    1. You will be playing against the dealer. 
    2. The game will be won when the sum of either your or the dealear's cards is closer to or reaches 21.
    3. If the sum of either your or the dealear's cards exceeds 21, that party will lose the bet. 
    4. To start, decide the amount of bet
    5. The dealer and you will be given 2 cards initially. Your cards are visible to you.
    6. One of the dealer's cards will be visible to you.
    7. You should decide to stand (stop getting cards) or hit (get more cards). 
    8. You can choose to raise the bet every time receiving a card.
=============================================================================================================
Inputs:
1. Play 
2. Quit
    ''')
# for save and load i will try to implement later
# TODO input the number to bet or smth
    optioninp=input()
    while optioninp != "1" and optioninp != "2": # Change later when more options are added
        print("A") 
        optioninp=input()
    match optioninp:
        case "1":
            running=True
            balance = 100000 #arbitrary number
            suite,value,totalplayervalue,totaldealervalue=0,0,0,0
            choices,dealerace,useraceoccurence=[],[],[]
            flag=True
            knowndealercard=[]
            knownplayercard=[]
            playercardstring=""

            storecard(knowndealercard,2)
            storecard(knownplayercard,2)

            showndealercard=knowndealercard[randint(0,1)]

            for i in knownplayercard:
                playercardstring+=str(i[0])+" "+i[1]+", "

            print(f"Your card is {playercardstring}and one of the dealer card is {str(showndealercard[0])+" "+showndealercard[1]}")

            print("Would you like to hit (get more cards)? (y/n)")
            userinp=input().lower()
            while userinp != "n" and userinp != "y":
                userinp=input().lower()
            userace()
            totalplayervalue=totalfunc(knownplayercard,totalplayervalue)
            totaldealervalue=totalfunc(knowndealercard,totaldealervalue)
            if userinp=="n":
                print("a")
                dealerchoice()
            while userinp=="y" and flag:
                storecard(knownplayercard,1)
                playercardstring+=str(knownplayercard[len(knownplayercard)-1][0])+" "+knownplayercard[len(knownplayercard)-1][1]+","
                userace()
                print(f"Your card is {playercardstring}and one of the dealer card is {str(showndealercard[0])+" "+showndealercard[1]}")
                if knownplayercard[len(knownplayercard)-1][0] == "A":
                    totalplayervalue+=choices[len(choices)-1]
                elif knownplayercard[len(knownplayercard)-1][0] in special:
                    totalplayervalue+=special[knownplayercard[len(knownplayercard)-1][0]]
                else:
                    totalplayervalue+=int(knownplayercard[len(knownplayercard)-1][0])
                flag=checkautowin()
                if flag==False:
                    break
                print("Would you like to hit (get more cards)? (y/n)")
                userinp=input().lower()
                while userinp != "n" and userinp != "y":
                    userinp=input().lower()
                if userinp=="n":
                    print("a")
                    dealerchoice()
        case "2":
            running=False