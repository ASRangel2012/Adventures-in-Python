#lab 08
#date:03/29/2018


class PatientData():
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0

#create instance

lunaLoveGood = PatientData()
print('patient data (before): ', end = ' ')
print(lunaLoveGood.height_inches, 'in, ', end=' ')
print(lunaLoveGood.weight_pounds, 'lbs')

#after: 63 inches and 115 lbs
lunaLoveGood.height_inches = 63
lunaLoveGood.weight_pounds = 115

print('patient data (after): ', end=' ')
print(lunaLoveGood.height_inches, 'in. ', end='  ')
print(lunaLoveGood.weight_pounds, 'lbs')


