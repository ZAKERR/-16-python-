#!user/bin/python
#-*-coding:utf-8-*-
'''
编写人：冯译贤
时间：2019.9.13
功能：求和
'''


len=0
sum=0;
print('输入成绩:')
while True:
    sum += int(input())
    len = len + 1
    judge=input('是否继续')
    if judge=='yes':
        print('输入成绩:')
    else :
        print(sum / len)

