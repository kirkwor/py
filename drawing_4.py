'''
Created on 13 Jul 2017

@author: T
'''
from tkinter import *
from tkinter.ttk import *

class TkCanvas():    
    
    def __init__(self, root):
        
        self.frame = Frame(root)
        self.canvas = Canvas(self.frame)
        self.canvas.grid(row=0, column=0)
        
        self.draw_rect()
        
        btnQuit = Button(self.frame, text="Quit", command=self.quit)
        btnQuit.grid(row=1, column=0, sticky=(S,E))
        #=======================================================================
        # add to draw 
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0, weight=2)
        #=======================================================================
        self.frame.pack(fill=BOTH, expand=True)
        #=======================================================================
        # Adding mose events
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.initial=(0,0)
        #=======================================================================
        
    def draw_rect(self):
        self.canvas.create_rectangle((100,100),(30,40))
        
    def quit(self):
        self.frame.quit()  
          
    def start_line(self, event):
        self.inital = (event.x, event.y) 
        
    def draw_line(self, event):
        self.canvas.create_line((self.inital[0], self.inital[1], event.x, event.y))
        self.inital = (event.x, event.y)
        
if __name__ == '__main__':
    root=Tk()
    app = TkCanvas(root)
    root.mainloop()