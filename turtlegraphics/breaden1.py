#https://www.geeksforgeeks.org/turtle-programming-python/
from turtle import * #Inside_Out
t = turtle()
t.color("#1A1A1A")
t.pensize(10)
t.speed(1)


turtle.setposition(0,0)
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
