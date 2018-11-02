from tkinter import *
import time
import random
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        skkk=[10,50,100,150,200]
        random.shuffle(skkk)
        self.id=canvas.create_oval(skkk[1],skkk[1],skkk[0],skkk[0],fill=color)
        sttt=[100,200,300,400,500]
        random.shuffle(sttt)
        self.canvas.move(self.id,sttt[0],sttt[1])
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
    def draw(self):
        #左负上负
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:self.y=2
        if pos[3]>=self.canvas_height:self.y=-2
        if pos[0]<=0:self.x=2
        if pos[2]>=self.canvas_width:self.x=-2
        
tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

#小球实例化
ball=Ball(canvas,'red')
ball2=Ball(canvas,'blue')
ball3=Ball(canvas,'green')
while True:
    ball.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
