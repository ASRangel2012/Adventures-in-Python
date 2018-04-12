#lab 08
#File_name:Inventory_Tag_AngelSR.py
#Print the data members of InvetoryTag
#Ex: if item_id is 314 and quantity_remaining is 500,
#print ID: 314, QTY:500

class Inventory_Tag():
    def __init__(self):
        self.item_id = 0
        self.quatity_remaining = 0

#create the instance of the class Invent Tag
red_sweater = Inventory_Tag()
red_sweater.item_id = 314
red_sweater.quantity_remaining = 500
print(red_sweater.item_id)
print(red_sweater.quantity_remaining)
