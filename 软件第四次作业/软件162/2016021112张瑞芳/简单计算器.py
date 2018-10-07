def jia(x,y):
    print(x+y) 
def jian(x,y):
    print(x-y) 
def cheng(x,y):
    print(x*y) 
def chu(x,y):
    print(x/y) 
x = int(input('请输入第一个数：')) 
c = input('请输入运算符+,-,*,/:') 
y = int(input('请输入第二个数：')) 
if c =='+':
    jia(x,y)
elif c=='-':
    jian(x,y) 
elif c=='*':
    cheng(x,y) 
else :
    chu(x,y) 
