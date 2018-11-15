import jieba
#openfile
with open ("三国.txt",'r',encoding='utf-8') as f:
    str1=f.read()
Cut=jieba.cut(str1)
with open("result.txt",'w',encoding='utf-8') as f:
    f.write(",".join(Cut))
