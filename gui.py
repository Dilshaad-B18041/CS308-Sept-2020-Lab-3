#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:05:04 2020

@author: mohib
"""

from tkinter import *
import os
from tkinter import filedialog

def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename)
    
    newstr = os.getcwd()
    newstr+="/word_in_sep_line.txt"
    
    f = open(newstr, 'w')
    f1 = open(filename, 'r')
    file = f1.readlines()
    type(file)
    for i in range(0, len(file)):
        f.write(file[i])
    f.close()
    
window = Tk()

window.title("File Chooser")

window.geometry("500x500")

window.config(background = "white")

label_file_explorer = Label(window,  
                            text = "File Explorer", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Choose Files", 
                        command = browseFiles)  
   
button_exit = Button(window,  
                     text = "Exit", 
                     command = exit)  

 
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
label_file_explorer.grid(column = 1, row = 1) 
   
button_explore.grid(column = 1, row = 2) 
   
button_exit.grid(column = 1,row = 3) 


   
# Let the window wait for any events 
window.mainloop() 