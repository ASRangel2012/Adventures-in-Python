#lab 08
#file_name: car_AngelSR.py
#date:03/29/2018
#This program demonstrates setting values for atrribrutes in instances

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initiliaze attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
