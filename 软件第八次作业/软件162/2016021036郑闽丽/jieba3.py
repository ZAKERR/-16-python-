import jieba

#Jieba.load_xiyouji("xiyouji.txt")
jieba.suggest_freq(('孙悟空','曰'),True)
#open flie
with open("xiyouji.txt",'r',encoding='utf-8') as f:
    str1=f.read()
cut=jieba.cut(str1)
#save segresult
with open("result.txt",'w',encoding='utf-8') as f:
    f.write("/".join(cut))
