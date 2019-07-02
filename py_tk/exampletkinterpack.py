##this is an example of tkinter's pack() method in python3
##in tkinter, pack() method is one of geometry manager
import tkinter as tk
root=tk.Tk();
frame=tk.Frame(root, bg="red",width=200,height=200);
frame.pack();
frame1=tk.Frame(root,bg="skyblue",width=100,height=100);
frame1.pack(expand=1);
frame2=tk.Frame(root,bg="yellow",width=200,height=200);
frame2.pack(fill="both");
frame3=tk.Frame(root,bg="blue",width=50,height=50);
frame3.pack(side="right");
root.mainloop();
