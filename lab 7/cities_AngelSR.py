#lab 07
#Letting the user choose when to quit
#file_name:cities_AngelSR.py
#date:03/08/18

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter quit when you are finished."
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
    
