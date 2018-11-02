请上传代码和截图!
#功能：运用turtle奥运五环
#编写人：安向永
#时间2018.10.22
ipaomi=turtle
ipaomi.shape('turtle')#把画笔设置为小乌龟
ipaomi.pensize(width=3)#设置画笔宽度
color = ['blue','black','red','yellow','green']
p_x = [-110,0,110,-55,55]
p_y = [-25,-25,-25,-75,-75]

for i in range(5):
    ipaomi.color(color[i])
    ipaomi.penup()
    ipaomi.goto(p_x[i],p_y[i])
    ipaomi.pendown()
    ipaomi.circle(45)

turtle.down()
