# -*- coding: utf-8 -*-
# Inport random functionnality
from random import *

# set players choices and players states
computer = {1:"pierre", 2:"feuille", 3:"ciseaux"}
result = {1:"égalité!!", 2:"perdu!!", 3:"gagné!!"}

def HelloThere():
"""
Description: player's name acquisition
Argument(s): none
Return value: player's name
"""
    ze_name = input("Hi There, please entre your name : ")
    print("Hi {}".format(ze_name))
    return(ze_name)


def user_choice():
"""
Description: user choice acquisition
Arguments(s): none
Return value: user choice
"""
    player = input("Choose between 1)pierre 2)feuille 3)ciseaux ? ")
    while player not in ["pierre","feuille","ciseaux"]:
        if player == "1":
            player = "pierre"
        elif player == "2":
            player = "feuille"
        elif player == "3":
            player = "ciseaux"
        else:
            player = input("Choose between 1)pierre 2)feuille 3)ciseaux ? ")
    return(player)
 
def computer_choice():
"""
Description: Random computer choice acquisition (between 1 to 3)
Argument(s): none
Return value: random number
"""
    return(randint(1,3))

def check_winner(man, machine):
"""
Description: Check winner's round
Argument(s): player choice (man) and computer draw (machine)
Return value: player status (1, 2 or 3)
"""
    print("U chose -> {} Machine chose -> {}".format(man, machine))
    if man == machine:
        status = 1
    elif man == computer[1] and machine == computer[2]:
        status = 2
    elif man == computer[1] and machine == computer[3]:
        status = 3
    elif man == computer[2] and machine == computer[1]:
        status = 3
    elif man == computer[2] and machine == computer[3]:
        status = 2
    elif man == computer[3] and machine == computer[1]:
        status = 2
    elif man == computer[3] and machine == computer[2]:
        status = 3
    return(status)

"""
Program main
"""
# open scores.txt files in write mode
scores_file = open("scores.txt", "a+")
Name = HelloThere()

# Game forever loop (resart game)
while True:
    score_man, score_machine  = 3, 3
    # Round loop (end after 3 wins)
    while score_man != 0 and score_machine != 0:
            # get user choice
            ze_man = user_choice()
            # get random computer choice
            random_choice = computer_choice()
            # check who or what won
            status = check_winner(ze_man, computer[random_choice])
            # handle round score
            if status == 3:
                score_man -= 1
            if status == 2:
                score_machine -= 1
            print(result[status])
            # handle game winner
            if score_man == 0:
                print("You won {}!!!".format(Name))
                # update scores.txt file
                print("You won {}!!!".format(Name), file=scores_file)
            if score_machine == 0:
                print("Computer Won!!!")
                # update scores.txt file
                print("Computer Won!!!", file=scores_file)
    # restart or end game            
    if (input("Still willing to play {} (Enter or anything else (+enter) for yes / no (+enter) for no) ? ".format(Name)) == "no"):
        break
print("Looking forward to seing you soon {}!".format(Name))
# close scores.txt file
scores_file.close()



