#!/user/bin/python
#-*-coding:utf-8-*-
'''
编写人：杨燕芳
编写时间：20181005
功能：计算器的实现
'''
#定义函数
def add(x,y):
    return x+y
def jian(x,y):
    return x-y
def cheng(x,y):
    return x*y
def chu(x,y):
    return x/y

print(u"选择运算：")
print(u"+   -    *    /")
choice =input("请输入你的选择：")

x = int(input(u'请输入第一个数字：'))
y = int(input(u'请输入第二个数字：'))

if choice == '+':
    print(x,'+',y,'=',add(x,y))
elif choice == '-':
    print(x,'-',y,'=',jian(x,y))
elif choice == '*':
    print(x,'*',y,'=',cheng(x,y))
elif choice == '/':
    print(x,'/',y,'=',chu(x,y))
else:
    print(u'您的输入出错！')



