from collections import Counter
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np


article = open("三国演义.txt","r",encoding='UTF-8').read()
words = jieba.cut(article)
wordlist=list(words)

'''c=Counter(words).most_common(100)
with open("result.txt","w") as fw:
    for x in c:
        if x[0] not in ["  ","Page","、","","『", "』", "；","；","“", "”", "！" , "？", "」", "「", "，", "。","-", "：", " ","的", "了"]:
            fw.write("{0},{1}\n".format(x[0],x[1]))'''
liststr="/".join(wordlist)
image1=Image.open("heart.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",
             mask=image2,
             max_words=100,
             font_path="C:\Windows\Fonts\simfang.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(liststr)
plt.figure("wc")
plt.imshow(wc)
plt.axis("off")
plt.show()
