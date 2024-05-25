import random
def win(computer,you):
    if(computer==you):
        print("game draw")
        playAgain()
    elif(computer=="rock"):
        if(you=="paper"):
            print("Congratulation!! you win")
            playAgain()
        if(you=="scissor"):
            print("Sorry!! you loose win")
            playAgain()
    elif(computer=="paper"):
        if(you=="rock"):
            print("Sorry!! you loose")
            playAgain()
        if(you=="scissor"):
            print("Congratulation!! you win")
            playAgain()
    else:
        if(you=="rock"):
            print("Congratulation!! you win")
            playAgain()
        if(you=="paper"):
            print("Sorry!! you loose win")
            playAgain()

def playAgain():
    
    wish=input("Enter yes to play and no to exit: ")
    wish=wish.lower()
    if (wish=="yes"):
       rNo=random.randint(1,3)
       if(rNo==1):
            computer="paper"
       elif(rNo==2):
            computer="rock"
       else:
            computer="scissor"
       print("your choices are: rock   paper   scissor:")
       you=input("Enter your choice:   ")
       print(f"computer chooses:   {computer}")
       win(computer,you)
    elif(wish=="no"):
       exit()
    else:
        print("you are supposed to enter yes or no")
        playAgain()
playAgain()



