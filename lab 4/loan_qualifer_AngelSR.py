#lab 4
#filename:Loan_qualifer_AngelSR.py
#02/15/18
#intro

def intro():
    print('Welcome, This program tests for a loan app')
    print('Are you ready to start?')

intro() #call function

#variable constraints
min_salary = 30000.0 #minimal salary 
min_years = 2        #minimum years on the job

#Get cust annual salary

salary = float(input('Enter your annual salary.'))

#get number of years on the job
years_on_job = int(input('Enter the number of years employed: '))

#determines whether you qualify
if salary >= min_salary:
    if years_on_job >=min_years:
        print('You qualify for this loan!')
    else:
        print('You need at least 2 years.')
else:
        print('you do not qualify for this loan.')

