#file_name: kilo_convert_AngelSR.py
import tkinter
class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        #frames
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        #create widgets
        self.prompt_label =tkinter.Label(self.top_frame,\
                            text = 'Enter distance in Kmts:')

        self.kilo_entry =tkinter.Entry(self.top_frame,\
                            width = 10)
        #packs
        self.prompt_label.pack(side = 'left')
        self.kilo_entry.pack(side = 'left')
        #widgets for middle frame
        self.descr_label =tkinter.Label(self.mid_frame,\
                            text = 'Convert to miles:')
        #object to output
        self.value = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame,\
                            textvariable = self.value)
           #pack middle frame
        self.descr_label.pack(side = 'left')
        self.miles_label.pack(side = 'left')
        #create buttons
        self.calc_button = tkinter.Button(self.bottom_frame,\
                            text = 'Convert', \
                            command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,\
                            text = 'Quit', \
                            command = self.main_window.destroy)
        #pack buttons.
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        #pack frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        #enter the mainloop
        tkinter.mainloop()
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = kilo * 0.6214
        self.value.set(miles)
kilo_conv = KiloConverterGUI()
        










        
       
         








         












        
        
        
