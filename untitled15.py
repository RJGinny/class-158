#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:43:30 2022

@author: riddhiekajain
"""

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Addition")
root.geometry("600x600")
input_box = Entry(root)
input_box.pack()
def addition():
    number = 5
    get_input = input_box.get()
    
    try:
       print(number = get_input)
    except(TypeError):
        messagebox.showinfo("Error", "Cannot add two different data types: integers and string" )
    
button = Button(root, text= "addition", command = addition)
button.pack()
root.mainloop()