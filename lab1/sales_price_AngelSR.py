#This program discounts purchase price by 20 percent.
#program name: sales_price_AngelSR.py
#date:01/24/18
#progrmr: A.SelvaRodriguez

#input


print( "How much is the value of your purchase?")
purchase = 0

       
action = input("Type amount of Purchase")

if action.isdigit():
       purchase=float(action)

coupon = input("type in promotional percent off")

if coupon.isdigit():
       coupon=float(coupon) / 100 * purchase
       print(coupon)
       print("This is your final price")
print(purchase - coupon) 
