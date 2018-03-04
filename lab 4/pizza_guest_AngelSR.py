#Lab 4
#file_name:pizza_guest_AngelSR.py
#This program populates a empty guest list and displays the list.

#program starts here
guests= []
#control variable

again = 'y'

#loop starts here
while again == 'y':
    new_guests = input("Enter a guest : ' ")
    guests.append(new_guests)
    print('next guest please: ' )
    again = input('y = yes, anything else = no: ')
    
    

#back in program
print ('n\guest : ') 
for my_guest in guests:
    print(my_guest)
