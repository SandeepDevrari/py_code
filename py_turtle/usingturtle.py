##this is the program of drawing a smiley with the help of turtle
import turtle as t
class smiley:
    def __init__(self):
        t.setup(500,500);
        t.screensize(100,100);
        t.setworldcoordinates(0,-50,100,50);
        t.bgcolor("skyblue");
        t.penup();
        t.setpos(60,0);
        t.left(90);
        t.pensize(5);
        t.pendown();
        t.pencolor("black");
        t.fillcolor("white");
        t.begin_fill();
        t.circle(10,360);
        t.end_fill();
        t.penup();
        t.setpos(56,3)
        t.pendown();
        t.pensize(1);
        t.fillcolor("black");
        t.begin_fill();
        t.circle(1,360);
        t.end_fill();
        t.penup();
        t.setpos(44,3);
        t.left(180);
        t.pendown();
        t.begin_fill();
        t.circle(1,360);
        t.end_fill();
        t.penup();
        t.pensize(5);
        t.setpos(50,3);
        t.pendown();
        t.forward(3);
        t.penup();
        t.setpos(53,-3);
        t.right(90);
        t.pendown();
        t.forward(6);
        t.penup();
        t.setpos(50,-10);
        t.left(90);
        ##t.pensize(5);
        t.pendown();
        t.forward(10);
        t.penup();
        t.setpos(67.07,-12.93);
        t.right(45);
        t.pendown();
        t.forward(10);
        t.right(45);
        t.forward(20);
        t.right(45);
        t.forward(10);
        t.penup();
        t.setpos(50,-20);
        t.left(135);
        t.pendown();
        t.forward(10);
        t.penup();
        t.setpos(47.07,-37.07);
        t.right(135);
        t.pendown();
        t.forward(10);
        t.right(135);
        t.forward(20);
        t.right(135);
        t.forward(10);
        t.penup();
        t.hideturtle();
        t.onscreenclick(None);
        t.mainloop();
obj1=smiley();