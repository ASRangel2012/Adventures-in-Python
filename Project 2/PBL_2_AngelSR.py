#----------------------
#file_name:PBL2_AngelSR.py
#Programmer:AngelSR
#Date:03.06.18
#Python program that simulates 7/11 game
#----------------------
import random
import time
import randrange


def intro():
    """Introduce game and rules"""
    print('''The name of the game is 7/11! Player must roll dice and if the
             outcome is 7, 11 or double player wins!If anything else GAME OVER''')
intro()



def roll():
        dice = randrange(1,6) + randrange (1,6)
        return dice

    
def game():
    dice = roll()
    if dice in (2,3,12):
        return False

    if dice in (7,11):
        return True
    while True:
        new_roll = roll()

    if new_roll == dice:
        return game


def sim_games(n):
    wins = losses = 0
    for i in range(n):
        if game():
            wins = wins + 1
        if not game():
            losses = losses + 1
    return wins, losses
sim_games()

def main():
    n = eval(input("How many games of 7/11 Double would you like to play? "))
    w, l = sim_games(n)
    print("wins:", w,"losses:", l)
    return main()
