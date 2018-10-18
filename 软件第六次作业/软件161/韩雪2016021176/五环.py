coordA=(-110,0,110,-55,55)
coordB=(-25,-25,-25,-75,-75)
cl=("red","blue","green","yellow","black")
i=0

from turtle import *
pensize(5)
for _ in range (5) :
    color(cl[i])
    penup()
    goto(coordA[i],coordB[i])
    pendown()
    circle(45)
    i=i+1
exitonclick()
