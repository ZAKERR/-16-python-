#!/usr/bin/python
#-*-coding:utf-8-*-
#编写人：单明亮
#编写时间：20181101
#功能：弹球游戏
from tkinter import *
import time
import random
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=3
        if pos[3]>=self.canvas_height:self.y=-3
        if pos[0]<=0:self.x=3
        if pos[2]>=self.canvas_width:self.x=-3
class Ball1(Ball):
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(20,20,35,35,fill=color)
        self.canvas.move(self.id,120,80)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=3
        if pos[3]>=self.canvas_height:self.y=-3
        if pos[0]<=0:self.x=3
        if pos[2]>=self.canvas_width:self.x=-3
class Ball2(Ball):
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(30,30,45,45,fill=color)
        self.canvas.move(self.id,150,130)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=3
        if pos[3]>=self.canvas_height:self.y=-3
        if pos[0]<=0:self.x=3
        if pos[2]>=self.canvas_width:self.x=-3

tk=Tk()
tk.title("ballgame")
tk.resizable(10,10)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
ball=Ball(canvas,'blue')
ball1=Ball1(canvas,'red')
ball2=Ball2(canvas,'yellow')
while True:
    ball.draw()
    ball1.draw()
    ball2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


