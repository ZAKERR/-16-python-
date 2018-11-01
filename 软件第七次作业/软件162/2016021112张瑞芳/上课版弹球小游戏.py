#_*_ coding:cp936 _*_
#author:����
#date:20181101
#������ײ
func:"������Ϸ��������"
from tkinter import *
import time
import random
#����С����

class Ball:
    def __init__(self,canvas,color):
       self.canvas=canvas
       #������Ĵ�С ������״
       #self.id=canvas.create_oval(10,10,50,50,fill=color)
       ad=[(10,10,50,50),(20,20,35,35),(30,30,90,90)]
       random.shuffle(ad)
       self.id=canvas.create_oval(ad[0],fill=color)
       #�ı���ĳ�ʼλ��
       a=random.randint(0,self.canvas.winfo_height())
       b=random.randint(0,self.canvas.winfo_width())
       self.canvas.move(self.id,a,b)
       starts=[-3,-2,-1,1,2,3]
       random.shuffle(starts)#shuffle�����������˳��
       self.x=starts[0]
       self.y=starts[1]
       self.canvas_height=self.canvas.winfo_height()#��ȡ�����ĸ߶�
       self.canvas_width=self.canvas.winfo_width()#��ȡ�����Ŀ��
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)#����С���ƶ�
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3#�ж��������±߿򼴻ص�
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0: #���ж����ǲ������������ұ߿�
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
#���ɽ���
tk=Tk()
tk.title("game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=1000,height=600,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#С��ʵ����
ball1=Ball(canvas,'green')
ball2=Ball(canvas,'red')
ball3=Ball(canvas,'blue')
#ˢ�»���
while True:
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()#��ͣ��ˢ�»���
    tk.update()
    time.sleep(0.001)
