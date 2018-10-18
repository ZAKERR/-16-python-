import turtle;

pen = turtle.Pen();
color = ["blue","black","red","yellow","green"]
pos_x = [-110,0,110,-55,55];
pos_y = [-25,-25,-25,-75,-75]

for i in range(5):
    pen.color(color[i]);
    pen.penup();
    pen.goto(pos_x[i],pos_y[i]);
    pen.pendown();
    pen.circle(45)

turtle.done();