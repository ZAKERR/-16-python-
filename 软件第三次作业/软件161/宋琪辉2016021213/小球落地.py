sum=0
a=0
high=100
for i in range(0,10):
    a=high/2
    sum+=high+a
    high=a   
print("小球共经过%lf米" %sum)
print("第十次反弹%lf米" %a)
