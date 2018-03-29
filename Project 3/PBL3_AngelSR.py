#PBL3
#file_name:PBL3_AngelSR.py
#date:03.14.18
#programmer:AngelSR
#This is game in which it will prompt the player to enter a cave
#each cave will have different outcome
#health status will be updated each time player gets attacked
#player will be able to collect items presented by dragon or found at any point
#must greet player


import time
import random


#GREET USER
def greet_player(player_name):
    """Display simple greeting"""
    print("""WELCOME TO THE DRAGONS REALM, """ + player_name.upper() + "!"
          + """Take your time, but decide posthaste:
          For one mistake will cost more than you can make.
          Choose one path, choose one cave:
          For each wrong path chosen will lead to your disgrace.
          For each right path chosen will lead to a secret place.""")
player_name= input("What is your name?")


#PROGRAM STARTS HERE#

def choose_cave():
    """Player must choose cave 1 or cave 2"""
    cave = ''
    while cave !='1' and cave !='2':
        print('Which cave do you choose? (1 or 2)')
        cave = input()
    return cave

healthBar= {
    'lives':'5',
    'weapons':'',
    'gold bars' : '1',
    }

for key, value in healthBar.items():
    print(' ' + key + ' value: ' + value)

    
    
    




    

def check_cave(chosen_cave):
    """Is the cave friendly or deadly?"""
    print("As you approach the cave you feel your chest tightening....")
    time.sleep(3)
    print("its becoming harder to breath with each step...")
    time.sleep(2)
    print(" A mighty dragon roars in front of you and it chooses to...")

    friendlyCave= random.randint(1,2)

    if chosen_cave == str(friendlyCave):
        print('give you 2 gold bars!')
    else:
        print('destroys you with its fiery breath')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    greet_player(player_name)
    caveNumber= choose_cave()
    check_cave(caveNumber)
    print("Would you like to play again? (Yes or no)")
    playAgain=input()
    
