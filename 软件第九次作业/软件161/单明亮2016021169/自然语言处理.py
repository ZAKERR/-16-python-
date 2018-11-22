#!/usr/bin/python
#-*-coding:utf-8-*-
#编写人：单明亮
#编写时间：20181115
import jieba
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
jieba.load_userdict("userdict.txt")
#open  file
with open('tianlongbabu.txt','r',encoding='utf-8') as f:
    Str1=f.read()
cut=jieba.cut(Str1)
#save segresult
with open('result.txt','w',encoding='utf-8') as f:
    f.write('/'.join(cut))
#fenci
words=jieba.cut(Str1)
wordlist=list(words)
#tong ji ci pin
c=Counter(words).most_common(100)
with open('result1.txt','w',encoding='utf-8') as fw:
    for x in c:
        if len(x[0])>1:
        #if x[0] not in ['，','。','的','“','”','：',',','？','…','、','！','‘','’','了','']:
            fw.write('{0},{1}\n'.format(x[0],x[1]))
#hui zhi ci yun
listStr="/".join(wordlist)
image1=Image.open("1.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",
             mask=image2,
             max_words=100,
             font_path="C:\Windows\Fonts\STLITI.TTF",
             max_font_size=300,
             random_state=300,
             margin=2)
wc.generate(listStr)
plt.figure("wc")
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.show()