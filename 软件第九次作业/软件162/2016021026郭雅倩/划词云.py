#划词云
import jieba
from PIL import Image
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import numpy as np
with open ("xiyouji.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()
words=jieba.cut(article)#分词
wordlist=list(words)
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("卡通1.jpg")
image2=np.array(image1)
wc=WordCloud(background_color="white",#属性
             mask=image2,
             max_words=100,
             font_path="C:/用户/pcC:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-simfang_31bf3856ad364e35_10.0.17134.1_none_6da2b04f8ac810fa\simfang.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")#保存图片
plt.imshow(wc)#用plt显示图片
plt.axis("off")#不显示做标轴
plt.show()#显示图片
