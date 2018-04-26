#----------------------------------------------------------------------------
#Program name: Menu driven program
#– filename P5_AngelSR.py
# Written by AngelSR
# Date – 04/24/2018
# Description of the program. menu driven program 
#----------------------------------------------------------------------------

       

# import function

import turtle
from tkinter import Tk, Label, Button


# menu selection

DRAW_SQUARE_CHOICE = 1
DRAW_RECTANGLE_CHOICE = 2
DRAW_CIRCLE_CHOICE = 3
SIMPLE_GUI_CHOICE = 4
QUIT_CHOICE = 5

choice = 0

#menu display

def display_menu():
    print('MENU')
    print('Press 1 Draw Square')
    print('Press 2 Draw Rectangle')
    print('Press 3 Draw Circle')
    print('Press 4 Show a window message')
    print('Press 5 to Quit')

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Simple GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("How's it going?")


#choice

while choice!= QUIT_CHOICE:
          display_menu()
          choice= int(input('Enter your choice:'))
          if choice == DRAW_SQUARE_CHOICE:
              square =turtle.Turtle()
              length = float(input('Enter the length of the side:'))
              square.right(90)
              square.fd(length)
              square.right(90)
              square.fd(length)
              square.right(90)
              square.fd(length)
              square.right(90)
              square.fd(length)
              turtle.done()

          elif choice == DRAW_RECTANGLE_CHOICE:
              length1= float(input('Enter length of side 1:'))
              length2= float(input('Enter length of side 2:'))
              rectangle=turtle.Turtle()
              rectangle.right(90)
              rectangle.fd(length1)
              rectangle.right(90)
              rectangle.fd(length2)
              rectangle.right(90)
              rectangle.fd(length1)
              rectangle.right(90)
              rectangle.fd(length2)
              turtle.done()

          elif choice == DRAW_CIRCLE_CHOICE:
              circle=turtle.Turtle()
              circle.circle(float(input('Input the diameter')))
              turtle.done()
              
              
          elif choice == SIMPLE_GUI_CHOICE:
              root = Tk()
              my_gui = MyFirstGUI(root)
              root.mainloop()
              
          elif choice == QUIT_CHOICE:
              print('Quit Program...')
          else:
              print('WRONG CHOICE BUDDY,TRY AGAIN.')
              
               
         
