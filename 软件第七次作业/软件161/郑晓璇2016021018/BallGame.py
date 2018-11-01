#！/usr/bin/python
#-*-coding:utf-8-*-
#···
#编写人：郑晓璇
#编写时间：20181101
#实现功能：用tkinter库写三个不同颜色的小球

from tkinter import *
import time
import random

tk = Tk()

class Ball:
    def __init__(self, canvas, color, b, l):
        self.canvas = canvas
        self.b = b
        self.l = l
        self.id = canvas.create_oval(10, 10, b, b, fill = color)
        self.canvas.move(self.id, 245, l)

        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        #随机排列
        self.x = starts[0]
        self.y = starts[1]
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        #让小球水平和垂直移动
        pos = self.canvas.coords(self.id)

        #判断小球是否撞到画布顶部或者底部，保证小球反弹回去，不消失
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        
tk.title("BallGame")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk,width = 800, height = 600, bd = 0, highlightthickness =0 )
canvas.pack()

tk.update()

#小球实例化
ball1 = Ball(canvas, 'blue', 60, 200)
ball2 = Ball(canvas, 'purple', 70, 300)
ball3 = Ball(canvas, 'orange', 80, 400)
while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
