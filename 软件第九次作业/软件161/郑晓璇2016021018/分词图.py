import jieba
#from collections import Counter
import numpy as np
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
from collections import Counter
#openfile
with open("sanguoyanyi.txt","r",encoding='utf-8')as f:
    Str1=f.read()
#cut =jieba.cut(Str1)
#savesegresult
#with open("resul.txt",'w',encoding='utf-8')as f:
   # f.write(",".join(cut))

#words=jieba.cut(Str1)
#c=Counter(words).most_common(100)
#with open("result.txt","w",encoding="utf-8")as fw:
    #for x in c:
        #if x[0] not in ["，","。"]:
            #fw.write("{0},{1}\n".format(x[0],x[1]))

#分词
words=jieba.cut(Str1)
wordlist=list(words)
#处理背景图片
image1 = Image.open("01.png")
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
