#-*-coding:utf-8-*-

while 1:

    age = input('请输入孔子年龄(输入0结束)：')

    if(int(age)<15 and int(age)>0):
        print('茁壮成长，天真无邪。')
    elif(int(age)<30 and int(age)>=15):
        print('志在学习。')
    elif(int(age)<40 and int(age)>=30):
        print('成长为顶天立地的男子汉。')
    elif(int(age)<50 and int(age)>=40):
        print('对生活上的事没有困惑，不再迷茫。')
    elif(int(age)<60 and int(age)>=50):
        print('知道自己的命运，不大喜大悲，不怨天尤人。')
    elif(int(age)<70 and int(age)>=60):
        print('看透人生，听逆耳之言也不生气。')
    elif(int(age)>=70 and int(age)!=73):
        print('顺其自然，随遇而安,颐养天年。')
    elif(int(age)==73):
        print('孔子享年73岁，卒。')
    elif(int(age)==0):
        break
