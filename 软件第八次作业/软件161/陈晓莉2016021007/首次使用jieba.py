import jieba

#jieba.load_userdict("userdict.txt")
jieba.suggest_freq(('孔明','曰'),True)
with open("马蹄下的断枪.txt",'r',encoding='utf-8') as f:
    str1=f.read()
    
cut = jieba.cut(str1)

with open("马蹄下的断枪.txt",'w',encoding='utf-8') as f:
    f.write(" ".join(cut))
