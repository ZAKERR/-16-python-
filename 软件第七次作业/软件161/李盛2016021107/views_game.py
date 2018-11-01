from tkinter import *
import time
import random

#生成小球类
class ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        
        self.id = canvas.create_oval(10, 10,25, 30, fill=color)

        x = random.randint(0, self.canvas.winfo_width())
        y = random.randint(0, self.canvas.winfo_height())
        self.canvas.move(self.id, x, y)

        start = [-3, -2, -1, 1, 2, 3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
    def draw(self):
        colors = ['yellow', 'pink', 'blue', 'gray', 'purple', 'green']
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 1
            
        if pos[1] <= 0:
            self.y = 2
            
        if pos[2] >= self.canvas_width:
            self.x = -1
            
        if pos[3] >= self.canvas_height:
            self.y = -2
            
    
#生成游戏背景窗体
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update() #刷新

#小球实例化
ball_1 = ball(canvas, 'yellow')
ball_2 = ball(canvas, 'blue')
ball_3 = ball(canvas, 'gray')
while True:
    ball_1.draw()
    ball_2.draw()
    ball_3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
