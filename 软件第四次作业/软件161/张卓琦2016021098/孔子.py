#-*-coding:utf-8-*-
while True:
    age = int(input('请输入孔子年龄:'))
    if age < 0 or age >73:
        print('孔子还未出生/已经去世了')
    elif age >= 0 and age <= 15:
        print('天真无邪')
    elif age <= 30:
        print('用心学习')
    elif age <= 40:
        print('能够自立！')
    elif age <= 50:
        print('不会被外界事物迷惑')
    elif age <= 60:
        print('懂得了天命')
    elif age <= 73:
        print('追随自己的内心，无所拘束')
    elif age == 73:
        print('孔子去世了，享年73岁')
