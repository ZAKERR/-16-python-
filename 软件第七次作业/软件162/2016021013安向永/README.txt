请上传代码和截图!
#-*-coding:utf-8-*-
#···
#编写人：安向永
#编写时间：20181102
#功能：实现小球游戏
#注意中文的字符输入除了utf8之外，还得在中文前加上u

import time
import random
from tkinter import *

class Ball():
    def __init__(self,canvas,color,a,b,c,d,e,f):
        self.canvas=canvas
        self.id=canvas.create_oval(a,b,c,d,fill=color)
        self.canvas.move(self.id,e,f)
       
        
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]

        self.y=starts[1]

        
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
       

        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)#获取坐标系
        if pos[1]<=0:self.y=1
        if pos[3]>=self.canvas_height:self.y=-1
        if pos[0]<=0:self.x=1
        if pos[2]>=self.canvas_width:self.x=-1




tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=600,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()   #刷新



#实例化
ball=Ball(canvas,'cyan',10,10,30,30,300,300)
ball2=Ball(canvas,'yellow',15,20,45,45,100,100)
ball3=Ball(canvas,'blue',30,35,55,55,450,450)

while True:
    ball.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)  #刷新窗体


