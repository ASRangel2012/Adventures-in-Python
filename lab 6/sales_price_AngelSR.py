#lab 06
#file_name:sales_price_AngelSR.py
#calculate the retail items sale price
discount_percent = .20

def get_regular_price():
    price = int(input("Enter the items regular price: "))
    return price

def discount(price):
    return price * discount_percent
#program starts here#

reg_price = get_regular_price()
#calculate
sales_price= reg_price - discount(reg_price)
#display

print('sales price is $', sales_price)
