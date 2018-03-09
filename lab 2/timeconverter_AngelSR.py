#this program gets the number of seconds from the user
#converts the number of seconds to hours, minutes and seconds
#filename:time_converter_AngelSR.py
#02/2/18

#Get the number of seconds from user
totalSeconds = float(input('enter the number of seconds:'))

#get the number of hours
hours = totalSeconds // 3600

#get the number of remaining minutes
minutes = (totalSeconds // 60) % 60

#get number of remaining seconds
seconds = totalSeconds % 60

#display results
print('here is the time in hours, minutes and seconds : ' )
print('hours', hours)
print('minutes', minutes)
print('seconds', seconds)

