
#file_name:gold_increments_AngelSR.py

###functions###
gold_bar = 0
h = 0


def counter (c):
    c = c+ 1
    return c
####Ask to play again####

playAgain = 'y'
while playAgain == 'y':
    health = counter(gold_bar)
    print("You suck, here's five gold bars")
    if health == True:
        h = h + 5
        print('Youve earned: ' , h , 'shitty gold bars! Way to go, dumbass!')
    playAgain = input('Enter (y)')
    

    
