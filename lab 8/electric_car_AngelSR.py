#lab 08
#file_name:elecric_car_AngelSR.py
#date:03/29/18
#Inheritance

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initiliaze attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
          if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
          else:
              print("You can't roll back on odometer!")
    def increment_odometer(self, miles):
            self.odometer_reading += miles

                    



class ElectricCar(Car):
    """This represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attribute of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla' , 'model s' , 2016)
print(my_tesla.get_descriptive_name())
