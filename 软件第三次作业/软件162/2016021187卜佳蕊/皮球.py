# !/user/bin/python
# -*-coding:utf-8-*-
'''
编写人：卜佳蕊
编写时间：20180920
功能：皮球所经过的路程以及第10次反弹高度
'''
sum = 100
high = 100
for i in range(2,11):
    high = high / 2
    sum = sum + high * 2
print('在第10次落地共经过%fm'%sum)
print('第10次反弹的高度为%fm'%high)




