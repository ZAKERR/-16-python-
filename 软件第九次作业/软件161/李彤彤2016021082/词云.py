#划词云
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
with open("三国演义.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()
words=jieba.cut(article) #分词
wordlist=list(words)
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("heart.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",#属性
             mask=image2,
             max_words=500,
             font_path="C:\Windows\Fonts\simfang.ttf",
             max_font_size=100,
             random_state=60,
             margin=2)
wc.generate(listStr)
plt.figure("wc")#保存图片
plt.imshow(wc)#显示图片
plt.axis("off")#不显示坐标轴
plt.show()#显示图片
