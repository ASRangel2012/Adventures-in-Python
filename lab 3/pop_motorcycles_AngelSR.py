#Lab 3: Lists (CHAPTER 3)
#pop method
#this program let us pop a motorcycle from the list of motorcycles
#filename:pop_motorcycles_AngelSR.py
#02/01/18

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
print(' ')
motorcycles[0] = 'ducati' #this will replace honda
print(' ')
print(motorcycles)
print(' ')
motorcycles.append('ducati')
print(motorcycles)



motorcycles.insert(2, 'America')
print(motorcycles)
del(motorcycles[0])
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
firstOwned= motorcycles.pop(0)
print('The first motorcycle I owned was a ' + firstOwned.title() + '.')



#Removing an item by value
motorcycles.append('harley')
motorcycles.remove('yamaha')
print(motorcycles)
