#Lab 4
#file_name:multiple_ifs_AngelSR.py
#This program demonstrates multiple if statements

#variables

car_year = int(input('What year is your vehicle?: '))

#test conditions
if car_year < 1970:
    print ("Few safety features.")

if car_year >= 1970:
    print ("Probably has seat belts.")

if car_year >= 1990:
    print ("Probably has anti-lock brakes.")

if car_year >= 2000:
    print ("Probably has air bags.")
    
