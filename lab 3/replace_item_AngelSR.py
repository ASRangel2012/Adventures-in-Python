#This program replaces an item on the list.
#User enters the items
#replace_item_AngelSR.py

def intro():
    print('Welcome, enter a list of pets')
intro() #call function
#variables

pets=[]
pets.append('cat')
pets.append('dog')
pets.append('fish')
print(pets)
#replace pet fish for pet rabbit
newPet= input('Enter new pet: ')
pets [2]= newPet
print(pets)

