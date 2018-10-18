'''
功能：用函数实现画奥运五环
作者：牛玉琛
日期：2018.10.18

'''

import turtle
def huayuan(s,x,y):
    turtle.speed(10)
    turtle.pencolor(s)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(45)

colors=['blue','black','red','yellow','green']
x=[-110,0,110,-55,55]
y=[-25,-25,-25,-75,-75]
for i in range(5):
    huayuan(colors[i],x[i],y[i])
