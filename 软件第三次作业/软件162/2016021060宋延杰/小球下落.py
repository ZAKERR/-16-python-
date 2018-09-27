sum=0.0
fhigh=0.0
high=100
for i in range(0,10):
    fhigh=high/2
    sum+=high+fhigh
    high=fhigh    
print("小球共经过%lf米" %sum)
print("第十次反弹%lf米" %fhigh)
