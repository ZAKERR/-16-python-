#！/usr/bin/python
#-*-coding:utf-8-*-
#···
#编写人：郑晓璇
#编写时间：20180927
#功能：计算器实现
#注意中文的字符输入除了utf8之外，还得在中文前加上u

#定义函数
def add(a,b):#相加
    return a+b
def subtract(a,b):#相减
    return a-b
def multiply(a,b):#相乘
    return a*b
def divide(a,b):#相除
    return a/b
print("选择的运算：")
print("+.相加")
print("-.相减")
print("*.相乘")
print("/.相除")
choice=input("请输入您的选择：")
x=int(input("请输入第一个数字："))
y=int(input("请输入第二个数字："))
if choice=='+':
    print(x,"+",y,"=",add(x,y))
elif choice=='-':
    print(x,"-",y,"=",subtract(x,y))
elif choice=='*':
    print(x,"*",y,"=",multiply(x,y))
elif choice=='/':
    print(x,"/",y,"=",divide(x,y))
else:
    print("输入错误")
