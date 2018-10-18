"""
时间：2019年10月5
功能：小球弹弹
"""

height = 100
sum = 0;
for i in range(10):
    sum += height
    height /=2
    sum += height
print("第十次落地经过了",sum-height,"米， 第十次反弹的高度为：",height)
