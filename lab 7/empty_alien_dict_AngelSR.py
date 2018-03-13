#Lab 07
#file_name:empty_alien_dict_AngelSR.py
#Program with a dictionary that stores one kind of information about many objects

#Create dictionary of aliens with key-pair values

aliens = []

#make 30 aliens
for alien_number in range(30):
    new_alien= {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)


#show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show total number of aliens 
print("total number of aliens : " + str(len(aliens)))


for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color']== 'yellow'
        alien['color']=='medium'
        alien['points']= 10


#show the first 5 aliens
for alien in aliens[0:5]:
    print(alien)
print("...")

#expand loop using ELIF block to trun yellow into red and fast moving ones worth 15 points each.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['speed'] = 'yellow'
        alien['points']= 10
    elif alien['color']== 'yellow':
        alien['color'] = 'red'
        alien['speed']='fast'
        alien['points']= 15
