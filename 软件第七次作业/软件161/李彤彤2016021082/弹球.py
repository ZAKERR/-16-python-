#生成界面
from tkinter import *
tk = Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 800, height = 600, bd = 0
                ,highlightthickness = 0)
canvas.pack()
tk.update()

from tkinter import *
import time
import random
class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        x = random.randint(20,35)
        n = random.randint(20,35)
        y = random.randint(45,50)
        z = random.randint(45,50)
        self.id = canvas.create_oval(x,n,z,y,fill = color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        
        self.x = starts[0]
        self.y = starts[1]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
           self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        
        
tk = Tk()
tk.title("TanQiuGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 800, height = 600, bd = 0
                ,highlightthickness = 0)
canvas.pack()
tk.update() 

#小球的实例化
ball = Ball(canvas,'black')
ball2 = Ball(canvas,'red')
ball3 = Ball(canvas,'blue')
while True:
    ball.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01) 
    

    
    
    






