##this is a program for python3's tkinter wigets
##here i'm only implementing tkinter.ttk's wigets
from tkinter import *
from tkinter.ttk import *
root=ttk.Tk();
frame=ttk.Frame(root,background="red",bd=3,cursor="arrow",height=200,width=200,highlightcolor="green");
frame.pack();
lable1=ttk.Lable(frame,
