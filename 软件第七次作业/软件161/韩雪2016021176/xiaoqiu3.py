#-*-coding:cp936-*-
#韩雪
#2018年11月1日
#功能：小球类3
from tkinter import*
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
        self.y=starts[1]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=1
        if pos[3]>=self.canvas_height:
            self.y=-1
        if pos[0]<=0:
            self.x=1
        if pos[2]>=self.canvas_width:
            self.x=-1


tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
ball=Ball(canvas,'yellow')
ball2=Ball(canvas,'blue')
ball3=Ball(canvas,'green')


while True:
     ball.draw()
     ball2.draw()
     ball3.draw()
     tk.update_idletasks()
     tk.update()
     time.sleep(0.01)


