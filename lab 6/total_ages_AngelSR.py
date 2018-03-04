#lab 06
#file_name:total_ages_AngelSR.py
#date:03/01/18
#programmer:AngelSR

def sum(num1, num2):
    result = num1 + num2
    return result

first_age = int(input('Enter your age :'))
second_age = int(input('Enter your friends age: '))
total = sum(first_age,second_age)
print('Together you are: ', total)
