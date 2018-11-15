#conding = utf-8
#编写人：宋琪辉
#编写时间：20181115
#编写内容：水浒传分割
#coding:utf-8

import jieba
#jieba.load_userdict("userdict.txt")
with open("shui.txt",'r',encoding='utf-8') as f:
    str1=f.read()

cut=jieba.cut(str1)
with open("result.txt",'w',encoding='utf-8') as f:
    f.write("/".join(cut))
