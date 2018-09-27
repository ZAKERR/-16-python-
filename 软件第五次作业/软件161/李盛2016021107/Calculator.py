#!/usr/bin/python
# -*-coding:utf-8-*-
'''
编写人：李盛
编写时间：2018.09.27
功能：简单的实数计算器
'''
#import math
print('----------------------------')
print('1. add           2. subtract')
print('3. multiply      4. divide')
print('5. power          ')
print('----------------------------')


def operator(x, y, z):
    try:
        if z == 1:
            return x + y
        elif z == 2:
            return x - y
        elif z == 3:
            return x * y
        elif z == 4:
            return x / y
        elif z == 5:
            return x ** y
        #elif z == 6:
        #   return math.sqrt(x, y)
    except:
        print('错误：分母为0')


z = int(input('请选择运算（1/2/3/4/5）：'))
x = int(input('请输入第一个数字：'))
y = int(input('请输入第一个数字：'))
list1 = [1, 2, 3, 4, 5]
if z in list1:
    print('结果为：', operator(x, y, z))
else:
    print('输入非法')