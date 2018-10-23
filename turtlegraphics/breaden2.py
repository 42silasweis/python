#https://www.geeksforgeeks.org/turtle-programming-python/
from turtle import *
import turtle #Inside_Out
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
