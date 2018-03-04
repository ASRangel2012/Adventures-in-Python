#lab 06
#Pass a value to the function
#the function will sotre the number inisde a variable result + display it
#date:03/01/18
#file_name:show_double_AngelSR.py

#function
def show_double(number):
    result = number * 2
    return result
#program starts here)
value = int(input("enter a number:"))
total = show_double(value)
print(total)


