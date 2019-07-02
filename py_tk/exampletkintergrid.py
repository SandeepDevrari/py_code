##this is an example of tkinter's grid() method in python3
##tkinter's grid() method is a geometry manager
import tkinter as tk
root=tk.Tk()
frame=tk.Frame(root,bg="green",width=200,height=200,bd=2,relief="solid");
frame.grid(column=2,columnspan=2,row=2,rowspan=3,ipadx=5,ipady=5,padx=4,pady=4);
root.mainloop();
