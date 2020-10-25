from tkinter import *
import tkinter
from tkinter import filedialog

import os
import sys

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def line_wth_key():
    root = Tk()
    f=open(os.path.join(sys.path[0], 'word_in_sep_line.txt'),'r')
    f=f.read().split('.')
    f1=open(os.path.join(sys.path[0], 'keywords.txt'),'r')
    f1=f1.read().split("\n")
    f1.remove("")
    ans = []
    for i in f1:
        for j in f:
            if i in j:
                ans.append(j)
    for item in ans:
        w = Label(root, text=item)
        w.pack()
line_wth_key()
