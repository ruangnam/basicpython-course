import turtle
import math
tao = turtle.Pen()
tao.shape('turtle')
pi = math.pi
x = 100*pi/12
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    
def gleeb():
    for i in range(12):
        if i == 0:
             tao.fillcolor('orange')
        elif i == 1:
             tao.fillcolor('orangered')
        elif i == 2:
             tao.fillcolor('hotpink')
        elif i == 3:
             tao.fillcolor('blueviolet')
        elif i == 4:
             tao.fillcolor('blue4')
        elif i == 5:
             tao.fillcolor('blue')
        elif i == 6:
             tao.fillcolor('dodgerblue2')
        elif i == 7:
             tao.fillcolor('green')
        elif i == 8:
             tao.fillcolor('green3')
        elif i == 9:
             tao.fillcolor('greenyellow')
        elif i == 10:
             tao.fillcolor('khaki')
        else:
             tao.fillcolor('yellow')
    
        tao.lt(30)
        tao.begin_fill()
        tao.rt(15)
        tao.fd(100)
        tao.lt(15)
        tao.circle(x,180)
        tao.lt(15)
        tao.fd(100)
        tao.lt(180-15)
        tao.end_fill()
        
def cen():
    tao.penup()
    tao.fd(50)
    tao.lt(90)
    tao.pendown()
    tao.fillcolor('cornsilk')
    tao.begin_fill()
    tao.circle(50)
    tao.end_fill()
    tao.lt(90)
    tao.penup()
    tao.goto(0,0)
    tao.pendown()

def mouth():
    tao.fillcolor('red')
    tao.begin_fill()
    tao.lt(90)
    tao.fd(35)
    tao.lt(90)
    tao.circle(35,180)
    tao.goto(0,0)
    tao.end_fill()

def eye():
    tao.penup()
    tao.goto(25,25)
    tao.pendown()
    tao.fillcolor('black')
    tao.begin_fill()
    tao.circle(5)
    tao.end_fill()
    tao.fillcolor('white')
    tao.begin_fill()
    tao.circle(2)
    tao.end_fill()
    tao.penup()
    tao.goto(0,0)
    tao.goto(-25,25)
    tao.lt(180)
    tao.pendown()
    tao.fillcolor('black')
    tao.begin_fill()
    tao.circle(5)
    tao.end_fill()
    tao.fillcolor('white')
    tao.begin_fill()
    tao.circle(2)
    tao.end_fill()
    tao.penup()
    
gleeb()
tao.rt(90)
cen()
mouth()
eye()
tao.goto(200,200)

