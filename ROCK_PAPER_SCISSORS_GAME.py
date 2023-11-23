import random
print("~~~~~~~~~~ ROCK-PAPER-SCISSORS GAME ~~~~~~~~~~")
choice="YES"
userScore=computerScore=0
while(True):
    if choice=="YES":
        userChoice=input("Choose ROCK/PAPER/SCISSORS : ").upper()
        computerChoice=random.choice(["ROCK","PAPER","SCISSORS"])
        print(f"USER CHOOSE '{userChoice}'\nCOMPUTER CHOOSE '{computerChoice}'")
        if ((userChoice=="PAPER" and computerChoice=="ROCK") or (userChoice=="SCISSORS" and computerChoice=="PAPER") or (userChoice=="ROCK" and computerChoice=="SCISSORS")):
            print("USER WINS")
            userScore+=1
        elif userChoice==computerChoice:
            print("IT\'S A TIE")
        else:
            print("USER LOSES")
            computerScore+=1
        print("SCORE:\nUSER\'S SCORE    COMPUTER SCORE")
        print("     ",userScore,"             ",computerScore)
        choice=input("ARE YOU WANT TO PLAY AGAIN (YES/NO):").upper()
    else:
        print("YOU ARE EXITED")
        break
