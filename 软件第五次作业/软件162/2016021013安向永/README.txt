请上传代码和截图!
#-*-coding:utf-8-*-
#···
#编写人：安向永
#编写时间：2018108
#功能：实现计算器
#注意中文的字符输入除了utf8之外，还得在中文前加上u

choice=int(input('选择运算：\n1、相加\n2、相减\n3、相乘\n4、相除\n请输入您的选择（1/2/3/4):'))
num1=int(input("请输入第一个数:"))
num2=int(input("请输入第二个数:"))
def add(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y
if choice == 1:
        print('{}+{}={}'.format(num1,num2,add(num1,num2)))
elif choice == 2:
        print('{}-{}={}'.format(num1,num2,jian(num1,num2)))
elif choice == 3:
        print('{}*{}={}'.format(num1,num2,cheng(num1,num2)))
elif choice == 4:
        print('{}/{}={}'.format(num1,num2,chu(num1,num2)))
else:
        print("输入非法")
