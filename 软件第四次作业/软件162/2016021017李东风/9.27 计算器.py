#计算器实现
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print(u"选择运算：")
print(u"1.加法   2.减法    3.乘法    4.除法")
choice =input("请输入你的选择：")

x=int(input("请输入第一个数："))
y=int(input("请输入第二个数："))

if choice == '1':
    print(x,"+",y,"=",add(x,y))
if choice == '2':
    print(x,"-",y,"=",subtract(x,y))
if choice == '3':
    print(x,"*",y,"=",multiply(x,y))
if choice == '4':
    print(x,"/",y,"=",divide(x,y))
