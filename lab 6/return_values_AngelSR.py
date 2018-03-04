#lab 06
#file_name: return_values_AngelSR.py
#date:03/01/18
#this program returns the contents of a list entered by user

def main():
    #get a list
    numbers = get_values()

    print('The numbers is the list are :')
    print(numbers)

#the get_value funtion gets a series of numbers
#from the user and stores them in the list
#the functions returns a reference to the list

def get_values():
    #create an empty list#
    values = []
    again = ('y')
    while again == 'y':
        num = int(input('Enter the number'))
        values.append(num)
        print('Do you want to add another number?')
        again = input('y = yes  otherwise anything else = no :')
        print()
        return values
main()
