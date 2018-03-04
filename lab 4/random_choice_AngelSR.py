#Programmer: AngelSR
#file_name:Random_choice_AngelSR.py
#date:02/15/18
#This program selects randomly from a set using the choice() method.

import random

menu = ['pizza','salad','chips','plates','cakes','sodas']
guests = ['mary','bob','donna','kate','pete','walter']

for guest in guests:
    person = input('what is your name?')
    if person == 'pete':
        print('bring', menu[2], '!', guests[4])
    else:
         print(guests [0], 'is bringing', random.choice(menu)) #choice() method
         print(guests [1], 'is bringing', random.choice(menu))
         print(guests [2], 'is bringing', random.choice(menu))
         print(guests [3], 'is bringing', random.choice(menu))
         print(guests [4], 'is bringing', random.choice(menu))
         print(guests [5], 'is bringing', random.choice(menu))
