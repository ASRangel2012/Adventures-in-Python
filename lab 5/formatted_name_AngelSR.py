#lab 5
#file_name: Formatted_name_AngelSR.py
#this program takes first and last name and returns full name
#date:02/22/18

def get_formatted_name(first_name, last_name):
    """Return formatted name"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

