from turtle import *  
  
colors=['blue','black','red','yellow','green']  
for i in range(5):  
    x = -100+100*i if i<3 else 50*(-1)**i  
    y = 50 if i<3 else 0  
    up(),goto(x,y),width(5),down()  
    color(colors[i])  
    circle(40)  
#  
color('black')  
up(),goto(-80,-80),down()  
write("安小飞良心之作",font=("Aril",16,'bold'))  
done()
