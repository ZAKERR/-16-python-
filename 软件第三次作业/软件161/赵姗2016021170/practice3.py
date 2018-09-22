'''
编写人：赵姗 软件161班  2016021170
编写时间：20180921
功能：弹球游戏
注意：文中字符输出除了加utf-8以外，还得在中文前加u
'''
Sn=100.0
Hn=Sn/2
for n in range(2,11):
    Sn+=2*Hn
    Hn/=2
print('Total of road is %f' %Sn)
print('The tenth is %f meter' %Hn)