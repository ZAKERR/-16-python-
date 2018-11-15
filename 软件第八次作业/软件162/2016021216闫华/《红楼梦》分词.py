#作者：闫华
#时间：2018.11.15
#功能：《红楼梦》分词
import jieba
#打开文档
with open("a dream in red mansion.txt",'r',encoding='utf-8') as f:
          str1=f.read()
cut = jieba.cut(str1)
#将结果写入文档
with open("result.txt",'w',encoding='utf-8') as f:
          f.write("_".join(cut))
