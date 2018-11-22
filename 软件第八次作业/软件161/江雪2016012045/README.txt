'''import jieba
jieba.load_userdict("userdict.txt")
s = u'世态人情，比明月清风更饶有滋味;' \
    u'作书读，可当戏看。书上的描摹，戏里的扮演，' \
    u'即使栩栩如生，究竟只是文艺作品;人情世态，都是天真自’' \
    u'然的流露，往往超出情理之外，新奇得令人震惊，令人骇怪，’' \
    u'给人以更深刻的效益，更奇妙的娱乐。惟有身处卑微的人，' \
    u'最有机缘看到世态人情的真相，而不是面对观众的艺术表演。'
cut = jieba.cut(s)
print("【Output】")
print(cut)
print('  '.join(cut))
'''

'''
# 全模式划分（分词）
import jieba
jieba.load_userdict("userdict.txt")
s = u'我想和朋友一起去北京博物馆'
cut = jieba.cut(s,cut_all=True)
print("【Output】")
print(cut)
print('  '.join(cut))
'''


''''''
import jieba
jieba.load_userdict("userdict.txt")
jieba.suggest_freq(('孔明','曰'),True)
#open file
with open("sanguo.txt",'rb') as f:
    Str1=f.read()
cut = jieba.cut(Str1)
#save seg result
with open ("result.txt",'w',encoding='utf-8') as f:
    f.write("~".join(cut))
