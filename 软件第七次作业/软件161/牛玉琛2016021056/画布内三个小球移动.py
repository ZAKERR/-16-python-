#多个小球在画布中移动
from tkinter import *
import random
import time
class Ball:
    def __init__(self,canvas,color,sx,sy):
        self.canvas = canvas
        self.id=canvas.create_oval(20,20,55,55,fill=color)
        self.canvas.move(self.id,sx,sy)
        starts=[-3,-2,-1,1,2,3]#移动速度
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:self.x=1
        if pos[1]<=0:self.y=1
        if pos[2]>=self.canvas_width:self.x=-1
        if pos[3]>=self.canvas_height:self.y=-1
    def set_oval(self,canvas,color,x1,y1,x2,y2):
        self.id=canvas.create_oval(x1,y1,x2,y2,fill=color)

tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",-1)
canvas=Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)#生成画布
canvas.pack()
tk.update()

ball=Ball(canvas,'blue',300,350)

ball2=Ball(canvas,'green',300,600)
ball2.set_oval(canvas,'green',30,30,60,60)

ball3=Ball(canvas,'red',400,600)
ball3.set_oval(canvas,'red',30,20,60,80)

while True:
    ball.draw()
    ball2.draw()
    ball3.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)








    
