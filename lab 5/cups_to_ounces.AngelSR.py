#this program converts cups to ounces, based on 1 cup = 8 ounces
#program name: cups_to_ounces.AngelSR.py

def main():
    intro()
    cups_needed = int(input('Enter the number of cups :'))
    cupts_to_ounces(cups_needed)

def intro():
    print('This program converts measurements')
    print('Coverts cups to ounces')
    print('formula: 1 cup = 8 ounces')

def cups_to_ounces(cups):
    ounces = cups * 8
    print('That converts to' , ounces, 'ounces')
    

main()
