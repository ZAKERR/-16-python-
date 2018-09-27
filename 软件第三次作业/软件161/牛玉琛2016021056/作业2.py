height = 100.0
Sum = 100.0
for i in range(1,10):
    Sum += height
    height/=2
print('第10次落地时共经过 %f 米' %Sum)
print('第10次能反弹 %f 米' %height)
