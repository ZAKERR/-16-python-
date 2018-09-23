'''
功能：判断各年龄段该干啥
日期：2018.9.20
名字：nyc
'''
while True:
    y = int(input('输入测试年龄：'))
    if y<15 and y>0:
        print('随便玩')
    elif y<30:
        print('该学习了')
    elif y<40:
        print('成家立业')
    elif y<50:
        print('不惑')
    elif y<60:
        print('知天命')
    elif y<70:
        print('耳顺')
    elif y<80:
        print('从心所欲')
    else:
        print('不逾矩')
