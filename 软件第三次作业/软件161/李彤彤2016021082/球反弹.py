sum = 100
height = sum/2

for n in range(0, 11):
    sum += 2 * height
    height = height / 2

print('共经过距离：',sum)
print ('第十次反弹高度：',height)
