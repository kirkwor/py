# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:19:07 2017

@author: Ionut
"""
count = 0

import tkinter as tk

root = tk.Tk() 

import tkinter.messagebox
# does not work without explicit import

# basic messagebox
tkinter.messagebox.showinfo("Python Quiz", message="Welcome to your Python Journey")

answer = tkinter.messagebox.askquestion("Question 1", "Is print a command?")
if answer == "yes":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 2", "Is while an example of iteration?")
if answer == "yes":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 3","Are there more than 33 commands in python?")
if answer == "no":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 4","Do you need to assign variable types?")
if answer == "no":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 5","Can == be used to compare a variable to a string")
if answer == "yes":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 6","Does != mean that an integer is equal to a string?")
if answer == "no":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 7","Is there a variation between Python2 and Python3?")
if answer == "yes":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 8","Can you use () for a list?")
if answer == "no":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 9","Do you start counting at 1?")
if answer == "no":
    print("correct")
    count = count + 1
else:
    print("unlucky")


answer = tkinter.messagebox.askquestion("Question 10","Do you love Python3?")
if answer == "yes":
    print("correct")
    count = count + 1
else:
    print("unlucky")
print("Your final score is ", + count)

if count >= 9:
    print("You are a Python Master!")

    photo = tk.PhotoImage(file='congratulations.png')
    lbl = tk.Label(root, image=photo)
    lbl.pack()
    
    canvas = tk.Canvas(root, width=450, height=200, bg="white")
    canvas.create_text(225,100,fill="darkblue",font="Tahoma 20 bold", text=(count))
    canvas.pack()
    
    def printName(): print('File has been printed')   
    btn1 = tk.Button(root, text="Print result", command=printName).pack()
    
    if __name__ == '__main__':
        root.mainloop()         
else:
    print("Revise! Read! Work Harder!..... Or Else")
    photo = tk.PhotoImage(file='nexttime.png')
    lbl = tk.Label(root, image=photo)
    lbl.pack()
    
    canvas = tk.Canvas(root, width=450, height=200, bg="white")
    canvas.create_text(225,100,fill="darkblue",font="Tahoma 20 bold", text="Work harder!")
    canvas.pack()
    
    def printName(): print('Test completed')   
    btn1 = tk.Button(root, text="Good bye!", command=printName).pack()
    
if __name__ == '__main__':
    root.mainloop()         