#conding = utf-8
#编写人：程亮亮
#编写时间：20181122
#编写内容：分词2

'''
s="我想和女朋友一起去北京博物馆" #全模式分词
cut=jieba.cut(s,cut_all=True)
print(','.join(cut))
'''
'''
import jieba

#jieba.load_userdict("userdict.txt")

with open("shui.txt",'r',encoding='utf-8') as f:#打开文件
    str1=f.read() #读文本

cut=jieba.cut(str1)   #分词
with open("result.txt",'w',encoding='utf-8') as f:#处理完写入文件
    f.write("/".join(cut)) #用/分割词
'''
'''
import jieba  #取部分词
from collections import Counter
with open("shui.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()

words=jieba.cut(article) #分词
c=Counter(words).most_common(100) #
with open("result1.txt",'w',encoding='utf-8') as fw:#打开文件
    for x in c:
        if len(x[0])>1:#此大于等于两个
            if x[0] not in ["，","。","了","：","“","”","！","？","、","；"]:#去掉不用的符号
                fw.write("{0},{1}\n".format(x[0],x[1]))
'''

#划词云
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
with open("shui.txt",'r',encoding='utf-8') as f:#打开文件
    article=f.read()
words=jieba.cut(article) #分词
wordlist=list(words)
#绘制词云
listStr="/".join(wordlist)
image1=Image.open("he1.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",#属性
             mask=image2,
             max_words=100,
             font_path="C:\Windows\Fonts\simfang.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")#保存图片
plt.imshow(wc)#显示图片
plt.axis("off")#不显示坐标轴
plt.show()#显示图片
        
