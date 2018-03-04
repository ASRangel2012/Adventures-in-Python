#Pizza_Party_AngelSR.py
#Angel Selva Rodriguez
#02/12/18
#This program is for someone planning a party. Will demonstrate use of lists.


 #intro 
def intro(): 
    print("How's it going? Planning a party? Start here!")
    
intro() #call function




#ask user to enter guests

def play():   
    print('please enter your guests')
    guests = []

    again = 'y'
    while again == 'y':
        new_guests = input("Enter a guest : ' ")
        guests.append(new_guests)
        print('next guest please: ' )
        again = input('y = yes, anything else = no: ')
    
#display final lists of guests
        print('Your guests are ')
    for my_guest in guests :
        print(my_guest)
#ask user to enter food items 

    print('Please enter food items for party.')
    food_items = []

    new_food = 'y'
    while new_food == 'y':
        new_items = input("Enter new food item : ' " )
        food_items.append(new_items)
        print('next item please : ')
        new_food = input('y = yes, anything else = no')
#displays new food
    print('The food for the party is as follows')
    for new_food in food_items :
        print(new_food)


    


#added new guests and removing old guests
        





### this will ask user to play again. 
    while True:
        answer = input("do you want to contnue planning?")
    if answer == 'yes':
        play = ()
    elif answer == 'no':
                break
            else:
                print('dont understand')
                
          
    
      

    

