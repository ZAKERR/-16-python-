#判断年龄阶段
x = int(input('请输入你的年龄：'))
if  x>0 and x<15 :
          print('\n玩')
elif x>=15 and x<30 :
          print('\n志于学')
elif x>=30 and x<40 :
          print('\n而立')
elif x>=40 and x<50 :
          print('\n不惑')
elif x>=50 and x<60 :
          print('\n知天命')
elif x>=60 and x<70:
          print('\n')
else :
          print('\n从心所欲，不逾矩')
