#词云
import jieba
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

#读取文件

#分词
with open('Iloveyou.txt','r',encoding = 'utf-8')as f:
    article = f.read()
words = jieba.cut(article)
wordlist = list(words)

#绘制词云
listStr = '/'.join(wordlist)
image1 = Image.open("heart.png")
#变成矩阵模式
image2 = np.array(image1)
wo = WordCloud(background_color="white",max_words=100,
               mask = image2,
               font_path= "C:\Windoes\Fonts\simfang.ttf",
               max_font_size = 50,
               random_state = 30,
               margin = 2)
wo.generate(listStr)
#标题
plt.figure("wo")
wo.to_file("wo.png")
plt.imshow(wo)
plt.axis("off")
plt.show()
               
