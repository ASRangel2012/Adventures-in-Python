#lab 10
#file_name:empty_window_AngelSR2.py

import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        #create a main window widget
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, \
                                   text = ('Hello, World'))
        self.label2 = tkinter.Label(self.main_window, \
                                    text = 'My GUI program!')

        self.my_button = tkinter.Button(self.main_window,\
                                        text = 'click me',\
                                        command = self.do_something)
                                       



        #call label widget using pack method
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'right')
        self.my_button.pack()
        # enter tkinter mailoop
        tkinter.mainloop()


    def do_something(self):
            tkinter.messagebox.showinfo('Response',\
                                        'Thanks for clicking!')

        #program
            #create an instance of MyGui class
my_gui = MyGUI()

