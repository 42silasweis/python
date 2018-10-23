import turtle  #Inside_Out
ts = turtle.Screen()
ts.setup(1000,800)
t = turtle.Turtle()
ts.bgcolor("white")
t = turtle.Turtle()

def drawgraph(t):
	t.color("#1A1A1A")
	t.pensize(2)
	t.speed(0)
	turtle.setposition(0, 1000)
	turtle.setposition(0, -1000)
	turtle.setposition(0, 0)
	turtle.setposition(1000, 0)
	turtle.setposition(-1000, 0)
	
	y = 0
	for x in range (-1000,1000,100):
		t.pensize(5)
		t.penup()
		t.setposition(x, y)
		t.dot(5)
		t.pendown()
	x = 0
	for y in range (-1000,1000,100):
		t.pensize(5)
		t.penup()
		t.setposition(x, y)
		t.dot(5)
		t.pendown()
		

drawgraph(t)
holdit = input ("*")
