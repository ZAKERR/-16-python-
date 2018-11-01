from tkinter import *
import time
import random
#生成小球类

class Ball:
    
    def __init__(self,canvas,color):
        self.canvas=canvas
        
        a=[(50,50,100,100),(75,75,25,25),(25,25,50,50)]
        random.shuffle(a)
        self.id=canvas.create_oval(a[0],fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=starts[1]
        #确定画布的高度
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #让小球水平和垂直移动
        pos=self.canvas.coords(self.id)
        #判断小球是否撞到画布顶部或者底部，保证小球反弹回去，不消失
        if pos[1]<=0:self.y=1
        if pos[3]>=self.canvas_height:self.y=-1
        if pos[0]<=0:self.x=1
        if pos[2]>=self.canvas_width:self.x=-1



tk=Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

#对小球进行实例化
ball1 = Ball(canvas,'red')
ball2 = Ball(canvas,'blue')
ball3 = Ball(canvas,'yellow')


while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    
   
    tk.update_idletasks()
    tk.update()
    time.sleep(.01)

   
