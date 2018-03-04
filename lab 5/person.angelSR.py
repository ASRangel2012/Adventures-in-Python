#Lab 5
#02/22/18
#programmer:AngelSR

def build_person(first_name, last_name, age = ''):
    """Return a dictionary of information about a person"""
    person = { 'first_name': first_name, 'last_name' :last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age = 27)
    
print(musician) 
