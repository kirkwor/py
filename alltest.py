# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:16:49 2017

@author: Ionut
"""

import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()              # make a base for the app
# create labels


class LabelApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        
        tk.Label(self, text="This is my label").pack()
    
class GridApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        self.var1 = tk.IntVar()
        
        tk.Label(self, text="Name").pack()

        self.entry = tk.Entry(self, bg='white')
        self.entry.pack()

        tk.Label(self, text="Password").pack()

        self.secret_entry = tk.Entry(self, show='*', bg='white')
        self.secret_entry.pack()
        
        tk.Checkbutton(self, text='Keep me logged', variable=self.var1, command=self.checked).pack()

        tk.Button(self, text='OK', command=self.ok).pack()
    
    def checked(self):
        print('Keep me logged in has been checked')

    def ok(self):
        print('Text box: {}\nSecret box: {} \nKeep me Logged: {}'.format(self.entry.get(), self.secret_entry.get(), self.var1.get()))
        
        
class Voltron(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(padx=15, pady=15)
        self.master.title("Voltron")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#e6e6e6')

        frame1 = tk.Frame(self)
        frame1.grid(row=0, column=1, columnspan=2)

        LabelApp(frame1)

        frame2 = tk.Frame(self) 
        frame2.grid(row=1, column=0)

        GridApp(frame2)
        
if __name__ == '__main__':
#    root = tk.Tk()

    tk.Message(
        root, text='Close this window when you are done looking at the example pop-ups.'
    ).pack(
        anchor='center', padx=100, pady=100
    )

    top1 = tk.Toplevel(root)
    LabelApp(top1)

    top2 = tk.Toplevel(root)
    GridApp(top2)
    
    root.mainloop()