#lab 08
#date:03/29/2018
#file_name: class_time_AngelSr.py

class Time():
    def __init__(self):
        self.hours  = 0
        self.minutes = 0

        
my_time = Time() #instance of the class Time
my_time.hours = 7
my_time.minutes = 15
print('It took 50 miles to run: ' )
print(str(my_time.hours) + ' ' + "hours")
print(str(my_time.minutes) + ' ' + "minutes")

