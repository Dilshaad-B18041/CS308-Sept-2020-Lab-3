#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:05:04 2020

@author: mohib
"""

from tkinter import *
import os
import sentence
import token_code
import stats_code
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
var1=0
var2=0
var3=0
def browseFiles(state): 
    global var1,var2,var3
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    label_file_explorer.configure(text="File Opened: "+filename)
    
    newstr = os.getcwd()
    if(state=="select"):
        var1=1
        newstr="browsed_file.txt"
    elif(state=="neglect"):
        var2=1
        newstr="exclude_file.txt"
    elif(state=="extract"):
        var3=1
        newstr="extract_file.txt"

    f = open(newstr, 'w')
    f1 = open(filename, 'r')
    file = f1.readlines()
    type(file)
    for i in range(0, len(file)):
        f.write(file[i])
    f.close()
    #to make token_count.txt file 
    token_code.make_tokens(state)
    if(var1==1 and var2==1 and var3==1):
        fig = Figure(figsize=(150, 6), dpi=100)    
        plot1 = fig.add_subplot(111)
        stats_code.func(window, maxprint, minprint,sentprint,fig, plot1)
        sentence.line_wth_key()


window = Tk()

window.title("File Chooser")

window.geometry("1500x1500")

window.config(background = "white")



label_file_explorer = Label(window,  
                            text = "File Explorer", 
                            width = 100, height = 4,  
                            fg = "blue") 
   
       
button_explore = Button(window,  
                        text = "Choose Main Text File", 
                        command = lambda:browseFiles("select"))  

button_explore1 = Button(window,  
                        text = "Choose ignore text file", 
                        command = lambda:browseFiles("neglect"))
button_explore2 = Button(window,  
                        text = "Choose extract txt file", 
                        command = lambda:browseFiles("extract"))

   
#button_exit = Button(window,  
#                     text = "Exit", 
#                     command = exit)  

maxprint = Label(window,  
                            text = "Words occuring maximum times will be shown here", 
                              
                            fg = "blue") 

minprint = Label(window,  
                            text = "Words occuring minimum times will be shown here", 
                              
                            fg = "red")


sentprint = Label(window,  
                            text = "number of sentences will be shown here", 
                              
                            fg = "black")

 

#plot_button = Button(master = window,  
#                     command = faltu.func(window, maxprint, minprint), 
#                     height = 2,  
#                     width = 10, 
#                     text = "Plot") 
  
# place the button  
# in main window 
#plot_button.pack() 
button_explore.pack()
button_explore1.pack()
button_explore2.pack()
label_file_explorer.pack()
maxprint.pack()
minprint.pack()
sentprint.pack()
#button_show = Button(window, text = "show label", command = faltu.func(window)) 
   
# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns 
#label_file_explorer.grid(column = 1, row = 1) 
   
#button_explore.grid(column = 1, row = 2) 
   
#button_exit.grid(column = 1,row = 3) 

#button_show.grid(column = 1, row = 5)

   
# Let the window wait for any events 
window.mainloop() 
