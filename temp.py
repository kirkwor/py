# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:13:21 2017

@author: Ionut
"""
#============== CLASS TEST ====================================================
# myVar = 0
# def myFunc(param):
#     myVar = 1
#     return myVar
# #    print(myVar)
# #def myFunc():
# #    myVar = 1
# #myFunc(myVar) 
# myVar = myFunc(myVar)
# print(myVar)
#==============================================================================

#=============== AREA CALC ====================================================
import tkinter as tk
import math
 
def areacalc(event):
    numberB = float(inputNumber.get())
    numberC = float(inputNumber1.get())
    print(numberB, type(numberB))
    print(numberC, type(numberC))
    actualcalc = (numberB * numberC)
    result.configure(text="Area of a rectangle is: " +str(actualcalc))
    
root = tk.Tk()

lbl = tk.Label(root, text="Input your length:").pack()
inputNumber = tk.Entry(root)
inputNumber.bind("<Return>", areacalc)
inputNumber.pack()
 
lbl1 = tk.Label(root, text="Input your width:").pack()
inputNumber1 = tk.Entry(root)
inputNumber1.bind("<Return>", areacalc)
inputNumber1.pack()

result = tk.Label(lbl)
result.pack()
 
root.mainloop()
 
#==============================================================================
 
#==============================================================================
# import tkinter.messagebox
# # does not work without explicit import
# 
# # basic messagebox
# tkinter.messagebox.showinfo("WindTilte", message="this is some message")
# 
# # question to answer yes/no
# answer = tkinter.messagebox.askquestion("Question 1", "what do anser")
# if answer == "yes":
#     print("clicked yes")
# 
# # another type of message    
# ans2 = tkinter.messagebox.askyesnocancel('title', 'Triple question')
# print(ans2)
# 
# 
#==============================================================================
