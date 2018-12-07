# plot-dictionary.py skw
import tkinter as tk
import turtle

def main():
    #table is a dictionary
    table = {-100:0,-90:-20,-80:-40,-70:-60,-60:-80,-50:-100,
                -40:-120,-30:-140,-20:-160,-10:-180,-0:-200,
                    10:-180,20:-160,30:-140,40:-120,50:-100,
                    60:-80,70:-60,80:-40,90:-20,100:0
            }
    print(" KEYS ")
    print(table.keys())
    print(" VALUES ")
    print(table.values())
    #turtle graphics
    twin = turtle.Screen()
    twin.clear()
    t = turtle.Turtle()
    #tWin = turtle.sreen()
    for h,k in table.items(): #get items in the dictionary
        print(h, k) # trace code
        #x,y = tables[n]
        t.penup()
        t.goto(h,k)
        t.pendown()
        t.circle(5)
    twin.exitonclick()

main()

"""
this code uses a dictionary with keys ranging from
-100 to 100 incrementing by 10.
each key has a value of 0 as an integer
To retrieve the values in the dictionary "table" a for loop is used.
the x cooridate on a python turtle screen corresponds to the h while
the y value  cooresponds to k.
***************************************************
for h,k in table.items(): #get the items in the dictionary
        print(h, k) #trace code
h and k are in ploted using
    t.goto(h,k)
    t.pendown()
    t.circle(5)
*** YOUR TASK ***
change all values (not keys) from 0 to another integer
Try to make something groovey
"""
