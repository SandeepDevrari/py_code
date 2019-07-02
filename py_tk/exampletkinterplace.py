##this an example of tkinter's place() method
##tkinter's place() method is a geometry manager
import tkinter as tk
root=tk.Tk();
frame=tk.Frame(root,bg="red",width=100,height=100);
frame.place(height=100,width=100,x=50,y=30);
root.mainloop();
