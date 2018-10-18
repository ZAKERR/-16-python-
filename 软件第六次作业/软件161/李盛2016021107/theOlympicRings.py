#!/usr/bin/python
# -*-coding:utf-8-*-
'''
编写人：李盛
编写时间：2018.09.27
功能：奥运五环
'''

import turtle as t  # 导入turtle模块
t.speed(0)
colors = ["blue", "black", "red", "green", "yellow"]
pos_x = [-110, 0, 110, 55, -55]
pos_y = [-25, -25, -25, -75, -75]


def circle_fif(x):
    t.pensize(10)
    t.color(colors[x])  # 定义颜色
    t.penup()  # penup和pendown()设置画笔抬起或放下时是否绘制直线
    t.goto(pos_x[x], pos_y[x])
    t.pendown()
    t.circle(45)  # 绘制圆的半径


for i in range(5):
    circle_fif(i)
t.done()