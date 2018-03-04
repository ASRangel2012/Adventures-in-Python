#Lab 05
#This program passes arbitrary number of arguments in function.
#file_name: pizza.AngelSR.py

def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following topppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green papers','extra cheese')
