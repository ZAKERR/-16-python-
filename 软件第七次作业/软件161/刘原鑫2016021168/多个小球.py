from tkinter import *
import time
import random

# 生成小球类
class ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        a = random.randint(10, 40)
        self.id = canvas.create_oval(15, 20, a+15, a+25, fill=color)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.canvas.move(self.id, x, y)
        self.x=-5
        self.y=-5
        self.canvas_height=self.canvas.winfo_height()#获取窗口高度
        self.canvas_width=self.canvas.winfo_width()#获取窗体宽度
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        post=self.canvas.coords(self.id)#x1,y1,x2,y2
        if post[0]<=0:self.x=5
        if post[1]<=0:self.y=5
        if post[2]>=self.canvas_width:self.x=-5
        if post[3]>=self.canvas_height:self.y=-5


# 生成游戏背景窗体

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()# 刷新

# 小球实例化
ball_1 = ball(canvas, 'yellow')
ball_2 = ball(canvas, 'blue')
ball_3 = ball(canvas, 'green')
while True:
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
