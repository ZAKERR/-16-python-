# !/user/bin/python
# -*-coding:utf-8-*-
'''
编写人：夔纭嘉
编写时间：20180920
功能：孔子不同的年龄阶段
'''
a = int(input('请输入孔子的年龄:'))
if a >= 70:
    print('从心所欲')
elif a >= 60 and a < 70:
    print('耳顺')
elif a >= 50 and a < 60:
    print('知天命')
elif a >= 40 and a < 50:
    print('不惑')
elif a >= 30 and a < 40:
    print('长大成人')
elif a >= 15 and a < 30:
    print('学习阶段')
else :
    print('Out of range')

