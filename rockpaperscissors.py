from multiprocessing import RLock
import random 
import math 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")

while True:
    print("Enter number 1 for Rock, 2 for Paper and 3 for Scissors ")
    choice = int(input("User Turn:-"))
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input:-"))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    
    print("You chose: " +choice_name)
    print("Now computer, please chose your turn")
    comp_choice= random.randint(1,3)
    


    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissor'
    
    
    
    print("\nComputer chose " +comp_choice_name)

    if ((choice==1 and comp_choice==3)or(choice==3 and comp_choice==1)):
        print("\nRock wins!!", end="")
        result="Rock"
    elif ((choice==2 and comp_choice==3)or(choice==3 and comp_choice==2)):
        print("\nScissor Wins!!",end="")
        result='Scissor'
    elif((choice==comp_choice)):
        print("Both chose the same")
    else:
        print("\nPaper Wins!!",end="")
        result='Paper'
    
    if result==choice_name:
        print("\nUser is the winner!!")
    else :
        print("\nComputer is the winner!")
    print("\nDo you wish to continue? (Yes/No)")
    ans=input()
    if ans== 'no' or 'No':
        break
    

    print("\nThanks for playing")






