import jieba
#import pylab
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np

with open('sanguo.txt','r',encoding='utf-8') as f:
    str=f.read()
    
#cut=jieba.cut(str,cut_all=True)

#with open('result.txt','w',encoding='utf-8') as f:
    #f.write(' '.join(cut))

words=jieba.cut(str)
wordlist=list(words)
#huizhiciyun
listStr='/'.join(wordlist)
image1=Image.open('哆啦A梦.png')
image2=np.array(image1)
wc=WordCloud(background_color='pink',
             mask=image2,
             max_words=100,
             font_path='C:\Windows\Fonts\simfang.ttf',
             max_font_size=50,
             random_state=30,
             margin=2)

wc.generate(listStr)
plt.figure('wc')
plt.imshow(wc)
plt.axis('off')
plt.show()

#c=Counter(words).most_common(100)
with open('resul.txt','w',encoding='utf-8')as fw:
    for x in c:
        if len(x[0])>1:
        #if x[0] not in ['，','。']:
            fw.write('{0},{1}\n'.format(x[0],x[1]))

