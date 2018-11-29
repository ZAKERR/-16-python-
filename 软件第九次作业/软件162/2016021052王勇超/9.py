import jieba
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np


# 读取文件
article = open('水浒传.txt','r',encoding='utf-8').read()

# 分词
words = jieba.cut(article)
wordlist = list(words)

# 绘制词云
listStr = "/".join(wordlist)
image1 = Image.open("1.png")
image2 = np.array(image1)
wc = WordCloud(background_color='white',
               mask=image2,
               max_words=100,
               font_path="c:\windows\Fonts\simfang.ttf",
               max_font_size=50,
               random_state=30,
               margin=2)
wc.generate(listStr)
plt.figure("wc")
plt.imshow(wc)
plt.axis("off")
plt.show()