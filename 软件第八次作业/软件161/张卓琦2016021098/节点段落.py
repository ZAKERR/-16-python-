import jieba

jieba.suggest_freq(('孔明','曰'),True)
with open('Harry Poter.txt','r',encoding = 'utf-8')as f:
    str1 = f.read()
cut = jieba.cut(str1)
with open('Harry Poter.txt','w',encoding = 'utf-8')as f:
    f.write(''.join(cut))
    
