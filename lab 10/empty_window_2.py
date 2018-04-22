import tkinter
import tkinter.messagebox
class MyGUI:
    def _init_(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, \
                                    text = 'hello world!')
        self.label2 = tkinter.Label(self.main_window, \
                                    text = 'MY GUI PROGRAM!')
        self.my_button = tkinter.Button(self.main_window, \
                                        text = 'Click Me!', \
                                        command = self.do_something)
        self.label1.pack(side = 'left')
        self.label2.pack(side = 'right')
        self.my_button.pack()
        
        tkinter.mainloop()
    def do_something(self):
            tkinter.messagebox.showinfo('Response', \
                                        'thanks for clicking the button')
my_gui = MyGUI()
