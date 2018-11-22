from collections import Counter
import jieba
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
with open("hongloumeng1.txt",'r',encoding='utf-8')as f:
    article=f.read()
words=jieba.cut(article)
'''
with open("result1.txt",'w',encoding='utf-8')as f:
    f.write("/".join(cut))



c=Counter(words).most_common(100)
with open("rr.txt",'w',encoding='utf-8') as fw:
     for x in c:
        if len(x[0])>=2 :
            fw.write('{0},{1}\n'.format(x[0],x[1]))
'''
image1=Image.open("timg.png")
image2=np.array(image1)
wordlist2=[]
wordlist=list(words)
for i in wordlist:
    if len(i)>=2 and i not in ["我们","你们","咱们","这个","那个","什么","怎么","一个","如今","这里","那里","知道","就是","如此","不敢","几个"]:
        wordlist2.append(i)
        

listStr="/".join(wordlist2)
wc=WordCloud(background_color="white",mask=image2,max_words=100,font_path='C:\windows\Fonts\STZHONGS.TTF',max_font_size=50,
             random_state=30,margin=2)
wc.generate(listStr)
plt.figure("wc")
plt.imshow(wc)
plt.axis("off")
plt.show()
