#conding = utf-8
#编写人：仉玉营
#编写时间：20181116
#功能：统计三国演义
import  jieba

txt = open("三国演义.txt","r",encoding='UTF-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

jieba.suggest_freq(('孔明','曰'),True)
for word in words:
    if  len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
        
items = list(counts.items())#将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(len(items)):
    word,count=items[i]
    w=open('文本统计1.txt','a')
    str1="{0:<15}  出现了{1:>10}次".format(word,count)#在文件里写入的数据
    
    w.write(str1)#在文件写入数据
    w.write("\n")
w.close()#关闭文件

