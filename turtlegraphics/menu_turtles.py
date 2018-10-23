from turtle import *
import tkinter as tk
import turtle
from random import randint

def setgraph():
    import graph_em

    #*************************************************************************
def setrings2():
    t = Turtle()
    t.color("#1A1A1A")
    t.pensize(10)
    t.speed(1)


    t.setposition(0,0)
    t.circle(50)

    t.penup()
    t.setposition(-110, 0)
    t.pendown()
    t.color("#0000FF")
    t.circle(50)

    t.penup()
    t.setposition(60, -60)
    t.pendown()
    t.color("#06FC24")
    t.circle(50)

    t.penup()
    t.setposition(-60, -60)
    t.pendown()
    t.color("#F5FF00")
    t.circle(50)

    t.penup()
    t.setposition(110, 0)
    t.pendown()
    t.color("#FF0000")
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
d = tk.Button(root, text="Braeden Rings",font=('courier', '20') ,command=setrings2)
t1 = tk.Label(root, text="Rings (Olympic Rings) : SKW",font=('courier', '10'))
t2 = tk.Label(root, text="Rings #2 (More Olympic Rings): BAF",font=('courier', '10'))
t3 = tk.Label(root, text="Rings #3 (Even More Olympic Rings): BAF",font=('courier', '10'))
t4 = tk.Label(root, text="Rings #4 (More More Olympic Rings): BAF",font=('courier', '10'))
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
