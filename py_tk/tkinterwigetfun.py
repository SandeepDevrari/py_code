##this is a program for making fun of tkinter wiget's
import tkinter as tk
from sys import exit
root=tk.Tk();
canvas=tk.Canvas(root,bg="black");
canvas.pack();
def exits():
    exit(1);
def hell():
    loot=tk.Tk();
    loot.geometry("150x50");
    vas=tk.Canvas(loot);
    vas.pack();
    ton=tk.Button(vas,text="DON'T!!!!",fg="black",bg="red",command=exits).pack();
    loot.mainloop();
bt1=tk.Button(canvas,bg="black",command=hell,text="Aqua",height=4,width=4,activebackground="aqua",activeforeground="white").grid(column=1,row=1);
bt2=tk.Button(canvas,bg="black",command=hell,text="Chartreuse",height=4,width=4,activebackground="chartreuse",activeforeground="white").grid(column=2,row=1);
bt3=tk.Button(canvas,bg="black",command=hell,text="Brown",height=4,width=4,activebackground="Brown",activeforeground="white").grid(column=3,row=1);
bt4=tk.Button(canvas,bg="black",command=hell,text="Crimson",height=4,width=4,activebackground="Crimson",activeforeground="white").grid(column=1,row=2);
bt5=tk.Button(canvas,bg="black",command=hell,text="Orange",height=4,width=4,activebackground="Orange",activeforeground="white").grid(column=2,row=2);
bt6=tk.Button(canvas,bg="black",command=hell,text="DeepPink",height=4,width=4,activebackground="DeepPink",activeforeground="white").grid(column=3,row=2);
bt7=tk.Button(canvas,bg="black",command=hell,text="Gold",height=4,width=4,activebackground="Gold",activeforeground="white").grid(column=1,row=3);
bt8=tk.Button(canvas,bg="black",command=hell,text="SeaGreen",height=4,width=4,activebackground="SeaGreen",activeforeground="white").grid(column=2,row=3);
bt9=tk.Button(canvas,bg="black",command=hell,text="Violet",height=4,width=4,activebackground="Violet",activeforeground="white").grid(column=3,row=3);
root.mainloop();
