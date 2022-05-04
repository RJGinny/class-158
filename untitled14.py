#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:27:04 2022

@author: riddhiekajain
"""

#bad Geometry error
from tkinter import *
root=Tk()
root.title("Geometry Error")
try:
    root.geometry("600")
except: 
    print("Bad geometry error, only one dimension passed in geometry instead of two")

root.mainloop()