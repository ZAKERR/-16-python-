#!/usr/bin/python
#-*-coding:utf-8-*-
'''
编写人 鲍蕾
编写时间20181115
'''
import jieba
#open file
with open("xiyouji.txt",'r',encoding='utf-8')as f:
    str=f.read()
cut=jieba.cut(str,cut_all=True)
#save seg result
with open("result.txt",'w',encoding='utf-8')as f:
    f.write("/".join(cut))
