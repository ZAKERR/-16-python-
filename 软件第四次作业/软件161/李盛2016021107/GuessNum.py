#!/usr/bin/python
# -*-coding:utf-8-*-
'''
编写人：李盛
编写时间：2018.09.27
功能：猜数小游戏 要求有输入验证
'''
import random
n = 1
x = random.randint(0, 101)

while True:
    y = input('Please input the number you guessed [0, 100]: ')
    if y.isdigit():
        y = int(y)
        if x > y:
            print('Your number is smaller than computer.')
            n += 1
        elif x < y:
            print('Your number is greater than computer.')
            n += 1
        else:
            print('You are right. total %d times' % n)
            break
    else:
        print('输入非法，请重新输入。')
        n += 1
