#This program will help locating items on a large list
#index
#02/01/18
#programer:AngelSR

#intro
def intro():#function definition
    print('Welcome, you will be replacing your lunch today')
intro() #call function 

food = []
#add items
food.append('Burgers')
food.append('Chips')
food.append('Soda')
#display
print('Here is the revised list: ')
print(food)

#change item
item=str(input('Which item do you want to change?'))
          

#get index
itemIndex= food.index(item)
#get value to replace
newItem=input('Enter new value: ')

#replace the old item
food[itemIndex]= newItem

#display the list
print('Here is the revised list: ')
print(food)

