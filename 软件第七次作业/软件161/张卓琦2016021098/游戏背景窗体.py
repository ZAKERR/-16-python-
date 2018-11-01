#生成游戏背景窗体
from tkinter import *
import time
import random
#生成小球类
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        ad = [(30,30,55,55),(50,50,100,100),(45,45,75,75)]
        random.shuffle(ad)
        self.id=canvas.create_oval(ad[0],fill=color)#椭圆型球,数字控制形状（10，10是位置25，25控制球大小
        sitea = [245,100,300,252]
        random.shuffle(sitea)
        self.canvas.move(self.id,sitea[0],sitea[1])#小球移动一个点
        #让小球随机运动
        starts=[-3,-2,-1,1,2,3]#让小球从中随机挑选一个速度
        random.shuffle(starts)#shuffle： 打乱顺序功能
        self.x = starts[0]
        self.y = starts[1]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)#获取位置
        if pos[1]<=0:self.y = 1
        if pos[3]>=self.canvas_height:self.y = -1#如果小球到达最顶端或者最下端往回走
        if pos[0]<=0:self.x = 1
        if pos[2]>=self.canvas_width:self.x = -1
tk = Tk() 
tk.title("BallGame")
tk.resizable(1,1)#是否可以随意改变窗体大小 0，0时候不可以
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 800,height = 600,bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()
#小球实例化
ball1 = Ball(canvas,'red')
ball2 = Ball(canvas,'yellow')
ball3 = Ball(canvas,'blue')
while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()#刷新
    tk.update()
    time.sleep(0.01)
