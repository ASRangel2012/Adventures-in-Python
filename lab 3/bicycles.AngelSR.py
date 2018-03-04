#Lab 03 Lists
#This program pulls out the first bicycle in the list and composes a message
#using that value and store it in the variable message
#filename: bicycles.AngelSR.py
#date:02/01/18

bicycles = ['trek','cannondale','redline','specialized'] #syntax=0,1,2,3
print(bicycles)
print(bicycles[0])

#format the element 'trek' more neatly by using the title() method
print(bicycles[0].title())

print(bicycles[-1])#last item on the list, can use 3 or -1

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


print(bicycles[2])


