#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Program name – my_restaurant_AngelSR.py
# Written by – AngelSR
# Date – 04/22/2018
# Description of the program. Will import two classes Restaurant and IcecreamStand


from restaurant_AngelSR import Restaurant, IceCreamStand

Copelands = Restaurant('Copelands', 'Game Meat')
Copelands.describe_restaurant()
Copelands.open_restaurant()
Copelands.set_number_served(585)

Brewsters = IceCreamStand('Brewsters', 'ice cream')
Brewsters.show_flavors()

