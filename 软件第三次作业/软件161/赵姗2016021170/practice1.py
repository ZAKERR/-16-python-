'''
编写人：赵姗 软件161班  2016021170
编写时间：20180920
功能：输出孔子的各阶段的状态
注意：文中字符输出除了加utf-8以外，还得在中文前加u
'''
year=int(input("输入孔子年龄："))
if year>0 and year<15:
    print("我还小着呢")
elif year<=30:
    print("至于学")
elif year<=40:
    print("而立")
elif year<=50:
    print("不惑")
elif year<=60:
    print("知天命")
elif year<=70:
    print("耳顺")
elif year<=73:
    print("从心所欲不逾矩")
elif year>73:#孔子的去世年龄
    print("已经西去")
else :
    print("你的格式出错了")
