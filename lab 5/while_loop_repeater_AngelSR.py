#lab 5
#file_name:while_loop_repeater_AngelSR.py
#date:02/22/2018
#programmer: AngelSR.
#An example of a loop program

import random
import time

def intro():
    print('play a guessing game against computer')
intro()
play_again = 'yes'

#loop

while play_again == 'yes':
    player_pick = int(input('enter a number between 1 and 8 : '))
    computer_pick = random.randint(1,8)
    time.sleep(3)
# decision

    if computer_pick == player_pick:
        print(" You're a winner!!! ")
    else:
        print('Sorry, the computer picked the winning number', computer_pick )

        play_again = input("type yes to play again")
