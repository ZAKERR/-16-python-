'''
#词频统计
import jieba
from collections import Counter

#fenci
with open("sanguo.txt",'rb') as f:
    article=f.read()
words=jieba.cut(article)
#tong ji ci pin
c=Counter(words).most_common(100)
with open ("result.txt",'w',encoding='utf-8') as fw:
    for x in c:
        #if x[0] not in ["，","。"]:
         if len(x[0])>1:
            fw.write("{0},{1}\n".format(x[0],x[1]))
'''

'''
from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
#from PIL import image
import jieba

#fenci
article="赵姗  背包客  喜欢看书  喜欢听音乐  喜欢美食  齐齐哈尔大学学生  计算机的学生 "
words= jieba.cut(article)
wordlist= list(words)
#绘制词云
listStr="/".join (wordlist)
wc=WordCloud(background_color="white",
             max_words=100,
             font_path="C:\Windows\Fonts\simafang.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(listStr)
plt.figure("wc")
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.show()
'''



from collections import Counter
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import jieba

#fenci
article=u'世态人情，比明月清风更饶有滋味;' \
    u'作书读，可当戏看。书上的描摹，戏里的扮演，' \
    u'即使栩栩如生，究竟只是文艺作品;人情世态，都是天真自’' \
    u'然的流露，往往超出情理之外，新奇得令人震惊，令人骇怪，’' \
    u'给人以更深刻的效益，更奇妙的娱乐。惟有身处卑微的人，' \
    u'最有机缘看到世态人情的真相，而不是面对观众的艺术表演。'
words= jieba.cut(article)
wordlist= list(words)
#绘制词云

str = ""
for word in wordlist:
    str = str + " " + word;

image1=Image.open("tu.png")
image2=np.array(image1)
wc=WordCloud(background_color="white",
             max_words=100,
             mask=image2,
             font_path=r"C:\Windows\Fonts\FZSTK.ttf",
             max_font_size=50,
             random_state=30,
             margin=2)
wc.generate(str)
plt.figure("wc")
wc.to_file("wc.png")
plt.imshow(wc)
plt.axis("off")
plt.show()