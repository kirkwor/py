# -*- coding: utf-8 -*-
'''
@author: Tomasz
taking all widgets inside one class
'''
import tkinter as tk
class tkButtons():
    # maaster is root window
    def __init__(self, master):
        frame1 = tk.Frame(master)
        frame1.pack()
        
        self.btnPrint = tk.Button(frame1, text='Print message', command=self.printMessage)
        self.btnPrint.pack(side='left')
        
        self.btnQuit = tk.Button(frame1, text='Quit', command=frame1.quit)
        self.btnQuit.pack(side="left")
        
        # FRAME with labels
        frame2 = tk.Frame(master)
        frame2.pack(side="left")
        
        self.lblOne = tk.Label(frame2, text="Tish is my text which shouuld be long", bg="red", fg="white")
        self.lblTwo = tk.Label(frame2, text="Second one", bg='green', fg='black')
        self.lblThree = tk.Label(frame2, text="Three", bg='blue', fg='black')
        self.lblOne.pack()
        self.lblTwo.pack(fill="x")
        self.lblThree.pack(side='left', fill="y")
        
        # FRAME WITH INPUT
        frame3 = tk.Frame(master)
        frame3.pack(side="right")
        
        self.lblFour = tk.Label(frame3, text='name')
        self.lblFive = tk.Label(frame3,text='Password')
        self.entry1 = tk.Entry(frame3)
        self.entry2 = tk.Entry(frame3)
        self.lblFour.grid(row=0, sticky='E')
        self.lblFive.grid(row=1)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
         
        self.chk = tk.Checkbutton(frame3, text="Keep me logged")
        self.chk.grid(columnspan=2)
        print(self.chk)
    # WORKING WITH MOUSE EVENTS
        frame4 = tk.Frame(master, width=300, height=250)
        frame4.bind("<Button-1>", self.leftClick)
        frame4.bind("<Button-2>", self.rightClick)
        frame4.bind("<Button-3>", self.middleClick)
        frame4.pack()
    # WORKING WITH EVENTS AND BUTTONS      
        frame5 =   tk.Frame(master)         
        frame5.pack()
        self.btn1 = tk.Button(frame5, text="Print name", command=self.printName)
        self.btn1.pack()
         
        self.btn2 = tk.Button(frame5, text='Second btn')
        # bind click of right mouse button with function
        self.btn2.bind("<Button-1>", self.print2Name)
        self.btn2.pack()
         
        self.btn3 = tk.Button(root, text='Third button')
        # bind to right button
        self.btn3.bind("<Button-3>", self.print3Name)
        self.btn3.pack()
         
    def printMessage(self):    
        print('workd')
    def printName(self):
        print('Hello')
         
    def print2Name(self, event):
        print(event, 'from event')
    def print3Name(self, event):
        print(event, 'btn 3')
         
    def leftClick(self, event):
        print('left')
    def rightClick(self, event):
        print('right')
    def middleClick(self, event):
        print('Middle')
#===============================================================================

if __name__ == '__main__':
    root = tk.Tk()
    myClass = tkButtons(root)
    root.mainloop()
