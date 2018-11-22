import jieba
from collections import Counter
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import re
import numpy as np
import pylab

jieba.load_userdict("key.txt");
with open("source4.txt","r",encoding='utf-8') as f:
    str = f.read()

str = re.sub(r"[\s+\.\!\/_,$%^(*+\" “”\']+|[+——！，。？、~@#￥%……&*（）]+", "",str)
cut_result = jieba.cut(str,cut_all=True)
count_result = Counter(cut_result).most_common(200)
real_result = ""


with open("result.txt","w",encoding='utf-8') as fn:
    for x in count_result:
        if x[0] not in ["的","吗","啊","在","一个"] and len(x[0]) >= 2:
            real_result = real_result  + " " + x[0]   # 可以改写成listStr = "/".join(wordlist)
            fn.writelines("关键词{0}:{1}\n".format(x[0],x[1]))

print(real_result)
font = r'C:\Windows\Fonts\FZSTK.TTF'
bg = np.array(Image.open("bg.png"));
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=1000,
               height=800,
               ).generate(real_result)
wc.to_file('data.png')  # 保存图片
plt.imshow(wc)  # 用plt显示图片
plt.axis('off')  # 不显示坐标轴
pylab.show()  # 显示图片




