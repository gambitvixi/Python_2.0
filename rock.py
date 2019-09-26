#rock paper scissors game
from random import randint
#Super napredni ai, nema sta
def ai_choice():
    pick = randint(1,3)
    if pick == 1:
        return "rock"
    elif pick ==2:
        return "paper"
    else:
        return "scissors"
choice = "Yes"
while choice != ("n") and choice != ("N"):    
    play = str(input("Ok, smuck. What do you pick? "))
    comp = ai_choice()
    print ("And I pick " + comp)
    if play == comp:
        print ("Well, I guess it is a draw!")
    elif play == "rock" and comp == "paper":
        print ("I WIN! YOU LOSE!")
    elif play == "scissors" and comp == "rock":
        print ("I WIN! YOU LOSE!")
    elif play == "paper" and comp == "scissors":
        print ("I WIN! YOU LOSE!")
    elif comp == "rock" and play == "paper":
        print ("YOU ARE CHEATING!!!!!")
    elif comp == "scissors" and play == "rock":
        print ("YOU ARE CHEATING!!!!!")
    elif comp == "paper" and play == "scissors":
        print ("YOU ARE CHEATING!!!!!")
    else:
        print ("Learn to spell, Potter!")
    choice = str(input("Do you want to play a game rock/paper/scissors? \n Y/N "))