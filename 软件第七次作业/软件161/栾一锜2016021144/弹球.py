#-*-coding:cp936-*-
'''author:wudi
data:201811.1
func:������Ϸ����'''
from tkinter import*
import time
import random
#����С����
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()#�����߶�
        self.canvas_width=self.canvas.winfo_width()#�������
       
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=1
        if pos[3]>=self.canvas_height:self.y=-1
        if pos[0]<=0:self.x=1
        if pos[2]>=self.canvas_width:self.x=-1
class Ball3:
    def __init__(self,canvas,color):
        self.speed=random.randint(5,20)
        self.canvas=canvas
        self.id=canvas.create_oval(60,60,45,45,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=self.speed
        self.y=self.speed
        self.canvas_height=self.canvas.winfo_height()#�����߶�
        self.canvas_width=self.canvas.winfo_width()#�������
       
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=self.speed
        if pos[3]>=self.canvas_height:self.y=-1*self.speed
        if pos[0]<=0:self.x=self.speed
        if pos[2]>=self.canvas_width:self.x=-1*self.speed
class Ball2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(140,140,65,65,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()#�����߶�
        self.canvas_width=self.canvas.winfo_width()#�������
       
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=self.speed
        if pos[3]>=self.canvas_height:self.y=-1*self.speed
        if pos[0]<=0:self.x=self.speed
        if pos[2]>=self.canvas_width:self.x=-1*self.speed
#self.canvas.move(self.id,-5,-5)
        
tk=Tk()#ʵ����
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=800,height=800,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#С��ʵ����
ball1=Ball(canvas,'red')
ball2=Ball2(canvas,'blue')
ball3=Ball3(canvas,'pink')
while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


