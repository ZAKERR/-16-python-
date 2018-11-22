from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import jieba
#jieba.load_userdict("userdict.txt")
'''#读取文件
with open('sanguo.txt','r',encoding='utf-8') as f:
     str1=f.read()
words=jieba.cut(str1)
c=Counter(words).most_common(100)
with open ('result.txt','w',encoding='utf-8')as fw:
     for x in c:
          if x[0] not in ['，','。']:
               fw.write('{0},{1}\n'.format(x[0],x[1]))'''
#开始
with open('sanguo.txt','r',encoding='utf-8') as f:
     str1=f.read()
words=jieba.cut(str1)
wordlist=list(words)
#绘制词云
listStr='/'.join(wordlist)
wc=WordCloud(background_color='white',
             max_words=100,
             font_path='C:\Windows\Fonts\simfang.ttf',
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
#wc.to_file('wc.png')
plt.figure('wc')
plt.imshow(wc)
plt.axis('off')
plt.show()
