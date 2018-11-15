#!/usr/bin/python
#-*-coding:utf-8-*-
#编写人：单明亮
#编写时间：20181115
import jieba
jieba.load_userdict("userdict.txt")
#open  file
with open('tianlongbabu.txt','r',encoding='utf-8') as f:
    Str1=f.read()
cut=jieba.cut(Str1)
#save segresult
with open('result.txt','w',encoding='utf-8') as f:
    f.write('/'.join(cut))
