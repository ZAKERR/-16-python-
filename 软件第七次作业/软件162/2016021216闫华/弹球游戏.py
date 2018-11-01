#实现游戏背景窗体
import random
import time
from tkinter import*
#生产小球类
class Ball:
          def __init__(self,canvas,color,x,y):
                    self.canvas=canvas
                    self.id=canvas.create_oval(10,10,45,45,fill=color)
                    self.canvas.move(self.id,x,y)
                    starts=[-3,-2,-1,1,2,3]
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
                   
tk = Tk()
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=800,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#小球的实例化
Ball2 = Ball(canvas,'black',500,666)
Ball1 = Ball(canvas,'red',222,333)
Ball= Ball(canvas,'blue',400,200)
while True:
          Ball.draw()
          Ball1.draw()
          Ball2.draw()
          tk.update_idletasks()
          tk.update()
          time.sleep(0.01)          
