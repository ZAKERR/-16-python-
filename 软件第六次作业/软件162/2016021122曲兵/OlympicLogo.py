import turtle #导入turtle模块

turtle.pensize(9)

turtle.color("cornflowerblue") #定义颜色
turtle.penup() #penup和pendown()设置画笔抬起或放下时是否绘制直线
turtle.goto(-110,-25)   #初始位置以中心坐标为(0,0)
turtle.pendown() 
turtle.circle(45)  #绘制圆的半径

turtle.color("black")
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("crimson")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.color("lime")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)
