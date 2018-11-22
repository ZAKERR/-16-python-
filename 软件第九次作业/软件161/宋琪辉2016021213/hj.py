"""
import jieba
from collections import Counter
with open("shui.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()

words=jieba.cut(article)
c=Counter(words).most_common(100)
with open("result1.txt",'w',encoding='utf-8') as fw:#打开文件
    for x in c:
        if len(x[0])>1:
        #if x[0] not in ["，","。"]:
            fw.write("{0},{1}\n".format(x[0],x[1]))
"""
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
with open("shui.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()
words=jieba.cut(article)#分词
wordlist=list(words)
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("heart.png")
image2=np.array(image1)
#属性
wc=WordCloud(background_color="white",
             mask=image2,
             max_words=100,
             font_path="c:\Windows\Fonts\simfang.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")
plt.imshow(wc)
plt.axis("off")
plt.show()
