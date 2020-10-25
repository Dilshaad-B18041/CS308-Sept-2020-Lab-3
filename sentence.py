from tkinter import *
import tkinter
from tkinter import filedialog

import os
import sys



def line_wth_key():
    root = Tk()
    root.title("Sentence Extracted")
    f=open(os.path.join(sys.path[0], 'browsed_file.txt'),'r')
    f=f.read().split('.')
    f1=open(os.path.join(sys.path[0], 'extract_file.txt'),'r')
    f1=f1.read().split("\n")
    f1.remove("")
    ans = []
    for i in f1:
        for j in f:
            if i in j:
                ans.append(j+".")
    for item in ans:
        w = Label(root, text=item)
        w.pack()
    root.mainloop()

