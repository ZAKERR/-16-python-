#作者:安小飞
#时间:20181101
#功能:
from tkinter import *
import random
import time
class Ball():
    def __init__(self,canvas,color,l_x,l_y):
        self.canvas=canvas
        self.id = canvas.create_oval(20,20,55,55,fill=color)#圆形小球
        self.canvas.move(self.id,l_x,l_y)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
       
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:self.x=1
        if pos[1]<=0:self.y=1
        if pos[2]>=self.canvas_width:self.x=-1
        if pos[3]>=self.canvas_height:self.y=-1

    def set_oval(self,canvas,color,x0,y0,x2,y2):
        self.id = canvas.create_oval(x0,y0,x2,y2,fill=color)#圆形小球
tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)#画布
canvas.pack()
tk.update()

ballone = Ball(canvas,'blue',745,550)

balltwo = Ball(canvas,'red',400,600)
balltwo.set_oval(canvas,'red',20,20,100,55)

balltt = Ball(canvas,'green',300,600)
balltt.set_oval(canvas,'green',30,20,10,10)

while True:
    ballone.draw()
    balltwo.draw()
    balltt.draw()
    
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)