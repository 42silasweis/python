from turtle import *
import tkinter as tk
import turtle
from random import randint
    #*************************************************************************
#Inside_Out
# new.py DDG
def setgabe():

    w = turtle.Screen()
    w.bgcolor("#7F7F7F")
    t = turtle.Turtle()
    def helloWorld():
    	t.color("#A52A2F")
    	t.speed(1)
    	t.width(9)

    	t.penup()
    	t.setposition(-112,90)
    	t.pendown()
    	t.setposition(-112,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-112,45)
    	t.pendown()
    	t.setposition(-67,45)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-67,90)
    	t.pendown()
    	t.setposition(-67,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-52,90)
    	t.pendown()
    	t.setposition(-52,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-52,45)
    	t.pendown()
    	t.setposition(-17,45)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-52,90)
    	t.pendown()
    	t.setposition(-7,90)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-52,0)
    	t.pendown()
    	t.setposition(-7,0)
    	t.penup()
    	t.color("#A52A2F")


    	t.setposition(7,90)
    	t.pendown()
    	t.setposition(7,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(7,0)
    	t.pendown()
    	t.setposition(52,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(67,90)
    	t.pendown()
    	t.setposition(67,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(67,0)
    	t.pendown()
    	t.setposition(112,0)
    	t.penup()
    	t.color("#A52A2F")

    	t.pendown()
    	t.circle(45)

    	t.penup()
    	t.setposition(-157,-15)
    	t.pendown()
    	t.setposition(-142,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-142,-105)
    	t.pendown()
    	t.setposition(-127,-15)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-127,-15)
    	t.pendown()
    	t.setposition(-112,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-112,-105)
    	t.pendown()
    	t.setposition(-97,-15)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-59.5,-105)
    	t.pendown()
    	t.circle(45)

    	t.penup()
    	t.setposition(-22,-15)
    	t.pendown()
    	t.setposition(-22,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-22,-60)
    	t.pendown()
    	t.setposition(22,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(-22,-60)
    	t.pendown()
    	t.circle(22.5,180)

    	t.penup()
    	t.setposition(37,-15)
    	t.pendown()
    	t.setposition(37,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(37,-105)
    	t.pendown()
    	t.setposition(82,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(97,-15)
    	t.pendown()
    	t.setposition(97,-105)
    	t.penup()
    	t.color("#A52A2F")

    	t.setposition(97,-105)
    	t.pendown()
    	t.left(180)
    	t.circle(45,180)
    	t.penup()

    helloWorld()
    holdit = input();

    #*************************************************************************
def setgraph():
    import graph_em

    #*************************************************************************
def setrings2():
    bgcolor("#8e8e8e")
    t = turtle.Turtle()
    t.color("#ff8a00")
    t.pensize(10)
    t.speed(1)


    turtle.setposition(0,0)
    t.circle(50)

    t.penup()
    t.setposition(-110, 0)
    t.pendown()
    t.color("#000000")
    t.circle(50)

    t.penup()
    t.setposition(60, -60)
    t.pendown()
    t.color("#000000")
    t.circle(50)

    t.penup()
    t.setposition(-60, -60)
    dec = 0;
    t.pendown()
    t.color("#ff8a00")
    t.circle(50)

    t.penup()
    t.setposition(110, 0)
    t.pendown()
    t.color("#000000")
    t.circle(50)


    holdit = input();
    #**************************************************************************
    #Silas's Rings
def thepoly(turtle,turtle2,turtle3,turtle4,turtle5,size):
	for i in range(2):

		turtle.speed(3)
		turtle.circle(60)
		turtle.pensize(6)
		turtle2.speed(3)
		turtle2.circle(60)
		turtle2.pensize(6)
		turtle3.speed(3)
		turtle3.circle(60)
		turtle3.pensize(6)
		turtle4.speed(3)
		turtle4.circle(60)
		turtle4.pensize(6)
		turtle5.speed(3)
		turtle5.circle(60)
		turtle5.pensize(6)

def setrings():
    # *************************************************************************
    # myturtle4.py sila

    bgcolor("gray")
    turtle = Turtle()
    turtle.pencolor("blue")

    turtle2 = Turtle()
    turtle2.pencolor("red")

    turtle3 = Turtle()
    turtle3.pencolor("green")

    turtle4 = Turtle()
    turtle4.pencolor("yellow")

    turtle5 = Turtle()
    turtle5.pencolor("black")


    turtle.penup()
    x = -125
    y = 0
    turtle.setpos(x, y)
    turtle.pendown()

    turtle2.penup()
    x = 125
    y = 0
    turtle2.setpos(x, y)
    turtle2.pendown()

    turtle3.penup()
    x = 65
    y = -80
    turtle3.setpos(x, y)
    turtle3.pendown()

    turtle4.penup()
    x = -65
    y = -80
    turtle4.setpos(x, y)
    turtle4.pendown()
    thepoly(turtle,turtle2,turtle3,turtle4,turtle5,20)



# *************************************************************************
#main tk (the menu starts below)
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("MENU - SKW PYTHON PRESENTATION")
root.minsize(400, 200)
a = tk.Button(root, text="Silas Rings",font=('courier', '20') ,command=setrings)
b = tk.Button(root, text="Braeden Rings",font=('courier', '20') ,command=setrings2)
c = tk.Button(root, text="Erduin Graph",font=('courier', '20') ,command=setgraph)
d = tk.Button(root, text="Gabes New Turtle",font=('courier', '20') ,command=setgabe)
t1 = tk.Label(root, text="Rings (Olympic Rings) : SKW",font=('courier', '10'))
t2 = tk.Label(root, text="Rings #2 (Even More Olympic Rings): BAF",font=('courier', '10'))
t3 = tk.Label(root, text="Rings #3 (Erduin's Graph): BAF",font=('courier', '10'))
t4 = tk.Label(root, text="Rings #4 (Gabes New Graphics): BAF",font=('courier', '10'))
t5 = tk.Label(root, text = "SOAR (Stack of Activation Records)",font=('courier', '10'))
a.pack()
b.pack()
c.pack()
d.pack()
t1.pack()
t2.pack()
t3.pack()
t4.pack()
t5.pack()
root.mainloop()

"""
This menu needs a lot of workself.
"""
