#import turtle
#t=turtle.Pen()
'''

#t.circle(50,steps=4)
t.speed(5)
turtle.goto(0,0)
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.home()
turtle.circle(50,270)
'''
'''
import turtle
t=turtle.Pen()
t.speed(1000)
for x in range(1000):
    t.circle(x)
    t.left(91)

'''
'''
for x in range(1,19):
    t.forward(100)
    if x%2==0:
        t.left(175)
    else:
        t.left(225)



'''

import turtle
p = turtle
turtle.bgcolor("purple")
color=["red","yellow","green","blue","black"]
a=[60,120,90,30,0]
b=[0,0,-30,-30,0]
for i in range(5):
    p.pensize(3)
    p.color(color[i])
    p.circle(30,360)
    p.pu()
    p.goto(a[i],b[i])
    p.pd()
turtle.done()

