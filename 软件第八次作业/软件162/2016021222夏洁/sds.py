import jieba

with open("西游记.txt",'r',encoding='utf-8')as f:
     str=f.read()

cut=jieba.cut(str,cut_all=True)

with open("result.txt",'w',encoding='utf-8')as f:
     f.write(" ".join(cut))
