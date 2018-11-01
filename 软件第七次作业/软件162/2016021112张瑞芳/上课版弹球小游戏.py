#_*_ coding:cp936 _*_
#author:张瑞芳
#date:20181101
#多球乱撞
func:"生成游戏背景窗体"
from tkinter import *
import time
import random
#生成小球类

class Ball:
    def __init__(self,canvas,color):
       self.canvas=canvas
       #控制球的大小 或者形状
       #self.id=canvas.create_oval(10,10,50,50,fill=color)
       ad=[(10,10,50,50),(20,20,35,35),(30,30,90,90)]
       random.shuffle(ad)
       self.id=canvas.create_oval(ad[0],fill=color)
       #改变球的初始位置
       a=random.randint(0,self.canvas.winfo_height())
       b=random.randint(0,self.canvas.winfo_width())
       self.canvas.move(self.id,a,b)
       starts=[-3,-2,-1,1,2,3]
       random.shuffle(starts)#shuffle：打乱数组的顺序
       self.x=starts[0]
       self.y=starts[1]
       self.canvas_height=self.canvas.winfo_height()#获取画布的高度
       self.canvas_width=self.canvas.winfo_width()#获取画布的宽度
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)#控制小球移动
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3#判断碰到上下边框即回弹
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0: #来判断球是不是碰到了左右边框
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
#生成界面
tk=Tk()
tk.title("game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=1000,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#小球实例化
ball1=Ball(canvas,'green')
ball2=Ball(canvas,'red')
ball3=Ball(canvas,'blue')
#刷新画布
while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()#不停的刷新画布
    tk.update()
    time.sleep(0.001)
