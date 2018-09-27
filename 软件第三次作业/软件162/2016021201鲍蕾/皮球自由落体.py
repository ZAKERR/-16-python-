Sn=100.0
Hn=Sn/2
for n in range(2,11):
    Sn+=2*Hn
    Hn/=2
print('Total of road is %f' %Sn)
print('The tenth is %f meter' %Hn)
    
