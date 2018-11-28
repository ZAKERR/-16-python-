from collections import Counter
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

# fenci

with open("红楼梦.txt", 'r', encoding='utf-8')as f:
    article = f.read()

''''
words = jieba.cut(article)

# 统计词性
c = Counter(words).most_common(100)
with open("result.txt", "w", encoding="utf-8") as fw:
    for x in c:
        # if x[0] not in ["，", "。"]:
        if x[0] not in ["  ", "Page", "、", "", "『", "』", "；", "；", "“", "”", "！", "？", "」", "「", "，", "。", "-", "：",
                        " ", "的", "了"]:
            fw.write("{0},{1}\n".format(x[0], x[1]))'''

words = jieba.cut(article)
wordlist = list(words)
# 绘制词云
listStr = "/".join(wordlist)
""""image1 2 mask 加背景图片"""
image1 = Image.open("0.png")
image2 = np.array(image1)
wc = WordCloud(background_color="white", mask=image2, max_words=100, font_path="D:\Python\simfang.ttf",
               max_font_size=50, random_state=30)

wc.generate(listStr)
plt.figure("wc")
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
