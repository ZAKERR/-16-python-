import jieba
from collections import Counter
from  wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image#导入图片处理库

import numpy as np
#读取文件
with open('三国.txt','rb') as f:
    article=f.read()
#分词
words = jieba.cut(article)
wordlist = list(words)

#处理背景图片
image1 = Image.open("1.png")
image2 = np.array(image1)#将图片变成矩阵
#绘制词云
listStr="/".join(wordlist)#使用/连接
wc=WordCloud(background_color="white",#背景色
             mask=image2,
             max_words=100,#最多词数
             font_path="C:\Windows\Fonts\simfang.ttf", #字体路径
             max_font_size=50,#字体的最大值
             random_state=30, #随机状况
             margin=2)#词距离
wc.generate(listStr) #对listStr生成词云
plt.figure("wc")
wc.to_file("wc1.png")#保存为图片
plt.imshow(wc)
plt.axis("off")#关闭坐标系
plt.show()
