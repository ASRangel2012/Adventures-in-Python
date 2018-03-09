#lab 07
#file_name:favorite_languages_AngelSR.py
#Dictionary that stores one kind of information about many objects
#date:03/09/18



#Define variable and set key-value pairs
favorite_languages = {
    'jen' : 'python',
    'drew' : 'c',
    'edward':'ruby',
    'phil':'python',
    }

#Use for loop and define new variable to get key-value pairs 
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

#Use .keys() to receive keys from dictionary. 
for name in favorite_languages.keys():
    print(name.title())
    
    
#same way to do what is above with name variable
for name in favorite_languages:
    print(name.title())
