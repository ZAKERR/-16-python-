#编写人：单明亮
#编写时间：201809
#编写题目：孔子
a=int(input("请输入你的年龄： "))
if a>=70:
    print("从心所欲")
elif a<70 and a>=60:
    print("耳顺")
elif a<60 and a>=50:
    print("知天命")
elif a<50 and a>=40:
    print("无惑")
elif a<40 and a>=30:
    print("立")
elif a<30 and a>=15:
    print("志于学")
else :
    print("吃吃吃")
