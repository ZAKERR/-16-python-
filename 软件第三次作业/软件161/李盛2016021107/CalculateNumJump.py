'''
开发人：  李盛
开发时间：2018_09_23
程序功能：见下述提示
'''
print("    Now, there is a ball that is falling from the height of 100m,", 
      "then jump back to half than before, after that, falling down.", 
      "Please telling me how many meters in total", 
      "in tenth time it hit the ground, and rebounding how many meters in this time?"
      )

'''
sum1 = ((100*(1-(0.5**10)))/0.5)*2 - 100
height = 100*(0.5**10)
print(sum1, height)
'''

height = float(100)
sum1 = float(100)
for i in range(2, 11):
    height /= 2
    sum1 = sum1 + (height*2)
print("第10次落地路程：", sum1, "第10次弹起高度：", height/2)
# 因为循环从第二次开始，所以高度就不应该从100开始，而是50，又因为高度没都是乘法运算，顾结果除以二
