# -*- coding: utf-8 -*-
from random import *

 
computer = {1:"pierre", 2:"feuille", 3:"ciseaux"}
result = {1:"égalité!!", 2:"perdu!!", 3:"gagné!!"}

def HelloThere():
    """
    Player's Name
    """
    ze_name = input("Hi There, please entre your name : ")
    print("Hi {}".format(ze_name))
    return(ze_name)

def user_choice():
    """
    user choice acquisition
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
    Random computer choice acquisition
    """
    return(randint(1,3))

def check_winner(man, machine):
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

scores_file = open("scores.txt", "a+")
Name = HelloThere()

while 1:
    score_man, score_machine  = 3, 3
    while score_man != 0 and score_machine != 0:
            ze_man = user_choice()
            n = computer_choice()
            status = check_winner(ze_man, computer[n])
            if status == 3:
                score_man -= 1
            if status == 2:
                score_machine -= 1
            print(result[status])
            if score_man == 0:
                print("You won {}!!!".format(Name))
                print("You won {}!!!".format(Name), file=scores_file)
            if score_machine == 0:
                print("Computer Won!!!")
                print("Computer Won!!!", file=scores_file)
    if (input("Still willing to play {} (Enter or anything else (+enter) for yes / no (+enter) for no) ? ".format(Name)) == "no"):
        break
print("Looking forward to seing you soon {}!".format(Name))
scores_file.close()



