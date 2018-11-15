import  jieba
#openfile
with open("xyj.txt","r",encoding='utf-8')as f:
    Str1=f.read()
cut =jieba.cut(Str1)
#savesegresult
with open("result.txt",'w',encoding='utf-8')as f:
    f.write(",".join(cut))

