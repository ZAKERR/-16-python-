from tkinter import *           
import time
import random
tk=Tk()        #创建一个界面
tk.title("弹球游戏")
canvas=Canvas(tk,width=800,height=600,bg="skyblue",bd=0,highlightthickness = 0)
tk.resizable(0,0) #表示边框不能被拉伸
canvas.pack()  #使部件放在主窗口中
tk.update()    #刷新界面
class Ball:  #球的类
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)  #在画布上画出一个球
        self.canvas.move(self.id,240,100)      #初始球的位置
        stat=[-3,-2,-1,1,2,3]   
        random.shuffle(stat)
        self.x=stat[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()  #获取画布的的高度
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False 
    def hit_paddle(self, pos):       #判断输赢
        paddle_pos = self.canvas.coords(self.paddle.id )
        if pos[2]>= paddle_pos[0] and pos[0]<= paddle_pos[2]:
            if pos[3]>= paddle_pos[1] and pos[3]<= paddle_pos[3]:
                return True
        return False
    def draw(self): #小球移动
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:  #判断小球是否碰到边框，如果碰到回弹
            self.y=3
        if pos[3]>=self.canvas_height:  #判断球拍是否有接到球 ，如果没接到游戏结束
            self.hit_bottom=True
        if self.hit_paddle(pos)==True:  #判断求是否碰到了球拍，如果碰到了使小球回弹
            self.y=-3
        if pos[0]<=0: #来判断球拍是不是碰到了边框，，
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
class Paddle: #球拍的的类
    def __init__(self,canvans,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,150,10,fill=color)
        self.canvas.move(self.id,400,450)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)  #通过按键来使球拍移动
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
    def turn_left(self,event): #每次按键球拍移动的距离
        self.x=-5
    def turn_right(self,event):
        self.x=5
    def draw(self):  #球拍移动的方法
        pos=self.canvas.coords(self.id)
        self.canvas.move(self.id, self.x, 0)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
paddle=Paddle(canvas,"blue")
ball=Ball(canvas,paddle,"red")
while True: #用循环 如果球怕没有接到球就推出
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    else:
        break
    tk.update_idletasks()# 不停的刷新画布
    tk.update()
    time.sleep(0.01)
