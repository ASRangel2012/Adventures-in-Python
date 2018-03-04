#lab 5
#file_name:pizzas.AngelSR.Py

def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make"""
    print("n\Making a" + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
