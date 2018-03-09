#lab 07
#file_name:pets_ AngelSR.py
#.remove method from lists

pets = 'dog cat parrot cat bird jaguar kitty cat aligator ants'
pet_list = pets.split()
print(pet_list)

while 'cat' in pet_list:
    pet_list.remove('cat')
print(pet_list)
