#lab 07
#file_name:user_dict_AngelSR.py
#Program that loops through all the key-value pairs. Displays the keys, then displays the values.

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

for key, value in user_0.items():
    print("\nKey " + key)
    print("\nValue: " + value)
