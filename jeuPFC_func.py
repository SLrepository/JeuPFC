# -*- coding: utf-8 -*-

# This file includes all functions called in main

# import random functionnality
from random import *

# set players choices and players states
computer = {1:"pierre", 2:"feuille", 3:"ciseaux"}
result = {1:"égalité!!", 2:"perdu!!", 3:"gagné!!"}

"""
Function name: HelloThere():
Description: player's name acquisition
Argument(s): none
Return value: player's name
"""
def HelloThere():
    ze_name = input("Hi There, please entre your name : ") 
    print("Hi {}".format(ze_name))
    return(ze_name)


"""
Function name: user_choice()
Description: user choice acquisition
Arguments(s): none
Return value: user choice
"""
def user_choice():
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
 
"""
Function name: computer_choice()
Description: Random computer choice acquisition (between 1 to 3)
Argument(s): none
Return value: random number
"""
def computer_choice():
    return(randint(1,3))

"""
Function name: check_winner()
Description: Check winner's round
Argument(s): player choice (man) and computer draw (machine)
Return value: player status (1, 2 or 3)
"""
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
