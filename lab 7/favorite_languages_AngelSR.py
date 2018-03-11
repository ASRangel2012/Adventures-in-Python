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
    'aaron':'',
    'hank':'',
    'gloria':'',
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


#send special message to only friends

friends = ['phil', 'jen']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")


#See who's not included(Hasn't taken the favorite language poll)


for name, language in sorted(favorite_languages.items()):
    if language == '':
        print("Take our poll and let us know what your favorite language is " + name.title() + "!")
    else:
        print("Thank you for taking the poll " + name.title() +"." + " \nI noticed your favorite language was " +
              language.title())

        
