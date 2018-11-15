from jieba import *

s ="i have a car"

cut = jieba.cut(s)

print ('Output')
print (cut)
print (','.join(cut))

