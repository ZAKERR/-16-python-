import turtle
color=['blue','black','red','orange','green']
#环境定义开始
turtle.setup(650,600,50,50)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(5)
turtle.seth(-90)
#结束环境定义
x=0
 
#画环函数
def circle():
    turtle.pencolor(color[x])
    turtle.circle(70,540)
 
#循环5环
for i in range(5):
 
    #第三环改变起始位
    if i==3:
        turtle.penup()
        turtle.right(90)
        turtle.fd(350)
        turtle.left(90)
        turtle.fd(100)
        turtle.left(90)
        turtle.right(90)
        turtle.pendown()
    circle()
    x+=1
    turtle.right(180)
