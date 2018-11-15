#conding = utf-8
#编写人：程亮亮
#编写时间：20181115
#编写内容：分词

'''
s="我想和女朋友一起去北京博物馆" #全模式分词
cut=jieba.cut(s,cut_all=True)
print(','.join(cut))
'''

import jieba
#jieba.load_userdict("userdict.txt")
with open("shui.txt",'r',encoding='utf-8') as f:
    str1=f.read()

cut=jieba.cut(str1)
with open("result.txt",'w',encoding='utf-8') as f:
    f.write("/".join(cut))
