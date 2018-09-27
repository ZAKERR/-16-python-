sum=0
heigth =100.0
for i in range(0,10):
    sum+=heigth
    heigth=heigth/2
    sum+=heigth
print(sum-heigth,heigth)
