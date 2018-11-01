func="生成游戏窗口"
from tkinter import *
import time
import random
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 30, 25, fill=color)
        self.canvas.move(self.id, 400, 300)
        starts=[-3,-2,-1,1,2,3]#小球随机出现
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)# 小球移动到x,y的位置上
        pos=self.canvas.coords(self.id)#获得小球的坐标系
        if pos[1]<=0:self.y=1         #超出顶向下走
        if pos[3]>=self.canvas_height:self.y=-1#超出底向下走
        if pos[0]<=0:self.x=1         #超出左边框向右走
        if pos[2]>=self.canvas_height:self.x=-1#超出右边框

tk=Tk()
tk.title("game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#小球实例化
ball=Ball(canvas,'red')
ball1=Ball(canvas,'yellow')
ball2=Ball(canvas,'blue')
while True:
    ball.draw()
    ball1.draw()
    ball2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

