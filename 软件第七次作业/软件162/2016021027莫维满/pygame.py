#-*-coding:utf-8-*-
'''author:moweiman
date:201602128
func：生成游戏窗体 '''
from tkinter import *
import time
import random

#生成小球类
class Ball:
    def __init__(self,canvas,color,b,l):

        self.canvas = canvas
        self.b = b
        self.l =l
        #球大小
        self.id=canvas.create_oval(10,10,b,b,fill=color)
        #坐标（起始位置）
        self.canvas.move(self.id,250,l)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()


    def draw(self):
        #小球移动
        #self.canvas.move(self.id,0,-1)
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0 : self.y= 1
        if pos[3] >=self.canvas_height:self.y =-1

        if pos[0] <= 0 : self.x= 1
        if pos[2] >=self.canvas_width:self.x =-1



    
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

#小球实例化
ball=Ball(canvas,'red',30,100)
ballt=Ball(canvas,'green',40,200)
ballfi=Ball(canvas,'blue',50,300)

while True:
    ball.draw()
    
    ballt.draw()
    
    ballfi.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
