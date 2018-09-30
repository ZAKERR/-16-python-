#!/usr/bin/python
#-*-coding:utf-8-*-
#编写人：赵姗
#编写时间：20180930
#功能；计算器实现
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("选择运算：")
choice = input("输入你的选择(加/减/乘/除):")
s = int(input("输入第一个数字: "))
m = int(input("输入第二个数字: "))
if choice == '加':
    print(s, "+", m, "=", add(s, m))
elif choice == '减':
    print(s, "-", m, "=", subtract(s, m))
elif choice == '乘':
    print(s, "*", m, "=", multiply(s, m))
elif choice == '除':
    print(s, "/", m, "=", divide(s, m))
