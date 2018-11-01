from tkinter import *
import random
import time
class Ball:
    def __init__(self,canvas,color):
        self.speed = random.randint(3, 10)
        self.canvas=canvas
        size = random.randint(10, 60)
        self.id=canvas.create_oval(20,20,size+20,size+20,fill=color)
        self.canvas.move(self.id,245,100)
        
        self.x=self.speed
        self.y=self.speed
        
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #self.canvas.move(self.id,-5,0)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=self.speed
        if pos[3]>=self.canvas_height:
            self.y=-1 * self.speed
        if pos[0]<=0:
            self.x=self.speed
        if pos[2]>=self.canvas_width:
            self.x=-1 * self.speed
      
    
tk=Tk()
tk.title('BallGame')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk,width=800,height=700,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
ball1=Ball(canvas,'red')
ball2=Ball(canvas,'blue')
ball3=Ball(canvas,'yellow')

while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
