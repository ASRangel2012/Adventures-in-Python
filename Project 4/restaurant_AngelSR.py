#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program name – restaurant_AngelSR.py
# Written by – AngelSR
# Date – 04/22/2018
# Description of the program. Will use __init__ method for Restaurant class which will,
#store two atrributes(restaurant_name, cuisine_type) and methods describe_restaurants()
#Will display message about restaurant

class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())



restaurant = Restaurant('Chumbucketeer', 'seafood')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

Lucky_guys = Restaurant('Lucky Guys', 'Bagels')
Lucky_guys.describe_restaurant()

Dianes = Restaurant("Diane's Palace", 'gourmet foods')
Dianes.describe_restaurant()

Chinese = Restaurant('Hot Wok', 'Chinese food')
Chinese.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 90
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(569)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(1245)
print("Number served: " + str(restaurant.number_served))


Brewsters = IceCreamStand('Brewsters Ice Cream')
Brewsters.flavors = ['vanilla', 'chocolate', 'Chocolote w/PB Buckeyes','cotton candy']

Brewsters.describe_restaurant()
Brewsters.show_flavors()
