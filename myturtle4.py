# ex4b.py skw
from turtle import *
space = Screen() 

bgcolor("white")
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

def thepoly(size):
	for i in range(50):
		
		turtle.speed(10)
		turtle.circle(60)
		turtle.pensize(6)
		turtle2.speed(10)
		turtle2.circle(60)
		turtle2.pensize(6)
		turtle3.speed(10)
		turtle3.circle(60)
		turtle3.pensize(6)
		turtle4.speed(10)
		turtle4.circle(60)
		turtle4.pensize(6)
		turtle5.speed(10)
		turtle5.circle(60)
		turtle5.pensize(6)




thepoly(10)


#mainloop()
holdit = input();

