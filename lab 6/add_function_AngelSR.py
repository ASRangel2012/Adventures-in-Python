#lab 06
#This program passes two values to the function Add_Function
#file_name:add_function_AngelSR.py
#date:03/01/18
#programmer:AngelSR

def add_function(v1, v2):
    result = v1 + v2
    return result


####PROGRAM#######
number1= int(input("Enter number 1:"))
number2 = int(input("Enter number 2:"))
total = add_function(number1,number2)
print(total) 
