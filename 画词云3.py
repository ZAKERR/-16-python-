import jieba
from collections import Counter
from wordcloud import WordCloud 
from matplotlib import  pyplot as plt
from PIL import Image
import numpy as np

with open('三国演义.txt','r',encoding = 'utf-8') as f:
    article=f.read()
    jieba.load_userdict('userdate.txt')
    words = jieba.cut(article)
wordlist=[]
c=Counter(words).most_common(100)
for x in c:
     if len(x[0])==1:# or i in includes:
            continue
     elif x[0] in ['丞相']:
            wordlist.append('曹操')
     elif x[0] in ['孔明曰','孔明']:
            wordlist.append('诸葛亮')
     elif x[0] in ['玄德曰', '玄德']:
            wordlist.append('刘备')
     elif x[0] in ['关公', '云长']:
            wordlist.append('关羽')
     elif x[0] in ['都督']:
            wordlist.append('周瑜')
     else:
            wordlist.append(x[0])
            
#wordlist=list(words)
#画词云
listStr='/'.join(wordlist)
image1 = Image.open('r.png')
image2 = np.array(image1)
wc=WordCloud(background_color='white',
             mask = image2,
             max_words=100,
             font_path='C:\Windows\Fonts\simfang.ttf',  #加载字体路径，才可以显示汉语
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure('标题')
wc.to_file('r1.png')
plt.imshow(wc)
plt.axis('off')
plt.show()
