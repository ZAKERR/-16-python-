import jieba
with open("hongloumeng.txt",'r',encoding='utf-8')as f:
    str1=f.read()
cut=jieba.cut(str1)
with open("result1.txt",'w',encoding='utf-8')as f:
    f.write("/".join(cut))


