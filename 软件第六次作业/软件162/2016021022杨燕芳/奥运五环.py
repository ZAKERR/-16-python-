# -*- coding:utf-8 -*-
'''
编写人： 杨燕芳
编写时间：20181020
功能：实现奥运五环
'''
import turtle #导入turtle模块

turtle.width(3)#笔的宽度

turtle.color("blue")#笔的颜色
turtle.circle(50)#画圆

turtle.penup()#抬笔，这样，路径就不会画出来
turtle.goto(120,0)#去坐标（120，0）
turtle.pendown()#下笔
turtle.color("black")
turtle.circle(50)

turtle.penup()
turtle.goto(240,0)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

turtle.penup()
turtle.goto(60,-50)
turtle.pendown()
turtle.color("yellow")
turtle.circle(50)

turtle.penup()
turtle.goto(180,-50)
turtle.pendown()
turtle.color("green")
turtle.circle(50)


turtle.color("black")
turtle.penup()
turtle.goto(-10,-80)
turtle.pendown()
turtle.write("奥运五环",font=("Aril",16,'bold'))

turtle.done()