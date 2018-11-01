"""
作者：李
时间：2018.11.01
功能：生成游戏背景窗体

"""
import time
import random
from tkinter import *
#生成小球类
class Ball:
    def __init__(self,canvas,color):

        self.canvas=canvas
        self.id=canvas.create_oval(20,20,35,35,fill=color) #在画布上画出一个球
        self.canvas.move(self.id,245,100)  #球的初始位置
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)

        self.x=starts[0]
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()   #获取画布当前高度
        self.canvas_width = self.canvas.winfo_width()   #获取画布当前宽度
    def draw(self):              #球移动
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)   #coords返回画布上画好的x和y坐标
        # 判断小球是否撞到画布顶部或者底部，保证小球反弹回去，不消失
        if pos[1]<=0:self.y=3
        if pos[3]>=self.canvas_height:self.y=-3
        if pos[0]<=0:self.x=3
        if pos[2] >= self.canvas_width: self.x= -3

        #self.canvas.move(self.id,-1,0)

tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#小球实例化
ball1=Ball(canvas,'black')
ball2=Ball(canvas,'red')
ball3=Ball(canvas,'blue')


while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)