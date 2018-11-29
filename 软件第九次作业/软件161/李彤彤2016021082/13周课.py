from collections import Counter
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib import pyplot as plt

#第十二周 45
import jieba

'''with open('sanguo.txt','r',encoding='utf-8') as f:
     str1=f.read()
cut=jieba.cut(str1,cut_all=True)
with open('result.txt','w',encoding='utf-8') as f:
    f.write(' '.join(cut))'''
#第十三周
with open('三国演义.txt','r',encoding='utf-8') as f:
     str1=f.read()
words=jieba.cut(article)
wordlist=list(words)
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("123456789.png")
image2=np.array(image1)
#tong ji ci pin
wc=WordCloud(background_color="white",
             mask=image2,
             max_words=100
             font_path="C:\Users\李彤彤\Downloads\bb5178.ttf"
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")
wc.to_file("wc.png")#保存图片
plt.imshow("wc")#用plt显示图片
plt.axis("off")#不显示坐标轴
plt.show()
'''c=Counter(words).most_common(100)
with open ('result.txt','w',encoding='utf-8')as fw:
     for x in c:
         if len(x[0])>1#只显示两字及以上词语
          #if x[0] not in ['，','。']:
              
              
               fw.write('{0},{1}\n'.format(x[0],x[1])
                        
