#this program demonstrates how a floating-point number can be displayed as currency
#Filename:dollar_display_AngelSR.py
#Date:02/02/2018

monthlyPay= 5000.0
annualPay= monthlyPay * 12

print('Your annual pay is $', \
      format(annualPay, ',.2f'), \
      sep = ' ') #sep argument
