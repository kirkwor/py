'''
Created on 13 Jul 2017
@author: T
https://www.youtube.com/watch?v=6isuF_bBiXs
Tkinter:
+ standard lib
+ lightweight
+ good enough
- limited widgets
- strange import
- ugly
Python 3x
- ttk module (theme for better)
* run in transparent loop
* widgets are with parents
Geometry:
: absolute (avoid this) 
: pack
    + simple
    - not flexible
: grid
'''
from tkinter import *
from tkinter.ttk import *

class WithoutTtk():
    def __init__(self, root):
        self.frame = Frame(root)
        self.build_window()
        self.frame.pack(fill='both')
        
        menubar = Menu(root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(menu=menu_file, label="File")
        
    def build_window(self):
        label = Label(self.frame, text="How do I look?")
#        label.pack(side="top")
        label.grid(row=0, column=1)
        
        button_bad = Button(self.frame, text="Terrible", command=self.quit)
#        button_bad.pack(side="left")
        button_bad.grid(row=0, column=0)
#        button_bad.grid(row=0, column=0, sticky="E")
        
        button_good = Button(self.frame, text="not bad", command=self.quit)
#        button_good.pack(side="right")
        button_good.grid(row=0, column=2)
#        button_good.grid(row=0, column=2, sticky="W")
        
        self.frame.rowconfigure(0,weight=2) #  row 0 is the one which will grow
        self.frame.columnconfigure(1, weight=2)
        
    def quit(self):
        self.frame.quit()
        
if __name__ == '__main__':
    root = Tk()
    myApp = WithoutTtk(root)
    root.mainloop()