#作者：胡荣胜
#时间：2018-11-15
#功能：分词
import jieba
#open file
with open("shuihuzhuan.txt",'r',encoding='utf-8') as f:
    str1 = f.read()
#分词
cut = jieba.cut(str1)
#save result
with open("shuihuresult.txt",'w',encoding='utf-8') as f:
    f.write(','.join(cut))
