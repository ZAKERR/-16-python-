import jieba
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

#分词
with open("西游记.txt",'r',encoding='utf-8') as f:
    article=f.read()
words=jieba.cut(article)
wordlist=list(words)
'''
#统计词频
c=Counter(words).most_common(100)
with open("西游记.txt","w",encoding="utf-8")as fw:
    for x in c:
        if x[0] not in ["，","。","你","我","他"]:
            fw.write("{0},{1}\n".format(x[0],x[1]))
'''
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("heart.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",
             mask=image2,
             max_words=100,
             font_path="C:\Windows\Fonts\simfang.ttf",
             max_font_size=40,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
'''
#jieba.load_userdict("userdict.txt")
jieba.suggest_freq(('孔明','曰'),True)
with open("马蹄下的断枪.txt",'r',encoding='utf-8') as f:
    str1=f.read()
    
cut = jieba.cut(str1)

with open("马蹄下的断枪.txt",'w',encoding='utf-8') as f:
    f.write(" ".join(cut))
'''
