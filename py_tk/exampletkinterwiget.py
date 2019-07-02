##this is the program for implementing tkinter's wigets
import tkinter as tk;
root=tk.Tk();
canvas1=tk.Canvas(root,bg="gold");
##coordinates=10,20,30,40;
##arc=canvas.create_arc(coordinates,start=0,extent=120,fill="green");
##oval=canvas.create_polygon(30,40,40,50,50,60);
canvas1.pack();
frame=tk.Frame(canvas1,bg="red",height=100,width=100);
frame.pack();
label1=tk.Label(frame,bg="skyblue",bd=2,fg="white",height=2,width=10,text="hello this is the first lable");
label1.grid();
def call():
    print("hello beta!!");

button1=tk.Button(frame,activebackground="blue",activeforeground="white",bg="black",height=2,width=3,command=call,text="click me");
#def call():
#    print("hello beta!!");
button1.grid(row=3);
canvas=tk.Canvas(bg="gold",height=200,width=200);
coordinates=10,20,130,140;
arc=canvas.create_arc(coordinates,start=0,extent=120,fill="green");
oval=canvas.create_polygon(30,40,40,50,50,60,fill="red");
canvas.pack();
chkbox=tk.Checkbutton(canvas,activebackground="red",fg="skyblue",text="Human");
chkbox.pack();
entry1=tk.Entry(label1,bg="red",bd=3);
entry1.pack();
list1=tk.Listbox(root);
list1.insert(1,"hell");
list1.insert(2,"you");
list1.pack();
tk.mainloop();
