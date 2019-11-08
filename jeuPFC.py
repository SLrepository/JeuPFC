# -*- coding: utf-8 -*-

# import random functionnality
from random import *
# import JeuPFC functions
from jeuPFC_func import *

# set players choices and players states
computer = {1:"pierre", 2:"feuille", 3:"ciseaux"}
result = {1:"égalité!!", 2:"perdu!!", 3:"gagné!!"}

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



