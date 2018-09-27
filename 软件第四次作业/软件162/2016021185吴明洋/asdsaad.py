i = int(input("请选择运算类型:(1代表加法 2代表减法 3代表乘法 4代表除法)"))
a1 = eval(input("请输入第一个数："))
a2 = eval(input("请输入第二个数："))
if i == 1:
    a1 = a1 + a2
elif i == 2:
    a1 = a1 - a2
elif i == 3:
    a1 = a1 * a2
else:
    a1 = a1 / a2
print(a1)
